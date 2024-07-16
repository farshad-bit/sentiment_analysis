// src/views/static/js/advanced_sentiment.js

async function analyzeAdvancedSentiment() {
    const text = document.getElementById('advanced-text-input').value;

    // Get the JWT token and CSRF token from cookies
    const token = document.cookie.split('; ').find(row => row.startsWith('access_token=')).split('=')[1];
    const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrf_access_token=')).split('=')[1];

    if (!token) {
        alert('Please log in to get a JWT token first.');
        return;
    }

    const response = await fetch('/api/advanced_sentiment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
            'X-CSRF-TOKEN': csrfToken  // Include the CSRF token in the headers
        },
        body: JSON.stringify({ text: text })
    });

    if (response.status === 401) {
        alert('Unauthorized. Please log in again.');
        return;
    }

    if (response.ok) {
        const result = await response.json();
        document.getElementById('advanced-result-original-text').innerText = result.original_text;
        document.getElementById('advanced-result-translated-text').innerText = result.translated_text;
        document.getElementById('advanced-result-sentiment').innerText = result.sentiment;
        document.getElementById('advanced-result-score').innerText = result.score.toFixed(2);
    } else {
        alert('Advanced sentiment analysis failed');
    }
}
