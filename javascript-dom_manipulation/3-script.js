// switching between classes.

// declare a constant varaible that get an elements by id.
const element = document.getElementById("toggle_header");
// declare a constant varaible that select an elements.
const elements = document.querySelector("header");
// this method will work when the user click on the "toggle_header(id)".
element.addEventListener("click", function() {
    // check if the header element(elements) currently has the "red" class. If it does, we remove the "red" class and add the "green" class.
    if (elements.classList.contains("red")){
    elements.classList.remove("red");
    elements.classList.add("green");
    }
    else {
        // If it doesn't have the "red" class, we remove the "green" class and add the "red" class.
        elements.classList.remove("green");
        elements.classList.add("red");
    }
});
