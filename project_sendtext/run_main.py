import csv
import smtplib
import time
import schedule
from twilio.rest import Client
from twilio_keys import account_sid, auth_token,mobile_no


import mail_utils


def main():
	
	print("Loading...")

	d = {}         # dictionary
	dup_msg = ""
	
	with open("Sample.csv",'r') as f:          # reading file
		cr = csv.reader(f, delimiter=',')
		header = next(cr)
		for line in cr:
			message = line[0]
			email   = line[1]
			phone   = line[2] 
			country = line[3]
			Schedule_On = line[4]
			scheduled_dt, scheduled_mn, scheduled_yr = Schedule_On.split('/')
			
			# check whether message is duplicate or not
			if message == dup_msg:
				mail_utils.write_to('messages.txt', 'a','Failure : Duplicate message will not allow..')

				
			d['message'] = message
			d['email'] = email
			d['phone'] = phone
			
			mobile_val = mail_utils.check_mobileno(d['phone'])
			bool_val = mail_utils.check_email(d['email'])

			current_dt,current_mn,current_yr = mail_utils.current_time()
			
			# checking all the conditions and if scheduled date equal to current then send mail.
			
			
			if (mobile_val) and (message != dup_msg) and (country.upper() in ['USA','INDIA']) and (len(message)>1 and len(message)<=160):
			
				client = Client(account_sid, auth_token)
				client.messages.create(to=mobile_no, from_="+17606153242", body="Message is from Python!")
				
						
			dup_msg = message
	
	print("Sent Text Message...")


# schedule.every().day.at("10:30").do(main)
# while True:
# 	schedule.run_pending()	
# 	time.sleep(1)


main()
