function login() {
    let username = document.querySelector(".box[type='text']").value;
    let password = document.querySelector(".box[type='password']").value;

    if (username && password) {
        window.location.href = "staff-homeo.html"; // Redirect to home page
    } else {
        alert("Please enter both username and password.");
    }
}

function forgotPassword() {
    alert("Redirecting to password recovery...");
}
