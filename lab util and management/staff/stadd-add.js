document.addEventListener("DOMContentLoaded", function () {
    const openFormBtn = document.getElementById("openFormBtn");
    const bookingForm = document.getElementById("bookingForm");
    const confirmBtn = document.getElementById("confirmBtn");
    const deleteBtn = document.getElementById("deleteBtn");
    const message = document.getElementById("message");

    // Toggle Form Visibility with Smooth Animation
    openFormBtn.addEventListener("click", function () {
        if (bookingForm.style.opacity === "0" || bookingForm.style.display === "none") {
            bookingForm.style.display = "block";
            setTimeout(() => { bookingForm.style.opacity = "1"; }, 10); // Smooth fade-in
        } else {
            bookingForm.style.opacity = "0";
            setTimeout(() => { bookingForm.style.display = "none"; }, 300); // Smooth fade-out
        }
    });

    // Confirm Booking
    confirmBtn.addEventListener("click", function () {
        const startTime = document.getElementById("startTime").value;
        const endTime = document.getElementById("endTime").value;
        const labDate = document.getElementById("labDate").value;
        const studentCount = Number(document.getElementById("studentCount").value);
        const labType = document.getElementById("labType").value;

        if (startTime && endTime && labDate && studentCount > 0 && labType) {
            message.textContent = "Lab booked successfully!";
            message.style.color = "green";
        } else {
            message.textContent = "Please fill all details.";
            message.style.color = "red";
        }
    });

    // Delete Booking
    deleteBtn.addEventListener("click", function () {
        document.getElementById("startTime").value = "";
        document.getElementById("endTime").value = "";
        document.getElementById("labDate").value = "";
        document.getElementById("studentCount").value = "";
        document.getElementById("labType").value = "";

        message.textContent = "Booking canceled.";
        message.style.color = "orange";
    });
});
