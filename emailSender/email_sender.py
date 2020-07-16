

"""
Email Sender
sending email to your friends
-some nice subject using html
-attaching image

smtplib- allow us to call SMTP server  - when we send emails
SMTP (simple mail transfer protocol) is a push protocol and is used to send the mail
for more information : https://www.geeksforgeeks.org/simple-mail-transfer-protocol-smtp/

 for make it work:
 change our seting of the gmail email to enable less secure app
 https://myaccount.google.com/lesssecureapps?pli=1

 you, as email sender  enter your email  and password for where you want to send the email

learn from
youtube.com/watch?v=JRCJ6RtE3xU
"""
print(__doc__)
import smtplib
import imghdr
from email.message import EmailMessage
from string import Template
from pathlib import Path # allow us to access  html file


html= Template(Path('index.html').read_text())
# how we send the eamil to
contacts=['a@gmail.com','b@gmail.com']
# create email
email= EmailMessage()
email['from']='your friend'
email['to']=', '.join(contacts)
email['subject']='you are amazinggg'

# email.set_content('haaahhaaa')
email.set_content(html.substitute({'name':'lucky you!'}),'html')



# create SMTP server for client with gmail account

# attached image

with open('img.jpg','rb') as file:
    file_data=file.read()
    file_type=imghdr.what(file.name)
    # print(file_type)
    file_name=file.name


email.add_attachment(file_data, maintype='image',subtype=file_type,filename=file_name)


sender_email = input("enter your email and press enter: ")
password = input("enter your password and press enter: ")
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()# ehlo func is part of the smtp protocol - the agreement- init the server
    smtp.starttls()# tls- encryption mechanism - connect securty to the server

    """"
    connect to the gmail account of the sender
    parameters:  email adders and password

    """
    smtp.login(sender_email,password)
    smtp.send_message(email)
    print("email send successfully")