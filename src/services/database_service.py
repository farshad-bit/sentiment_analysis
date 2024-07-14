import sqlite3

class DatabaseService:
    def __init__(self, db_name='sentiment_analysis.db'):
        self.db_name = db_name
        self.initialize_db()

    def initialize_db(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()

        # ایجاد جدول
        c.execute('''CREATE TABLE IF NOT EXISTS sentiments
                     (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      text TEXT, 
                      sentiment TEXT, 
                      date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

        conn.commit()
        conn.close()

    def save_sentiment(self, text, sentiment):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        # استفاده از پارامترهای جایگزین برای جلوگیری از SQL Injection
        c.execute("INSERT INTO sentiments (text, sentiment) VALUES (?, ?)", (text, sentiment))
        conn.commit()
        conn.close()

    def fetch_all_sentiments(self):
        conn = sqlite3.connect(self.db_name)
        c = conn.cursor()
        c.execute("SELECT * FROM sentiments")
        rows = c.fetchall()
        conn.close()
        return rows
