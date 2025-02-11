document.addEventListener("DOMContentLoaded", function () {
    const confirmBtn = document.getElementById("confirm");
    const deleteBtn = document.getElementById("delete");

    confirmBtn.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent form submission

        const startTime = document.getElementById("startTime").value;
        const endTime = document.getElementById("endTime").value;
        const labDate = document.getElementById("labDate").value;
        const studentCount = document.getElementById("studentCount").value;
        const labType = document.getElementById("labType").value;

        if (!startTime || !endTime || !labDate || !studentCount || !labType) {
            alert("Please fill in all the details before confirming the booking.");
            return;
        }

        alert("Lab has been successfully booked!");
        location.reload(); // Refresh the page
    });

    deleteBtn.addEventListener("click", function () {
        location.reload(); // Refresh the page on delete
    });
});
