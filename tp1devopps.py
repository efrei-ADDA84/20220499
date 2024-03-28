import os
import requests

def get_weather(latitude, longitude, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return None

def main():
    latitude = os.environ.get("LAT")
    longitude = os.environ.get("LONG")
    api_key = os.environ.get("API_KEY")

    if not all([latitude, longitude, api_key]):
        print("Veuillez fournir les valeurs de LAT, LONG et API_KEY dans les variables d'environnement.")
        return

    weather_data = get_weather(latitude, longitude, api_key)
    if weather_data:
        print("Météo actuelle:")
        print(f"Température: {weather_data['main']['temp']} °C")
        print(f"Conditions météorologiques: {weather_data['weather'][0]['description']}")
    else:
        print("Échec de la récupération des données météorologiques.")

if __name__ == "__main__":
    main()
