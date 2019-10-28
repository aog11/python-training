# Chapter 14
# Fetching Current Weather Data Project

#! python3

# Importing the needed modules
import sys, requests, json

# Compute location for command line arguments
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API
apiKey = '' # You now need an API key
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&&appid=%s' % (location,apiKey)
res =  requests.get(url)
res.raise_for_status()

# Load JSON data into a Python variable
weatherData = json.loads(res.text)

# Print weather descriptions
w = weatherData['list']
print('Current weather in %s:'%(location))
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'],end='\n\n')
print('Tomorrow:')
print(w[1]['weather'][1]['main'],'-',w[1]['weather'][1]['description'],end='\n\n')
print('Day after tomorrow:')
print(w[2]['weather'][2]['main'],'-',w[2]['weather'][2]['description'])