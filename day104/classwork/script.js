const cont = document.querySelector(".container");

fetch("https://fakestoreapi.com/products")
    .then((res) => res.json())
    .then((json) => {
        json.forEach((el) => {
            cont.innerHTML += `
                <div>
                    <img src="${el.image}" width=200>
                    <h3>${el.title}</h3>
                    <p>${el.price}</p>
                </div>
            `;
        });
    });
