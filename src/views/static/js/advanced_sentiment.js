document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('advanced-sentiment-form').addEventListener('submit', function (event) {
      event.preventDefault();
      analyzeAdvancedSentiment();
  });
});

async function analyzeAdvancedSentiment() {
  const text = document.getElementById('text-input').value;

  const csrfToken = getCookie('csrf_access_token');

  if (!csrfToken) {
      alert('CSRF token not found.');
      return;
  }

  try {
      const response = await fetch('/advanced/analyze', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'X-CSRF-TOKEN': csrfToken
          },
          body: JSON.stringify({ text: text })
      });

      if (response.status === 401) {
          alert('Unauthorized. Please log in again.');
          return;
      }

      if (response.ok) {
          const result = await response.json();
          document.getElementById('result-text').innerText = result.translated_text;
          document.getElementById('result-sentiment').innerText = result.sentiment;
      } else {
          alert('Advanced sentiment analysis failed');
      }
  } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while analyzing the sentiment.');
  }
}

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
  return null;
}
