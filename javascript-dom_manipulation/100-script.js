document.addEventListener('DOMContentLoaded', function() {
    // Select relevant DOM elements
    const addItemButton = document.getElementById("add_item");
    const removeItemButton = document.getElementById("remove_item");
    const clearListButton = document.getElementById("clear_list");
    const myList = document.querySelector(".my_list");

    function addItem() {
        // Function to add a new <li> element to the list
        const newItem = document.createElement("li");
        newItem.textContent = "Item";
        myList.appendChild(newItem);
    }
    function removeItem() {
        // Function to remove the last <li> element from the list
        const lastItem = myList.lastElementChild;
        if (lastItem) {
          myList.removeChild(lastItem);
        }
    }
    function clearList() {
        // Function to clear all <li> elements from the list.
        myList.innerHTML = "";
        // Removes all children elements
    }

    // Add click event listeners
    addItemButton.addEventListener("click", addItem);
    removeItemButton.addEventListener("click", removeItem);
    clearListButton.addEventListener("click", clearList);
});
