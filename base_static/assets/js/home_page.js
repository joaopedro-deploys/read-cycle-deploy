import get_location from "./get_location.js";

async function fetchLocation() { //verify location is available in localstorege, if not, get and set this.
    const storedLocation = localStorage.getItem('user_location');
    if (storedLocation) {
        sendLocation(location);
    }
    else {
        if (navigator.geolocation) {
            const data = await get_location();
            localStorage.setItem('user_location', JSON.stringify(data));
            console.log('Localização armazenada no localStorage:', data);
            sendLocation(data);
        } 
        else {
            console.log('Geolocalização não é suportada neste navegador.');
        }
    }
}

function sendLocation(data) { // send location to home_page and render the html return on template
    const target = document.querySelector('#portfolio-container');
    const csrftoken = document.querySelector('#csrf-token').getAttribute('content');
    fetch(
        '/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify(data)
        }
    )
    .then(response => response.text())
    .then(html => target.innerHTML = html)
    .catch(error => console.log('error no fetch: ', error));
}
fetchLocation();


