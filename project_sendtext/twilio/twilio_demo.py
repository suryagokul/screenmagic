from twilio.rest import Client

#importing credentials from created file
from twilio_keys import account_sid, auth_token,mobile_no


# paste account sid and auth token
client = Client(account_sid, auth_token)

client.messages.create(to=mobile_no, 
                       from_="+17606153242", 
                       body="Hello from Python!")
