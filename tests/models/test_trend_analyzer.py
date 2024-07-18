# tests/models/test_trend_analyzer.py
import pytest
from unittest.mock import patch, MagicMock
from src.models.trend_analyzer import plot_trends

@patch('src.models.trend_analyzer.plt')
@patch('src.models.trend_analyzer.get_db_connection')
def test_plot_trends(mock_get_db_connection, mock_plt):
    # تنظیمات mock برای اتصال دیتابیس و اجرای کوئری
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = [('Positive', 10), ('Negative', 5), ('Neutral', 7)]
    mock_get_db_connection.return_value = mock_conn

    plot_trends()

    mock_cursor.execute.assert_called_once_with("SELECT sentiment, COUNT(*) as count FROM sentiments GROUP BY sentiment")
    mock_cursor.fetchall.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_conn.close.assert_called_once()

    mock_plt.bar.assert_called_once_with(['Positive', 'Negative', 'Neutral'], [10, 5, 7])
    mock_plt.xlabel.assert_called_once_with('Sentiment')
    mock_plt.ylabel.assert_called_once_with('Count')
    mock_plt.title.assert_called_once_with('Sentiment Analysis Trends')
    mock_plt.show.assert_called_once()
