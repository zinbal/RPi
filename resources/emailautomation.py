import smtplib
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

'''
	Keep in Mind to turn on less secure apps from < https://myaccount.google.com/lesssecureapps >
'''
send_from =  "your name here"
send_to = "varnit.kashyap@gmail.com"
subject = "INTRUSION DETECTED"
body = "There is a intruder in your AREA   P.F.A. intruder image"		#enter your mail body here in " "
username  =  "enteryourmailhere@gmail.com"						  		#enter your email id here
password =  "password"													#enter your pass here
attachmentPath  = "/home/pi/Desktop/1.txt"          				#enter attachment path here


msg = MIMEMultipart()
msg['From'] = send_from
msg['To'] = send_to
msg['Date'] = formatdate(localtime=True)
msg['Subject'] = subject
msg.attach(MIMEText(body))


'''
	Enter your desired email details in above para using reference
'''

server = "smtp.gmail.com"
port = 587
use_tls = True

def attachment():
	part = MIMEBase('application', "octet-stream")
	with open(attachmentPath, 'rb') as file:
	    part.set_payload(file.read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',
	                'attachment; filename="{}"'.format(Path(attachmentPath).name))
	msg.attach(part)


attachment()#if you dont want to send attachments mark its starting with #

smtp = smtplib.SMTP(server, port)
if use_tls:
    smtp.starttls()
smtp.login(username, password)
smtp.sendmail(send_from, send_to, msg.as_string())
smtp.quit()

print ("Message Sent")
