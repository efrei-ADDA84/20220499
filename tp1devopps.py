from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

def get_weather(latitude, longitude, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data
    else:
        return None

@app.route('/')
def weather():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    api_key = os.environ.get('API_KEY')

    if not all([latitude, longitude, api_key]):
        return jsonify({'error': 'Missing parameters'}), 400

    weather_data = get_weather(latitude, longitude, api_key)
    if weather_data:
        return jsonify({
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description']
        }), 200
    else:
        return jsonify({'error': 'Failed to fetch weather data'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
