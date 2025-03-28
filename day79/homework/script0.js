let listPeople = [];

document.addEventListener("DOMContentLoaded", function () {
    let info = document.querySelector(".info");
    let form = document.querySelector(".form");
    let authorization = document.querySelector(".authorization");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        let name = form.elements.name.value.trim();
        let email = form.elements.email.value.trim();
        let password = form.elements.password.value.trim();

        if (listPeople.length !== 0) {
            listPeople.forEach((person) => {
                if (person.email === email) {
                    alert("Email already exists!");
                } else {
                    writeDetails();
                }
            });
        } else {
            writeDetails();
        }

        function writeDetails() {
            if (name !== "" || email !== "" || password !== "") {
                info.innerHTML = `
                        <p>Name: ${name}</p>
                        <p>Email: ${email}</p>
                        <p>Password: ${password}</p>
                    `;

                form.reset();

                listPeople.push({ name, email, password });
                console.log(listPeople);
            }
        }
    });
    authorization.addEventListener("click", function () {
        let email = form.elements.email.value.trim();
    
        if (listPeople.length === 0) {
            alert("You are not registered!");
        }
        listPeople.forEach((person) => {
            if (person.email == email) {
                alert("You successfully logged in!");
            } else {
                alert("Incorrect email");
            }
        });
    });
});
