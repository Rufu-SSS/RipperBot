import os
import requests

def get_weather(city: str) -> str:
    api_key = os.getenv("WEATHER_API_KEY")  # Carregar la clau de l'API des de les variables d'entorn
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Temperatura en graus Celsius
        "lang": "en"  # Idioma en anglès
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:  # Consulta correcta
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        return (
            f"**Weather in {city_name}, {country}:**\n"
            f"- Description: {description.capitalize()}\n"
            f"- Temperature: {temperature}°C\n"
            f"- Humidity: {humidity}%\n"
            f"- Wind speed: {wind_speed} m/s"
        )
    else:  # Error (ciutat no trobada o problema amb l'API)
        error_message = data.get("message", "Unknown error")
        return f"Could not retrieve the weather for {city}. Error: {error_message}"
