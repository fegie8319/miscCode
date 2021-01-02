import smtplib
from email import  encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
server = smtplib.SMTP('smtp.gmail.com', 25)

server.ehlo()

with open('password.txt','r') as f:
    password = f.read()

server.login('fegie8319@gmail.com',password)


msg = MIMEMultipart()
msg['From'] = 'NeuralNine'
msg['To'] = 'fegie0109@gmail.com'
msg['Subject'] = 'Just A Test'

with open('massage.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message),'plain')