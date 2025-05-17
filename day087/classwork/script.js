const form = document.querySelector('.form');

form.addEventListener('submit', function (e) {
    e.preventDefault();
    const username = document.querySelector('#username').value;
    const email = document.querySelector('#email').value;
    const number = document.querySelector('#number').value;

    localStorage.setItem(`person${localStorage.length + 1}`, JSON.stringify({username, email, number}));
});