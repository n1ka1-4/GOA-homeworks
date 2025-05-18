const container = document.querySelector(".container");
const button = document.querySelector(".decoration");
fetch("https://api.adviceslip.com/advice")
    .then((res) => res.json())
    .then((json) => {
        container.innerHTML = `
            <p>Advice #${json.slip.id}</p>
            <p>"${json.slip.advice}"</p>
            <img src="images/pattern-divider-desktop.svg" class="divider"/>`;
    });

button.addEventListener("click", () => {
    fetch("https://api.adviceslip.com/advice")
        .then((res) => res.json())
        .then((json) => {
            container.innerHTML = `
                <p>Advice #${json.slip.id}</p>
                <p>"${json.slip.advice}"</p>
                <img src="images/pattern-divider-desktop.svg" class="divider"/>`;
        });
});


