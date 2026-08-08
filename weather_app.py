# Weather App
import requests

def get_location():
    location = input("Enter a city: ").strip()
    return location

def get_coordinates(location):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
        "name": location
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    if "results" not in data or len(data["results"]) == 0:
        return None

    results = data["results"]

    latitude = results[0]["latitude"]
    longitude = results[0]["longitude"]

    return latitude, longitude

def get_weather(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code",
        "temperature_unit": "fahrenheit"
    }

    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    if "current" not in data:
        return None

    current = data["current"]

    temp = current["temperature_2m"]
    weather_code = current["weather_code"]

    return temp, weather_code

def display_weather(location, temp, weather_code):
    if weather_code == 0:
        condition = "Clear sky"
    elif weather_code == 1:
        condition = "Mainly clear"
    elif weather_code == 2:
        condition = "Partly cloudy"
    elif weather_code == 3:
        condition = "Overcast"
    elif weather_code == 45:
        condition = "Fog"
    elif weather_code == 51:
        condition = "Drizzle: Light"
    elif weather_code == 53:
        condition = "Drizzle: Moderate"
    elif weather_code == 55:
        condition = "Drizzle: Dense"
    elif weather_code == 61:
        condition = "Rain: Slight"
    elif weather_code == 63:
        condition = "Rain: Moderate"
    elif weather_code == 65:
        condition = "Rain: Heavy"
    elif weather_code == 71:
        condition = "Snowfall: Slight"
    elif weather_code == 73:
        condition = "Snowfall: Moderate"
    elif weather_code == 75:
        condition = "Snowfall: Heavy"
    elif weather_code == 95:
        condition = "Thunderstorm"
    else:
        condition = "Unknown"

    print(f"Location: {location}")
    print(f"Temperature: {temp}°F")
    print(f"Condition: {condition}")

def ask_to_continue():
    while True:
        decision = input("Do you want to continue? (yes/no): ").strip().lower()

        if decision == "yes":
            return True
        elif decision == "no":
            return False

        print("Please enter yes or no.")


def main():
    while True:
        location = get_location()

        coordinates = get_coordinates(location)

        if coordinates is None:
            print("Location not found.")
            continue

        latitude, longitude = coordinates

        weather = get_weather(latitude, longitude)

        if weather is None:
            print("Weather data could not be retrieved.")
            continue

        temp, weather_code = weather

        display_weather(location, temp, weather_code)

        if not ask_to_continue():
            print("Goodbye!")
            break

main()
