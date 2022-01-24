from fileinput import filename
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()

with open('email.txt', 'r') as email:
    password = email.readline()

server.login('testmail@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'gmail'
msg['To'] = 'test.test'
msg['Subject'] = 'Testing email'

with open('message.txt', 'r') as message:
    text = message.read()

msg.attach(MIMEText(text, 'plain'))
filename = 'sem_titulo.png'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', 'attachment; filename={}'.format(filename))
msg.attach(p)

txt = msg.as_string()
server.sendmail('HERE A VALID EMAIL', 'test.test', txt)
