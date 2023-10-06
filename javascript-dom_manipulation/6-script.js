// declare an constant varaible to store the URL.
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
// declare an constant varaible that get elements by id the HTML tag.
const characterElement = document.getElementById("character");
// send a request to the web_srever(the URL).
fetch(url)
// check if the response from the web_server(the URL) is ok or not. 
  .then(response => {
    if (!response.ok) {
        // if not the response ok then will raise an erorr.
      throw new Error('Network response was not ok');
    }
    // if the response is ok then will return with the data(json file).
    return response.json();
  })
  .then(data => {
    // declare an constant varaible to tell to the web_server(the URL) to put the specified data(name);
    const characterName = data.name;
    // we finally  displayed it in the  HTML tag with id 'character'.
    characterElement.textContent = `Character Name: ${characterName}`;
  })
  .catch(error => {
    // this '.catch' function will check if the request of the fetch delivered to the web_server(the URL); 
    console.error('Fetch error:', error);
  });
