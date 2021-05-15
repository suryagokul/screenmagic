from twilio.rest import Client

'''
create twilio_keys file in same directory. 
	
	In that file type below line & replace values with ur api keys. 
	
		account_sid, auth_token, mobile_no = "urid", "urtoken", "receiverno"

'''

#importing credentials from created file
from twilio_keys import account_sid, auth_token,mobile_no


# paste account sid and auth token
client = Client(account_sid, auth_token)

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number

client.messages.create(to=mobile_no, 
                       from_="+17606153242", 
                       body="Hello from Python!")