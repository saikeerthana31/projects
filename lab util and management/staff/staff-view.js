document.addEventListener("DOMContentLoaded", function () {
    let deleteButtons = document.querySelectorAll(".delete");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function () {
            let box = this.closest(".boxes");
            box.style.animation = "fadeOut 0.4s ease-out forwards";
            
            setTimeout(() => {
                box.remove();
            }, 400); // Remove after animation completes
        });
    });
});
