# app.py
import flask 
from flask import Flask, jsonify, request, render_template
import requests
from dotenv import load_dotenv
import os

load_dotenv() #load environment variables from .env

# access noaa api token
NOAA_API_BASE = "https://api.weather.gov"
NOAA_API_TOKEN = os.getenv("NOAA_API_TOKEN")


app = flask.Flask(__name__)

# Route for the home page
@app.route("/")
@app.route("/index")
def index():
    """The main page of the application"""
    return flask.render_template("index.html")

# route for about page
@app.route("/about")
def about():
    return flask.render_template("about.html")

#route for trip page
@app.route("/trip")
def trip():
    return flask.render_template("trip.html")

#route for daytrip page
@app.route("/daytrip")
def daytrip():
    return flask.render_template("daytrip.html")


@app.route("/forecast", methods = ['GET'])
def forecast():
     # Example coordinates (fixed for now)
    lat = request.args.get('lat', default="43.978434", type=str)
    lon = request.args.get('lon', default="-121.688328", type=str)
    points_url = f"{NOAA_API_BASE}/points/{lat},{lon}"
    headers = {"User-Agent": "YourAppName", "token": NOAA_API_TOKEN}

    try:
        # First request to get forecast endpoint
        points_response = requests.get(points_url, headers=headers)
        points_response.raise_for_status()
        points_data = points_response.json()

        # Extract forecast URL
        forecast_url = points_data["properties"]["forecast"]
        
        # Second request to retrieve forecast data
        forecast_response = requests.get(forecast_url, headers=headers)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()["properties"]["periods"]

    except requests.exceptions.RequestException as e:
        print("Error fetching weather data:", e)
        return jsonify({"error": "Unable to fetch weather data"}), 500
    except KeyError:
        print("Error parsing data from NOAA API.")
        return jsonify({"error": "Data format error"}), 500
    
    # Render template with forecast data
    return render_template("weather.html", forecast_data=forecast_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)