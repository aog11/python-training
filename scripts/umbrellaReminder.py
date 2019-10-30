# Chapter 16
# Umbrella Reminder Project

#! python3

# Importing the needed modules
import requests, bs4
from twilio.rest import Client

# Twilio client information
def sendWeather():
    accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxx'
    authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    myTwilioNumber = '+1xxxxxxxxxx'
    myNumber = '+1xxxxxxxxxx'
    twilioCli = Client(accountSID,authToken)
    message = 'Please take an umbrella today!'
    twilioCli.messages.create(body=message,from_=myTwilioNumber,to=myNumber)

# Checking the weather
weatherURL = 'https://www.bbc.com/weather/3492908'
res = requests.get(weatherURL)
weatherData = bs4.BeautifulSoup(res.text)
currData = weatherData.select('.wr-day__weather-type-description.wr-js-day-content-weather-type-description.wr-day__content__weather-type-description--opaque')[0].getText()

# Notifying in case of clouds or rain
if 'rain' in currData.lower() or 'cloud' in currData.lower():
    sendWeather()