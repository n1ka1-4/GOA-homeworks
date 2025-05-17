const box = document.querySelector('.box');
const box1 = document.querySelector('.box1');

let x = 0;
let y = 0;

// 1
const moveRight = setInterval(() => {
    x += 1; 
    box.style.top = `${x}px`;
    if (x == 450){
       clearInterval(moveRight);
       const moveDown = setInterval(() => {
          y += 1; 
          box.style.left = `${y}px`;
          if (y == 450){
             clearInterval(moveDown);
             const moveLeft = setInterval(() => {
                x -= 1; 
                box.style.top = `${x}px`;
                if (x == 0){
                   clearInterval(moveLeft);
                   const moveUp = setInterval(() => {
                      y -= 1; 
                      box.style.left = `${y}px`;
                      if (y == 0){
                         clearInterval(moveUp);
                      }
                   }, 5)
                }
             }, 5)
          }
       }, 5)
    }
 }, 5)

//  2
let left = 0;
let top1 = 0
let direction = "right";

const move = setInterval(function(){
    if(direction == "right"){
        top1++;
        if(top1 == 455){
            direction = "bottom";
        }
    } else if(direction == "bottom"){
        left++;
        if(left == 455){
            direction = "left";
        }
    } else if(direction == "left"){
        top1--;
        if(top1 == 5){
            direction = "top";
        }
    } else{
        left--;
        if(left == 5 && y == 5){
            direction = "right";
        }
    }

    box1.style.left = left + 'px';
    box1.style.top = top1 + 'px';
}, 5);
