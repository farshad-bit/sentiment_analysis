# src/services/database_service.py
import mysql.connector
from mysql.connector import Error

class DatabaseService:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                port=3307,
                database='sentiment_analysis',
                user='root',
                password='Farshad7013'
            )
            if self.connection.is_connected():
                db_Info = self.connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
        except Error as e:
            print("Error while connecting to MySQL", e)

    def insert_sentiment(self, text, sentiment):
        try:
            cursor = self.connection.cursor()
            query = "INSERT INTO sentiments (text, sentiment) VALUES (%s, %s)"
            cursor.execute(query, (text, sentiment))
            self.connection.commit()
            cursor.close()
        except Error as e:
            print("Failed to insert record into MySQL table", e)

    def __del__(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")
