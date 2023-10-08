document.addEventListener('DOMContentLoaded', function () {
    // Select relevant DOM elements
    const languageSelect = document.getElementById("language_code");
    const translateButton = document.getElementById("btn_translate");
    const helloElement = document.getElementById("hello");

    function fetchAndDisplayTranslation() {
        // Function to fetch and display the translation
        const selectedLanguage = languageSelect.value;
        if (!selectedLanguage) {
          helloElement.textContent = "Please choose a language";
          return;
        }
    
        const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${selectedLanguage}`;

        fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            return response.json();
          })
          .then(data => {
            const translation = data.hello;
            helloElement.textContent = translation;
          })
          .catch(error => {
            console.error('Fetch error:', error);
            helloElement.textContent = "Translation not available";
          });
    }

        // Add click event listener to the Translate button   
        translateButton.addEventListener("click", fetchAndDisplayTranslation);
});
