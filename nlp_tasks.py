import spacy
import sqlite3
import os

def perform_nlp_tasks():
    try:
        # Load the spaCy model
        nlp = spacy.load('en_core_web_sm')

        # Connect to the database
        db_path = os.path.join(os.path.dirname(__file__), 'news_aggregator.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Example: Perform NLP tasks on article content
        cursor.execute('SELECT * FROM articles')
        rows = cursor.fetchall()

        for row in rows:
            if row[3]:  # Assuming 'content' is in the fourth column (index 3)
                doc = nlp(row[3])
                # Perform NLP tasks such as named entity recognition, dependency parsing, etc.
                for entity in doc.ents:
                    print(entity.text, entity.label_)
            else:
                print(f"Skipping article with ID {row[0]} due to empty content.")

        conn.close()

    except IOError as e:
        print(f"Error loading spaCy model: {e}")
    except sqlite3.OperationalError as e:
        print(f"Error accessing database: {e}")

if __name__ == '__main__':
    perform_nlp_tasks()
