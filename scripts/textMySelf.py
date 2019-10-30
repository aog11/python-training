# Chapter 16
# Just Text Me Module Project

#! python3

# Importing the needed modules
from twilio.rest import Client

# Preset values
accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber =  '+1xxxxxxxxxx'
twilioNumber = '+1xxxxxxxxxx'

def textmyself(message):
    twilioCli = Client(accountSID,authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)