// src/views/static/js/sentiment_analyze.js

document.addEventListener('DOMContentLoaded', function () {
    console.log('App is ready');

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }

    async function analyzeSentiment() {
        const text = document.getElementById('text-input').value;
        
        const csrfToken = getCookie('csrf_access_token');

        console.log('CSRF Token:', csrfToken);

        if (!csrfToken) {
            alert('Please log in to get a CSRF token first.');
            return;
        }

        try {
            const response = await fetch('/analyze/api/sentiment', {  // تغییر مسیر URL به مسیر درست
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRF-TOKEN': csrfToken
                },
                body: JSON.stringify({ text: text })
            });

            console.log('Response status:', response.status); // لاگ برای وضعیت پاسخ
            console.log('Response:', response); // لاگ برای کل پاسخ

            if (response.status === 401) {
                alert('Unauthorized. Please log in again.');
                return;
            }

            if (response.ok) {
                const result = await response.json();
                console.log('Sentiment analysis result:', result); // لاگ برای نتیجه تحلیل احساسات
                document.getElementById('result-text').innerText = result.text;
                document.getElementById('result-sentiment').innerText = result.sentiment;
            } else {
                const errorText = await response.text();
                console.error('Sentiment analysis failed:', errorText); // لاگ برای متن خطا
                alert('Sentiment analysis failed');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('An error occurred while analyzing the sentiment.');
        }
    }

    document.getElementById('analyze-button').addEventListener('click', analyzeSentiment);
});
