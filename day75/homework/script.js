const smile = document.getElementById('smile');

let x = 0;
let y = 0;
const speed = 10;

document.addEventListener('keydown', event => {
    smile.textContent = "😩"
    smile.style.backgroundColor = 'rgb(255, 68, 0)';
});

document.addEventListener('keyup', event => {
    smile.textContent = '😁'
    smile.style.backgroundColor = '#00a6bc';
});

document.addEventListener('keydown', event => {

    event.preventDefault();

    switch (event.key) {
        case 'ArrowRight':
            x += speed;
            break;
        case 'ArrowLeft':
            x -= speed;
            break;
        case 'ArrowDown':
            y += speed;
            break;
        case 'ArrowUp':
            y -= speed;
            break;
    }
    smile.style.top = `${y}px`;
    smile.style.left = `${x}px`;
});

    