document.addEventListener("DOMContentLoaded", function () {

    // ADD ITEM
    const addBtn = document.getElementById("add_btn");
    const inputBox = document.querySelector("input[name='item_input']");

    if (addBtn) {
        addBtn.addEventListener("click", function (event) {

            if (inputBox.value.trim() === "") {
                alert("Item name cannot be empty!");
                event.preventDefault();
            } else {
                alert("Item added successfully!");
            }

        });
    }


    // DELETE ITEM
    const deleteButtons = document.querySelectorAll(".del-btn");

    deleteButtons.forEach(function (button) {
        button.addEventListener("click", function () {

            const itemId = this.getAttribute("data-id");

            if (confirm("Are you sure you want to delete this item?")) {

                fetch("/home/delete/" + itemId, {
                    method: "DELETE"
                })
                .then(function (response) {
                    return response.json();
                })
                .then(function (data) {
                    alert(data.message);
                    location.reload();
                })
                .catch(function () {
                    alert("Something went wrong!");
                });

            }

        });
    });


    // EDIT ITEM
    const editButtons = document.querySelectorAll(".edit-btn");

    editButtons.forEach(function (button) {
        button.addEventListener("click", function () {

            const itemId = this.getAttribute("data-id");
            window.location.href = "/home/edit/" + itemId;

        });
    });

});

