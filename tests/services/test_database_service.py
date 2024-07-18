# tests/services/test_database_service.py
import pytest
from unittest.mock import patch, MagicMock
from src.services.database_service import DatabaseService, save_sentiment, get_trends

@patch('src.services.database_service.mysql.connector.connect')
def test_database_connection(mock_connect):
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    db_service = DatabaseService()
    
    mock_connect.assert_called_once_with(
        host='localhost',
        port=3307,
        database='sentiment_analysis',
        user='root',
        password='Farshad7013'
    )
    assert db_service.connection == mock_conn

@patch('src.services.database_service.DatabaseService.insert_sentiment')
def test_save_sentiment(mock_insert_sentiment):
    save_sentiment("This is a test text", "Positive")
    mock_insert_sentiment.assert_called_once_with("This is a test text", "Positive")

@patch('src.services.database_service.mysql.connector.connect')
def test_insert_sentiment(mock_connect):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn

    db_service = DatabaseService()
    db_service.insert_sentiment("This is a test text", "Positive")

    mock_cursor.execute.assert_called_once_with("INSERT INTO sentiments (text, sentiment) VALUES (%s, %s)", ("This is a test text", "Positive"))
    mock_conn.commit.assert_called_once()
    mock_cursor.close.assert_called_once()

@patch('src.services.database_service.mysql.connector.connect')
def test_get_trends(mock_connect):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchall.return_value = [{'sentiment': 'Positive', 'count': 10}]
    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn

    db_service = DatabaseService()
    trends = db_service.get_trends()

    mock_cursor.execute.assert_called_once_with("SELECT sentiment, COUNT(*) as count FROM sentiments GROUP BY sentiment")
    mock_cursor.fetchall.assert_called_once()
    mock_cursor.close.assert_called_once()
    assert trends == [{'sentiment': 'Positive', 'count': 10}]
