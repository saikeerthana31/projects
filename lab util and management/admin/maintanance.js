document.getElementById('subbutton').addEventListener('click', function() {
    if (confirm('Are you sure you want to submit this request?')) {
        alert('Your maintenance request has been submitted successfully!');
        setTimeout(() => {
            location.reload(); // Refresh after alert
        }, 500); // Small delay to ensure alert is seen
    } else {
        alert('Submission cancelled.');
    }
});
