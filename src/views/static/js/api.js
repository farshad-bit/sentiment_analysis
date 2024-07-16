// src/views/static/js/api.js

async function analyzeSentiment() {
    const text = document.getElementById('text-input').value;

    // Get the JWT token and CSRF token from cookies
    const token = document.cookie.split('; ').find(row => row.startsWith('access_token=')).split('=')[1];
    const csrfToken = document.cookie.split('; ').find(row => row.startsWith('csrf_access_token=')).split('=')[1];

    if (!token) {
        alert('Please log in to get a JWT token first.');
        return;
    }

    const response = await fetch('/api/sentiment', {
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
        document.getElementById('result-text').innerText = result.text;
        document.getElementById('result-sentiment').innerText = result.sentiment;
    } else {
        alert('Sentiment analysis failed');
    }
}
