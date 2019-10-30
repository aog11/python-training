# Chapter 16
# Sending Text Messages 
# Demostration with Twilio

#! python3

# Importing the needed modules
from twilio.rest import Client

# Account information
accountSID = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Authentication process
twilioCli = Client(accountSID,authToken)

# Sender and receiptient
myTwilioNumber = '+xxxxxxxxxx'
myCellPhone = '+xxxxxxxxxx'

# Sending the message
message = twilioCli.messages.create(body='This is a test. Sent from Python through Twilio', from_=myTwilioNumber, to=myCellPhone)