import requests
import sqlite3
import os
from config import NEWS_API_KEY

def fetch_articles():
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    articles = response.json().get('articles', [])

    db_path = os.path.join(os.path.dirname(__file__), 'news_aggregator.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for article in articles:
        cursor.execute('''
            INSERT INTO articles (title, description, content, url, categories, published_at)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (article['title'], article['description'], article['content'], article['url'], '', article['publishedAt']))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    fetch_articles()
    print("Articles fetched and inserted into the database.")
