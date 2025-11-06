# Import the requests library to make HTTP API calls
import requests

# Set the city we want to get weather information for
city = "Minneapolis"

# Build the API URL with the city name and API key
url = f"http://api.weatherapi.com/v1/current.json?key=0c8efd9c56274e2480660908250611&q={city}&aqi=no"  

# Make a GET request to the weather API
response = requests.get(url)

# Convert the API response from JSON format to a Python dictionary
weather_json = response.json()  

# Extract the current temperature in Fahrenheit from the response
temp = weather_json.get("current").get("temp_f")

# Extract the weather condition description (e.g., "Sunny", "Cloudy")
description = weather_json.get("current").get("condition").get("text")

# Print the weather information in a readable format
print("Today's weather in", city, "is", description, "and", temp, "degrees")