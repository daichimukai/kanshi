import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

FROM_ADDRESS = 'your gmail address'
MY_PASSWORD = 'password'
TO_ADDRESS = 'destination address'
SUBJECT = 'testmail'
BODY = 'test'

def create_massage(from_addr,to_addr,subject,body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg

def send(from_addr,to_addr,msg):
    smtpobj = smtplib.SMTP('smtp.gmail.com',587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(FROM_ADDRESS,MY_PASSWORD)
    smtpobj.sendmail(from_addr,to_addr,msg.as_string())
    smtpobj.close()

if __name__ == '__main__':
    to_addr = TO_ADDRESS
    subject = SUBJECT
    body = BODY
    msg = create_massage(FROM_ADDRESS,to_addr,subject,body)
    send(FROM_ADDRESS,to_addr,msg)