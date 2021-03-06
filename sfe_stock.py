#! /usr/bin/python
#By William Garrido (FriedCircuits.us)
#Upploaded 09-21-2013
#Licensed as CC-BY-SA
#https://github.com/FriedCircuits/Stock_Checker

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json
from urllib2 import urlopen
import re
import time

#Base URL
URL = 'http://sparkfun.com/products/'

#Product IDs to check
products = [11879, 11021]
pro_stock = [0, 0]

#Time in between checks in seconds
checkTimer = 900 

firstRun = 1

#Gmail Settings
GMAIL_USER = 'username'
GMAIL_PASS = 'password'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
RECIPIENT = 'user@domain.com'


def send_email(recipient, subject, text, html):
    smtpserver = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)
    
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = GMAIL_USER
    msg['To'] = recipient
    
    #Old code below
    #header = 'To:' + recipient + '\n' + 'From: ' + GMAIL_USER
    #header = header + '\n' + 'Subject:' + subject + '\n'
    #msg = header + '\n' + text + ' \n\n'
    
    html = """\
    <html>
       <head></head>
         <body>
           <p>"""+html+"""\
	  </p>
       </body>
    </html>
    """ 
    
    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    
    smtpserver.sendmail(GMAIL_USER, recipient, msg.as_string())
    smtpserver.close()
    
#Searches site for current stock and handles no stock or unknown stock
def get_stock(soup, pro_id):
	x = soup["quantity"]
	return x

#Searches site for name of item from title tag
def get_pro_name(soup, pro_id):
	x = soup["name"]
	return x

#Loops through each item id and check is stock changes since last check, compiles into email body and sends if there is data
#First run change says 0	
email_body=""
loop = 1
while loop == 1 :
 	
 	email_body=""
 	email_body_html=""
	for idx in range(0, len(products)):
		pro_id = products[idx]
		URL2 = URL + str(pro_id) + '.json'
		#print URL2

		webpage = urlopen(URL2)
		

		soup = json.load(webpage)
		stock = get_stock(soup, pro_id)
		if (stock != pro_stock[idx]):
			stockChange = int(stock) - int(pro_stock[idx])
			pro_stock[idx] = stock
			name = get_pro_name(soup, pro_id)
			if (firstRun):
				stockChange = 0
						
			email_body += name + ': ' +  str(pro_id) + ' currently has ' + str(stock) + ' in stock. ' + 'Change: ' + str(stockChange) + ' in past ' + str(checkTimer) + ' seconds\n'
			email_body_html += '<FONT COLOR=blue><b><a href=' + URL2[:-5] + '> ' + name + '</a>: </b></FONT>' +  str(pro_id) + ' currently has <FONT COLOR=RED><b>' + str(stock) + '</b></FONT> in stock. ' + 'Change: <FONT COLOR=RED><b>' + str(stockChange) + '</b></FONT> in past ' + str(checkTimer) + ' seconds<br><br>\n'
		
	if (email_body != ""):	
		print email_body
		send_email(RECIPIENT, 'SFE - Current Stock', email_body, email_body_html)
	else:
		print "No Change"

	firstRun = 0			
	time.sleep(checkTimer)
	
print "Done"
