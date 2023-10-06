// define a constant variable that get element by it's id
const elements = document.getElementById("red_header");
// change the color when the user click on the tag with the id
 elements.addEventListener("click", function() {
    elements.style.color = "#FF0000"
 });
