// // src/views/static/js/main.js

// // این تابع زمانی که صفحه کاملاً بارگذاری می‌شود اجرا می‌شود
// document.addEventListener('DOMContentLoaded', function () {
//     // اضافه کردن رویداد 'submit' به فرم تحلیل احساسات
//     document.getElementById('sentiment-form').addEventListener('submit', function (event) {
//         event.preventDefault(); // جلوگیری از ارسال پیش‌فرض فرم
//         analyzeSentiment(); // فراخوانی تابع تحلیل احساسات
//     });
// });

// // تابع برای گرفتن کوکی بر اساس نام آن
// function getCookie(name) {
//     const value = `; ${document.cookie}`;
//     const parts = value.split(`; ${name}=`);
//     if (parts.length === 2) return parts.pop().split(';').shift();
//     return null;
// }

// // تابع برای تحلیل احساسات
// async function analyzeSentiment() {
//     const text = document.getElementById('text-input').value;

//     const token = getCookie('access_token');
//     const csrfToken = getCookie('csrf_access_token');

//     console.log('Access Token:', token); // برای اشکال‌زدایی
//     console.log('CSRF Token:', csrfToken); // برای اشکال‌زدایی

//     if (!token) {
//         alert('Please log in to get a JWT token first.');
//         return;
//     }

//     try {
//         const response = await fetch('/api/sentiment', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'Authorization': `Bearer ${token}`,
//                 'X-CSRF-TOKEN': csrfToken
//             },
//             body: JSON.stringify({ text: text })
//         });

//         if (response.status === 401) {
//             alert('Unauthorized. Please log in again.');
//             return;
//         }

//         if (response.ok) {
//             const result = await response.json();
//             document.getElementById('result-text').innerText = result.text;
//             document.getElementById('result-sentiment').innerText = result.sentiment;
//         } else {
//             alert('Sentiment analysis failed');
//         }
//     } catch (error) {
//         console.error('Error:', error);
//         alert('An error occurred while analyzing the sentiment.');
//     }
// }
