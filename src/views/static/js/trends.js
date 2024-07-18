// src/views/static/js/trends.js
document.addEventListener('DOMContentLoaded', async function () {
    const response = await fetch('/trends/data');
    if (response.ok) {
        const trends = await response.json();

        const categories = {
            'Very Good': 0,
            'Good': 0,
            'Neutral': 0,
            'Bad': 0,
            'Very Bad': 0
        };

        trends.forEach(trend => {
            if (trend.sentiment.toLowerCase() === 'positive') {
                if (trend.text.includes('very')) {
                    categories['Very Good']++;
                } else {
                    categories['Good']++;
                }
            } else if (trend.sentiment.toLowerCase() === 'negative') {
                if (trend.text.includes('very')) {
                    categories['Very Bad']++;
                } else {
                    categories['Bad']++;
                }
            } else {
                categories['Neutral']++;
            }
        });

        const data = {
            labels: Object.keys(categories),
            datasets: [{
                label: 'Trends',
                data: Object.values(categories),
                backgroundColor: [
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(201, 203, 207, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 99, 132, 0.2)'
                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(201, 203, 207, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(255, 99, 132, 1)'
                ],
                borderWidth: 1
            }]
        };

        const config = {
            type: 'bar',
            data: data,
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            },
        };

        const trendsChart = new Chart(
            document.getElementById('trendsChart'),
            config
        );
    } else {
        alert('Failed to fetch trends data');
    }
});
