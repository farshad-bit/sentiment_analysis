// src/views/static/js/trends.js

async function fetchTrends() {
    const token = document.cookie.split('; ').find(row => row.startsWith('access_token=')).split('=')[1];

    if (!token) {
        alert('Please log in to get a JWT token first.');
        return;
    }

    const response = await fetch('/trends/data', {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    });

    if (response.status === 404) {
        alert('API endpoint not found.');
        return;
    }

    if (response.status === 401) {
        alert('Unauthorized. Please log in again.');
        return;
    }

    if (response.ok) {
        const trends = await response.json();
        
        const trendNames = trends.map(trend => trend.sentiment);
        const trendValues = trends.map(trend => trend.count);

        const ctx = document.getElementById('trendsChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar', // 'line', 'pie', etc.
            data: {
                labels: trendNames,
                datasets: [{
                    label: 'Trend Values',
                    data: trendValues,
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
        alert('Error fetching trends');
    }
}

document.addEventListener('DOMContentLoaded', function() {
    fetchTrends();
});
