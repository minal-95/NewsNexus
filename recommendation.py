import sqlite3

def recommend_articles():
    try:
        db_path = 'app/news_aggregator.db'  # Adjust the path as needed
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Example: Select all articles
        c.execute("SELECT * FROM articles")
        rows = c.fetchall()

        for row in rows:
            print(row)  # Print each row as an example

        conn.close()

    except sqlite3.OperationalError as e:
        print(f"SQLite error: {e}")

if __name__ == '__main__':
    recommend_articles()
