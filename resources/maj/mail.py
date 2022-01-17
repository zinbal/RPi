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
send_from =  "yournamehere"
send_to = "varnit.kashyap@gmail.com"
subject = "INTRUSION DETECTED"
body = "There is a intruder in your AREA   P.F.A. intruder image"			#enter your mail body here in " "
username  =  "mymailid@gmail.com"						  	#enter your email id here
password =  "mypassword"								#enter your pass here
attachmentPath  = "/home/pi/Desktop/threat.jpg"          				#enter attachment path here


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

def attachment(aP):
	part = MIMEBase('application', "octet-stream")
	with open(aP, 'rb') as file:
	    part.set_payload(file.read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition',
	                'attachment; filename="{}"'.format(Path(attachmentPath).name))
	msg.attach(part)

try:
    attachment(attachmentPath)#if you dont want to send attachments mark its starting with #
except:
    print("no image")
attachmentPath="/home/pi/Desktop/video.h264"
try:
    attachment(attachmentPath)
except:
    print("no video")
    
smtp = smtplib.SMTP(server, port)
if use_tls:
    smtp.starttls()
smtp.login(username, password)
smtp.sendmail(send_from, send_to, msg.as_string())
smtp.quit()

print ("Message Sent")
