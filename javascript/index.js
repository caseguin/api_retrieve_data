
const api_key = 'api_key';

function getWeather() {
    const cityInput  = document.getElementById('city').value;

    if (!city) {
        alert('Please enter a city');
        return;
    }

    const current_weather_url = `https://api.openweathermap.org/data/2.5/weather?q=${cityInput}&appid=${api_key}`;
    const forecast_weather_url = `https://api.openweathermap.org/data/2.5/forecast?q=${cityInput}&appid=${api_key}`;

    fetchWeatherData(current_weather_url)
}


function fetchWeatherData(url) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('City not found or network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Current weather data:', data);
            displayWeather(data);
        })
        .catch(error => {
            console.error('There was a problem fetching the current weather:', error);
        });
}

function displayWeather(data) {
    try {
    const city = data.name
    const temperature = Math.round(data.main.temp - 273.15);
    const weather = data.weather[0].description;
    const iconCode = data.weather[0].icon;
    const iconUrl = `https://openweathermap.org/img/wn/${iconCode}@2x.png`;
    
    const cityElement = document.getElementById('city-div')
    const temperatureElement = document.getElementById('temp-div');
    const weatherElement = document.getElementById('weather-info');
    const iconElement = document.getElementById('weather-icon');

    cityElement.textContent = `${city}`;
    temperatureElement.textContent = `${temperature}°C`;
    weatherElement.textContent = `${weather}`
    iconElement.src = iconUrl;
    iconElement.alt = weather;
    iconElement.style.display = 'block';

    } catch (error) {
        console.error('Erreur displaying weather: ', error);
    }
}