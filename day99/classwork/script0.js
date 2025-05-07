const number = document.querySelector(".number");
const mm = document.querySelector(".mm");
const yy = document.querySelector(".yy");
const cvc = document.querySelector(".cvc");
const error1 = document.querySelector(".error1");
const error2 = document.querySelector(".error2");
const error3 = document.querySelector(".error3");
const submit = document.querySelector(".btn");

// პითონის ფუნქცია, რომელიც აბრუნებს True თუ str შეიცავს მხოლოდ ციფრებს ეგ დავადეკლალირე
function isdigit(str) {
    return (
        str.length > 0 && [...str].every((char) => char >= "0" && char <= "9")
    );
}

// ვალიდაციის ფუნქცია, რომელიც აბრუნებს True თუ str შეიცავს მხოლოდ ციფრებს თუ არა და ერორს
number.addEventListener("input", function () {
    if (!isdigit(number.value)) {
        number.style.outline = "2px solid hsl(0, 100%, 66%)";
        error1.style.display = "block";
    } else {
        number.style.outline = "";
        error1.style.display = "none";
    }
    if (number.value.length === 0) {
        number.style.outline = "";
        error1.style.display = "none";
    }

    if (number.value.length > 16) {
        number.value = number.value.slice(0, 16);
    }
});

// ვალიდაციის ფუნქცია, რომელიც აბრუნებს True თუ str შეიცავს რაიმეს (არ არის ცარიელი) თუ არა და ერორს
mm.addEventListener("input", function () {
    if (mm.value.length === 0 || yy.value.length === 0) {
        mm.style.outline = "2px solid hsl(0, 100%, 66%)";
        error2.style.display = "block";
    } else {
        mm.style.outline = "";
        yy.style.outline = "";
        error2.style.display = "none";
    }
});

// ვალიდაციის ფუნქცია, რომელიც აბრუნებს True თუ str შეიცავს რაიმეს (არ არის ცარიელი) თუ არა და ერორს
yy.addEventListener("input", function () {
    if (mm.value.length === 0 || yy.value.length === 0) {
        yy.style.outline = "2px solid hsl(0, 100%, 66%)";
        error2.style.display = "block";
    } else {
        mm.style.outline = "";
        yy.style.outline = "";
        error2.style.display = "none";
    }
});

// ვალიდაციის ფუნქცია, რომელიც აბრუნებს True თუ str შეიცავს რაიმეს (არ არის ცარიელი) თუ არა და ერორს
cvc.addEventListener("input", function () {
    if (cvc.value.length === 0) {
        cvc.style.outline = "2px solid hsl(0, 100%, 66%)";
        error3.style.display = "block";
    } else {
        cvc.style.outline = "";
        error3.style.display = "none";
    }
});

// როცა არ არის ერორები და ყველაფერი არის შევსებული მარტო მაშინ ცვლის. შეცვლა ხდება ერთი ფრაიმს ვაქრობ და მეორეს ვაჩვენებ
submit.addEventListener("click", function (e) {
    e.preventDefault();
    if (
        error1.style.display !== "block" &&
        error2.style.display !== "block" &&
        error3.style.display !== "block" &&
        number.value.length !== 0 &&
        mm.value.length !== 0 &&
        yy.value.length !== 0 &&
        cvc.value.length !== 0
    ) {
        document.querySelector(".right").classList.toggle("hidden");
        document.querySelector(".after-right").classList.remove("hidden");
    }
});
