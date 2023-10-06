// declare a varaible that get an element by id.
const element = document.getElementById("add_item");
// declare a varaible that select the class we gonna use.
const parentElement = document.querySelector(".my_list");
// declare a cinstant varaible that create an element in specific class.
const newElements = document.createElement("li");
// this method will work when the user click on the "add_item(id)".
element.addEventListener("click", function() {
    // the method adds the "Item" to the "newElement".
   newElements.textContent = "Item";
   parentElement.appendChild(newElements);
});
