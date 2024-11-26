#!/usr/bin/env python3
from flask import Flask, request, render_template
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def home():
    # Get city from query parameters, default to 'London'
    city = request.args.get("city", "London")
    
    # Get the weather data for the specified city
    weather_data = get_weather(city)
    
    # Render the template with the weather data and city
    return render_template("index.html", weather=weather_data, city=city)

def get_weather(city):
    # OpenWeatherMap API URL with the city and API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    # Send GET request to OpenWeatherMap API
    response = requests.get(url)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()  # Return the weather data as JSON
    else:
        return None  # Return None if there's an error in fetching weather data

if __name__ == "__main__":
    # Change the host to '0.0.0.0' to make it accessible from any IP address
    app.run(debug=True, host="0.0.0.0", port=5000)

