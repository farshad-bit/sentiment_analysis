// src/views/static/js/trends.js

async function fetchTrends() {
    // واکشی توکن JWT از کوکی‌ها
    const token = document.cookie.split('; ').find(row => row.startsWith('access_token=')).split('=')[1];

    if (!token) {
        alert('Please log in to get a JWT token first.');
        return;
    }

    // ارسال درخواست به سرور برای واکشی روندها
    const response = await fetch('/api/trends', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`
        }
    });

    if (response.ok) {
        const trends = await response.json();
        const labels = trends.map(trend => trend.name);
        const values = trends.map(trend => trend.value);

        // ایجاد نمودار با استفاده از Chart.js
        const ctx = document.getElementById('trendsChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar', // نوع نمودار
            data: {
                labels: labels,
                datasets: [{
                    label: 'Trends',
                    data: values,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    } else {
        alert('Error fetching trends: ' + response.statusText);
    }
}

fetchTrends();
