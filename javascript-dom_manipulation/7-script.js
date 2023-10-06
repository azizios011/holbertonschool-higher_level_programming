// declare an constant varaible to store the URL.
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
// declare an constant varaible that get elements by id the HTML tag.
const element = document.getElementById("list_movies");
// send a request to the web_srever(the URL).
fetch(url)
// check if the response from the web_server(the URL) is ok or not. 
  .then(Response => {
    if (!Response.ok) {
      // if not the response ok then will raise an erorr.
      throw new Error('Network response was not ok');
    }
    // if the response is ok then will return with the data(json file).
    return Response.json();
  })
  .then(data => {
    // declare a constant varaible to store the results of the data.
    const films = data.results;
    // this will give the films one by one.
    films.forEach(film => {
      // this will take the title of every film.
      const title = film.title;
      // declare an constant varaible that create an elements (li) in the (ul) tags.
      const list_item = document.createElement('li');
      // this will fill every (li) elements with the title of every film.
      list_item.textContent = title;
      // // we finally  displayed it in the  HTML tag with id 'list_movies'.
      element.appendChild(list_item);
    });
  })
  .catch(error => {
    // this '.catch' function will check if the request of the fetch delivered to the web_server(the URL); 
    console.error('Fetch error:', error);
  });
