const desert = document.querySelector(".sweet");

fetch("data.json")
    .then((res) => res.json())
    .then((res) => {
        res.forEach((el) => {
            desert.innerHTML += `
                <div class="item" style="position: relative;">
                    <div class="add-tcart" style="position: absolute; width: 140px; height: 40px; display: flex; align-items: center; justify-content: center; border:1px solid hsl(14, 25%, 72%); background: white; left: 30px; bottom: 3px; border-radius: 20px; cursor: pointer;">
                        <img src="./assets/images/icon-add-to-cart.svg" style="margin-right: 5px;"/>
                        <p>Add to Cart</p>
                    </div>
                    <img class="desert" src="${el.image.desktop}" alt="${el.name}" style="width: 200px; height: 190px; border-radius: 5px; margin-right: 10px;" />
                    <div class="desert-text">
                        <p class="nikname" style="color: hsl(14, 25%, 72%);">${el.category}</p>
                        <p class="name" style="color: hsl(14, 65%, 9%);">${el.name}</p>
                        <p class="prize" style="color: rgb(255, 153, 127); margin-right: 10px;">$${el.price.toFixed(2)}</p>
                    </div>
                </div>
            `;
        });
    });
