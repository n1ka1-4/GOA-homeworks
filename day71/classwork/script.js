// 1
let pText = document.getElementsByClassName('txt');

// 2
let H1 = document.querySelector('#h1');
let H2 = document.querySelector('.h1');

// 3
let img = document.getElementById('img');

img.src = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png';
img.style.width = '100px';

// 4
let p = document.getElementById('p');

p.style.color = 'red';
p.style.fontSize = '20px';
p.style.backgroundColor = 'yellow';

// 5
let p1 = document.createElement('p');
let txTN = document.createTextNode('This is a new paragraph');
let div = document.getElementById('div');

p1.appendChild(txTN);
div.appendChild(p1);