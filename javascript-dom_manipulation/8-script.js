// Function to fetch and display the translation.
function fetchAndDisplayTranslation() {
// declare an constant varaible to store the URL.
const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
// declare an constant varaible that get elements by id the HTML tag.
const elments = document.getElementById("hello");
// send a request to the web_srever(the URL).
fetch(url)
// check if the response from the web_server(the URL) is ok or not. 
    .then(response => {
        // if not the response ok then will raise an erorr.
        if (!response.ok) {
            throw new Erorr("Network response was not ok");
        }
        // if the response is ok then will return with the data(json file).
        return response.json();
    })
    .then(data => {
        // declare a constant varaible to search for sepecific data and store it.
        const value = data.hello;
        // this will display it in the HTML tag (<head>).
        elments.textContent = value;
    })
    .catch(erorr => {
        // this '.catch' function will check if the request of the fetch delivered to the web_server(the URL);
        console.error('Fetch erorr:', erorr)
    });
}
    // this will watch the fetchAndDisplayTranslation function on complete it's work at the rigth time/without problems.
    document.addEventListener('DOMContentLoaded', fetchAndDisplayTranslation);
