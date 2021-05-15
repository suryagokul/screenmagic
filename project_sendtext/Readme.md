steps : 	

	pip install -r requirements.txt

	login to twilio.com account and 
	
	then goto console. 
	
	click on get trail number and copy that number.

	paste it to the from_ in the 50th line in run_main code..

	from twilio console copy Twilio Account SID and Auth Token.
	
	create twilio_keys file in this directory.I haven't uplodaed here because not to expose my api keys.

	In that file type below line & replace values with ur api keys. 

		account_sid, auth_token, mobile_no = "urid", "urtoken", "receiverno"

	change the "to" number to the phone number you signed up for Twilio with,

	or upgrade your account to send SMS to any phone number

	open cmd where this file exists and type

		python run_main.py
