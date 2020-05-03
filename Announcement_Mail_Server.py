"""
@author: Giray Coskun
@github: https://github.com/giraycoskun

Reference:
    https://realpython.com/python-send-email/#option-2-setting-up-a-local-smtp-server
    https://developers.google.com/gmail/api/quickstart/python

Docs:
    https://docs.python.org/3/library/smtplib.html
    https://docs.python.org/3/library/email.mime.html

Notes:
    For Gmail server enable https://myaccount.google.com/lesssecureapps
    localhost server command: python -m smtpd -c DebuggingServer -n localhost:1025
"""

import smtplib, ssl
from datetime import date
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from main2 import main

MY_ADDRESS = 'coskun.giray.07@gmail.com'
PASSWORD = ""
host = 'localhost'  # 'smtp.gmail.com'
port = 1025  # 587

today = date.today()
today_str = today.strftime('%d/%m/%Y')

# MAIL
sender_email = "coskun.giray.07@gmail.com"
receiver_email = "coskun.giray.07@gmail.com"
subject = "mySU Announcements " + today_str

# announcements = main()


##CREATE EMAIL
message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

##################################
context = ssl.create_default_context()
try:
    server = smtplib.SMTP(host, port)
    # server.ehlo()  # Can be omitted
    # server.starttls(context=context)
    # server.ehlo()  # Can be omitted
    # server.login(MY_ADDRESS, PASSWORD)
    server.sendmail(sender_email, receiver_email, message.as_string())
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit()

