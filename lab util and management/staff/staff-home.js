document.getElementById("button1").addEventListener("click", function(){
    animateButton(this);
    setTimeout(() => window.location.href = "staff-add.html", 300);
});

document.getElementById("button2").addEventListener("click", function(){
    animateButton(this);
    setTimeout(() => window.location.href = "staff-view.html", 300);
});

function animateButton(button) {
    button.style.transform = "scale(0.95)";
    setTimeout(() => button.style.transform = "scale(1)", 150);
}
