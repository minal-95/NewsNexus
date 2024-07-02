import sqlite3
import pandas as pd
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from config import NEWS_API_KEY

# Download NLTK resources if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

def clean_and_preprocess():
    try:
        db_path = os.path.join(os.path.dirname(__file__), 'news_aggregator.db')
        conn = sqlite3.connect(db_path)
        articles = pd.read_sql_query('SELECT * FROM articles', conn)

        stop_words = set(stopwords.words('english'))

        def clean_text(text):
            if text:
                tokens = word_tokenize(text)
                tokens = [word.lower() for word in tokens if word.isalpha()]
                tokens = [word for word in tokens if word not in stop_words]
                return ' '.join(tokens)
            return ''

        articles['cleaned_content'] = articles['content'].apply(clean_text)

        conn.close()
        return articles

    except sqlite3.OperationalError as e:
        print(f"Error accessing database: {e}")

if __name__ == '__main__':
    articles = clean_and_preprocess()
    if articles is not None:
        print(f"{len(articles)} articles processed.")
