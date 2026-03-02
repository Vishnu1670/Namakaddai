document.addEventListener("DOMContentLoaded", function () {

    // ADD ITEM
    const addBtn = document.getElementById("add_btn");
    const inputBox = document.querySelector("input[name='item_input']");

    if (addBtn) {
        addBtn.addEventListener("click", function (event) {

            if (inputBox.value.trim() === "") {// if empty value given
                alert("Item name cannot be empty!");
                event.preventDefault();//stops the default action that the browser would normally do
            } else {
                alert("Item added successfully!");
            }

        });
    }


    // DELETE ITEM
    const deleteButtons = document.querySelectorAll(".del-btn");//select the perticular button in the loop

    deleteButtons.forEach(function (button) { //.forEach() =    loop over each button
        button.addEventListener("click", function () {

            const itemId = this.getAttribute("data-id"); //this.getAttribute("data-id") = get the item_id of the clicked button

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
                    alert("Something went wrong!"); //.catch() → if something goes wrong, alert user
                });

            }

        });
    });


    // EDIT ITEM
    const editButtons = document.querySelectorAll(".edit-btn");//select the perticular button in the loop

    editButtons.forEach(function (button) {
        button.addEventListener("click", function () {

            const itemId = this.getAttribute("data-id");
            window.location.href = "/home/edit/" + itemId;

        });
    });

});

document.addEventListener("DOMContentLoaded", function () {

    const qtyInput = document.getElementById("purchase_qty");
    const rateInput = document.getElementById("purchase_rate");
    const amountInput = document.getElementById("purchase_amount");

    function calculateAmount() {
        const qty = parseFloat(qtyInput.value) || 0;
        const rate = parseFloat(rateInput.value) || 0;
        amountInput.value = qty * rate;
    }

    qtyInput.addEventListener("input", calculateAmount);
    rateInput.addEventListener("input", calculateAmount);

});

document.addEventListener("DOMContentLoaded", function () {

    const salesQtyInput = document.getElementById("sales_qty");
    const salesRateInput = document.getElementById("sales_rate");
    const salesAmountInput = document.getElementById("sales_amount");

    function calculateSalesAmount() {
        const qty = parseFloat(salesQtyInput.value) || 0;
        const rate = parseFloat(salesRateInput.value) || 0;
        salesAmountInput.value = qty * rate;
    }

    salesQtyInput.addEventListener("input", calculateSalesAmount);
    salesRateInput.addEventListener("input", calculateSalesAmount);

});