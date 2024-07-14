# Sentiment Analysis API

## Overview
This project provides a sentiment analysis API built with Flask. The API allows users to analyze the sentiment of text, returning whether the sentiment is positive, negative, or neutral.

## Features
- **Sentiment Analysis**: Analyzes the sentiment of provided text.
- **Multi-language Support**: Detects and translates text to English if it's in another language.
- **Database Storage**: Stores analyzed sentiments in an SQLite database.
- **Security**: Implements CSRF protection and input sanitization to prevent XSS and SQL Injection attacks.
- **Authentication**: Provides JWT-based authentication for secure access.

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Setup
1. Clone the repository:

    ```sh
    git clone https://github.com/farshad-bit/sentiment_analysis.git
    cd sentiment_analysis
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Set environment variables (optional):

    ```sh
    export SECRET_KEY='your-secret-key'
    export JWT_SECRET_KEY='your-jwt-secret-key'
    ```

5. Initialize the database:

    ```sh
    python -c "from src.services.database_service import DatabaseService; DatabaseService().initialize_db()"
    ```

## Usage

### Running the Server
To start the Flask server, run:

```sh
python app.py
