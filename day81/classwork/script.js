document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".form");
    let divInfo = document.querySelector(".info");

    form.addEventListener("submit", (e) => {
        e.preventDefault();
        name = form.elements.name.value.trim();
        email = form.elements.email.value.trim();
        password = form.elements.password.value.trim();
        divInfo.innerHTML = `<p>name: ${name}</p>
                            <p>email: ${email}</p>
                            <p>password: ${password}</p>`;
    });
});