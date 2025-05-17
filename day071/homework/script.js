const jr1Title = document.querySelector('.jr1-title');
const jr2Title = document.querySelector('.jr2-title');
const jr3Title = document.querySelector('.jr3-title');
const textTtile = document.querySelector('.text-title');

const jr1Text = document.querySelector('.jr1-text');
const jr2Text = document.querySelector('.jr2-text');
const jr3Text = document.querySelector('.jr3-text');
const jr4Text = document.querySelector('.jr4-text');

let jr1Couter = true;
let jr2Couter = true;
let jr3Couter = true;
let jr4Couter = true;

const im1 = document.querySelector('.im1');
const im2 = document.querySelector('.im2');
const im3 = document.querySelector('.im3');
const im4 = document.querySelector('.im4');

jr1Title.addEventListener('click', () => {
    if (jr1Couter) {
    jr1Text.style.display = 'block';
    jr2Text.style.display = 'none';
    jr3Text.style.display = 'none';
    jr4Text.style.display = 'none';
    im2.src = './images/icon-minus.svg';

    jr1Couter = false;
    }
    else {
        jr1Text.style.display = 'none';
        jr1Couter = true;
        im2.src = './images/icon-plus.svg';
    }
});

jr2Title.addEventListener('click', () => {
    if (jr2Couter) {
        jr1Text.style.display = 'none';
        jr2Text.style.display = 'block';
        jr3Text.style.display = 'none';
        jr4Text.style.display = 'none';
    
        jr2Couter = false;
        im3.src = './images/icon-minus.svg';
        }
        else {
            jr2Text.style.display = 'none';
            jr2Couter = true;
            im3.src = './images/icon-plus.svg';
        }
});

jr3Title.addEventListener('click', () => {
    if (jr3Couter) {
        jr1Text.style.display = 'none';
        jr2Text.style.display = 'none';
        jr3Text.style.display = 'block';
        jr4Text.style.display = 'none';
    
        jr3Couter = false;
        im4.src = './images/icon-minus.svg';
        }
        else {
            jr3Text.style.display = 'none';
            jr3Couter = true;
            im4.src = './images/icon-plus.svg';
        }
});

textTtile.addEventListener('click', () => {
    if (jr4Couter) {
        jr1Text.style.display = 'none';
        jr2Text.style.display = 'none';
        jr3Text.style.display = 'none';
        jr4Text.style.display = 'block';

    
        jr4Couter = false;
        im1.src = './images/icon-minus.svg';
        }
        else {
            jr4Text.style.display = 'none';
            jr4Couter = true;
            im1.src = './images/icon-plus.svg';
        }
});