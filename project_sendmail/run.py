import csv
import smtplib
import time
import schedule

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
			
			mail_utils.check_mobileno(d['phone'])
			bool_val = mail_utils.check_email(d['email'])

			current_dt,current_mn,current_yr = mail_utils.current_time()
			
			# checking all the conditions and if scheduled date equal to current then send mail.
			
			'''
			if (bool_val) and (message != dup_msg) and (country.upper() in ['USA','INDIA']) and  \
				(scheduled_dt==current_dt) and (scheduled_mn==current_mn) and (scheduled_yr==current_yr):  
			'''
			if (bool_val) and (message != dup_msg) and (country.upper() in ['USA','INDIA']):
				
				#with smtplib.SMTP('localhost', 1025) as smtp:
				with smtplib.SMTP('smtp.gmail.com', 587) as smtp:        
					
					
					smtp.ehlo()      # initating communication to server by passing hello
					smtp.starttls()  # encrypt the traffic
					smtp.ehlo()      # after encryption we need to rerun ehlo

					smtp.login(mail_utils.sender_mail, mail_utils.password)
   
					smtp.sendmail(mail_utils.sender_mail, d['email'],d['message'])
					
					print("email sent to %s..."% d['email'])
			
			dup_msg = message
	
	print("Sent...")


# schedule.every().day.at("10:30").do(main)
# while True:
# 	schedule.run_pending()	
# 	time.sleep(1)


main()
