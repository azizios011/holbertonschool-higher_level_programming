// declare a constant varaible that get an element by id.
const element = document.getElementById("update_header");
// declare a constant varaible that select an elements.
const elements = document.querySelector("header");
// this will work when the user click on the "update_header(id)".
element.addEventListener("click", function() {
    // Update the text inside the elements.
    elements.textContent = 'New Header!!!';
});
