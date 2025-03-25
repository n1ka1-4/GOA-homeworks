// if we have p tag and inside b tag and p has class parent and b has class child and if we add eventlistener on p tag thats gives as i'm parent in console and if we add eventlistener on b tag thats gives as i'm child in console we see that in console when we click b tag we get 1) i am child 2) i am parent this is bubbling phase and when we click p tag we get 1) i am parent 2) i am child this is capturing phase we can adjust this by using True or False method after function in p tag event listener and b tag eventlistener true means capturing phase and false means bubbling phase


const slides = document.querySelectorAll(".slides img");
let slideIndex = 0;
let intervalId = null;

document.addEventListener("DOMContentLoaded", initializeSlider);

function initializeSlider(){
    if(slides.length > 0){
        slides[slideIndex].classList.add("displaySlide");
        intervalId = setInterval(nextSlide, 5000);
    }
}

function showSlide(index){
    if(index >= slides.length){
        slideIndex = 0;
    }
    else if(index < 0){
        slideIndex = slides.length - 1;
    }

    slides.forEach(slide => {
        slide.classList.remove("displaySlide");
    });
    slides[slideIndex].classList.add("displaySlide");
}

function prevSlide(){
    clearInterval(intervalId);
    slideIndex--;
    showSlide(slideIndex);
}

function nextSlide(){
    slideIndex++;
    showSlide(slideIndex);
}