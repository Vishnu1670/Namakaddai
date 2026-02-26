

document.addEventListener("DOMContentLoaded", function() { //to add item

    const addBtn = document.getElementById("add_btn");

    if (addBtn) {
        addBtn.addEventListener("click", function() {
            alert("Item added successfully!");
        });
    }

});

document.addEventListener("DOMContentLoaded", function () { // to stop user to add empty text

    const addBtn = document.getElementById("add_btn");
    const inputBox = document.querySelector("input[name='item_input']");

    addBtn.addEventListener("click", function (event) {

        if (inputBox.value.trim() === "") {
            alert("Item name cannot be empty!");
            event.preventDefault();  // stop form submission
        }

    });

});

document.addEventListener("DOMContentLoaded", function () { // delete button
 
    const deleteButtons = document.querySelectorAll(".del-btn");

    deleteButtons.forEach(button => {
        button.addEventListener("click", function () {

            const itemId = this.getAttribute("data-id");

            if (confirm("Are you sure you want to delete this item?")) {

                fetch(`/home/delete/${itemId}`, {
                    method: "DELETE"
                })
                .then(response => response.json())
                .then(data => {
                    alert(data.message);
                    location.reload();
                })
                .catch(error => {
                    alert("Something went wrong!");
                });

            }

        });
    });

});