import sqlite3

def setup_database():
    conn = sqlite3.connect('app/news_aggregator.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY,
            title TEXT,
            description TEXT,
            content TEXT,
            url TEXT,
            categories TEXT,
            published_at TEXT
        )
    ''')
    
    print("Table 'articles' created or already exists.")

    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == '__main__':
    setup_database()
