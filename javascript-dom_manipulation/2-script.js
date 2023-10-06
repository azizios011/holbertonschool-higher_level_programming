// get the element by it's id and select an element 
const element = document.getElementById("red_header");
const elements = document.querySelector("header");
// add it a class red when the user click on the tag(id) red_heder
element.addEventListener("click", function() {
    elements.classList.add("red")
});
