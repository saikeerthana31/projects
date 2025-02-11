document.addEventListener("DOMContentLoaded", function() {
    const requests = document.querySelectorAll(".boxreqs, .boxreqs2, .boxreqs3, .boxreqs4");

    requests.forEach((request) => {
        const cancelBtn = request.querySelector("#cancel");
        const okayBtn = request.querySelector("#okay");

        // Approve Request
        okayBtn.addEventListener("click", function() {
            request.style.backgroundColor = "green";
            request.style.opacity = "0.5";
            setTimeout(() => request.remove(), 800);
        });

        // Cancel Request
        cancelBtn.addEventListener("click", function() {
            request.style.backgroundColor = "red";
            request.style.opacity = "0.5";
            setTimeout(() => request.remove(), 800);
        });
    });
});
