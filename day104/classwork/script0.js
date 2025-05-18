const form = document.querySelector(".form");
const cont = document.querySelector(".container");
const input = form.querySelector("input");

form.addEventListener("submit", (event) => {
    event.preventDefault();
    fetch(
        `https://www.googleapis.com/books/`
    )
        .then((res) => res.json())
        .then((json) => {
            cont.innerHTML = "";
            json.forEach((el) => {
                if (
                    el.title
                        .toLowerCase()
                        .includes(input.value.toLowerCase().trim())
                ) {
                    cont.innerHTML += `
                    <div>
                        <h3>${el.title}</h3>
                        <p>${el.body}</p>
                    </div>
                `;
                }
            });
        });
});
