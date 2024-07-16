// src/views/static/js/login.js
async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    });

    if (response.ok) {
        const data = await response.json();
        localStorage.setItem('jwtToken', data.access_token);
        window.location.href = '/home/input';
    } else {
        alert('Login failed');
    }
}
