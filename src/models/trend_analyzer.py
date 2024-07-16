# src/models/trend_analyzer.py
import mysql.connector
import matplotlib.pyplot as plt

def get_db_connection():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3307,
        user='root',
        password='Farshad7013',
        database='sentiment_analysis'
    )

def plot_trends():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT sentiment, COUNT(*) as count FROM sentiments GROUP BY sentiment"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    sentiments = [row[0] for row in results]
    counts = [row[1] for row in results]

    plt.bar(sentiments, counts)
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.title('Sentiment Analysis Trends')
    plt.show()
