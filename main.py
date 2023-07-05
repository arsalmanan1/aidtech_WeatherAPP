import requests
import json

API_KEY = '11ddcb5d64bafeca3c1a791f99858029'

def fetch_weather_data(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}'
    response = requests.get(url)
    data = json.loads(response.text)
    return data

def parse_weather_data(data):
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    return temperature, humidity, description

def display_weather_data(location, temperature, humidity, description):
    print(f'Weather in {location}:')
    print(f'Temperature: {temperature}°C')
    print(f'Humidity: {humidity}%')
    print(f'Description: {description}')

while True:
        location = input("Enter a location (or 'quit' to exit): ")
        if location.lower() == 'quit':
            break
        data = fetch_weather_data(location)
        if data['cod'] == '404':
            print('Location not found. Please try again.')
            continue

        temperature, humidity, description = parse_weather_data(data)
        display_weather_data(location, temperature, humidity, description)
        print()
