// if we have p tag and inside b tag and p has class parent and b has class child and if we add eventlistener on p tag thats gives as i'm parent in console and if we add eventlistener on b tag thats gives as i'm child in console we see that in console when we click b tag we get 1) i am child 2) i am parent this is bubbling phase and when we click p tag we get 1) i am parent 2) i am child this is capturing phase we can adjust this by using True or False method after function in p tag event listener and b tag eventlistener true means capturing phase and false means bubbling phase
// let see this in action: 

let parent1 = document.querySelector('.parent');
let child1 = document.querySelector('.child');

parent1.addEventListener('click', function(){
    console.log('i am parent');
}, true);
child1.addEventListener('click', function(){
    console.log('i am child');
});