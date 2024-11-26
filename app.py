#!/usr/bin/env python3
from flask import Flask, request, render_template
import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    # Get city from query parameters, default to 'New York'
    city = request.args.get("city", "New York")
    weather_data = get_weather(city)
    return render_template("index.html", weather=weather_data, city=city)

def get_weather(city):
    # OpenWeatherMap API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # Return JSON response
    return None  # Return None if request fails

if __name__ == "__main__":
    app.run(debug=True)
