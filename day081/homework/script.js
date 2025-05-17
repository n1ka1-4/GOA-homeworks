const adminAccount = { username: "admin", password: "123456789", role: "admin" };

if (localStorage.getItem("users").length === 0) {
    const users = [adminAccount];
    localStorage.setItem("users", JSON.stringify(users));
}

function registerUser() {
    const username = document.getElementById("regUsername").value;
    const password = document.getElementById("regPassword").value;

    if (!username || !password) {
        alert("please fill in all fields");
        return;
    }

    const users = JSON.parse(localStorage.getItem("users"));
    const newUser = { username, password, role: "user" };
    users.push(newUser);
    localStorage.setItem("users", JSON.stringify(users));
    alert("registration successful!");
}

function loginUser() {
    const username = document.getElementById("loginUsername").value;
    const password = document.getElementById("loginPassword").value;

    const users = JSON.parse(localStorage.getItem("users"));
    const user = users.find(
        (u) => u.username === username && u.password === password
    );

    if (user) {
        displayUserData(user);
        if (user.role === "admin") {
            showAdminPanel();
        }
    } else {
        alert("invalid username or password");
    }
}

function displayUserData(user) {
    const userDetailsDiv = document.getElementById("userDetails");
    userDetailsDiv.innerHTML = `<h3>user details</h3>
                                  <p>name: ${user.username}</p>
                                  <p>role: ${user.role}</p>`;
}

function showAdminPanel() {
    const users = JSON.parse(localStorage.getItem("users"));
    let userList = "<h3>all users:</h3>";
    users.forEach((user, index) => {
        if (user.role !== "admin") {
            userList += `<div>
                        <p>${user.username}</p>
                        <button onclick="deleteUser(${index})">delete</button>
                      </div>`;
        }
    });
    document.getElementById("adminPanel").innerHTML = userList;
}

function deleteUser(index) {
    const users = JSON.parse(localStorage.getItem("users"));
    users.splice(index, 1);
    localStorage.setItem("users", JSON.stringify(users));
    showAdminPanel();
    alert("user deleted!");
}
