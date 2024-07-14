""" go to gmail >>> stup twofa
#generate app password
#create a function to send the mail"""


#import this
from email.message import EmailMessage
#from second import password: this is another python file in my folder where i created a variable named password where i stored my original password
# , from where you stored it or you can just input it directly
from second import password

"""importing ssl is to establish a secure connection with the mail server. This ensures that your email content,
 including sender and recipient information, is encrypted during transmission.
#for security, standard practice"""

import ssl


"""smtplib for Core Functionality: The smtplib module provides the essential functions for interacting with an SMTP 
(Simple Mail Transfer Protocol) server. It allows you to establish a connection, send commands,
 authenticate with the server, and ultimately send your email message."""
import smtplib





email_sender = "marvsticks123@gmail.com"
email_password = password

email_receiver = "jancyalice09@gmail.com"

subject = "My first time sending emails through python coding"
body = """I am growing steadily in mmy python progamming. I plan to be better at this as time goes by.
    I started this in the month of june 2024 at CIH. I am being taught by Daddy K and he seems to be
    the best. I want to upgrade by coding skills day by day untill i am at the peak of the iceberg.
    A wise man once said the you in you is the you you will become
    Thank you for reading the first email i sent using python
"""
#here you are going to arrange your email the way it is arranged on your phone for example
#you have your from, to, subject, body, 
em = EmailMessage
em['From'] = email_sender
em['TO'] = email_receiver
em['Subject']


#note .set_content
em.set_content(body)

contex = ssl.create_default_context()

with smtplib.SMTP_SSL('stmp.gmail.com', 465, context=contex) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver,em.as_string())