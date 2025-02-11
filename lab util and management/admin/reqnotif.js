const notifBoxes = document.querySelectorAll("#notif1, #notif2, #notif3, #notif4");

notifBoxes.forEach(box => {
    box.addEventListener("click", () => handleTouch(box)); // Handle click
    box.addEventListener("touchstart", () => handleTouch(box)); // Handle touch on mobile
});

function handleTouch(box) {
    box.classList.add("swipe-out");
    setTimeout(() => {
        box.style.display = "none";  // Remove the box after animation
    }, 500);  // Wait for the animation to finish (0.5s)
}
