import os
import sys
import datetime
import urllib.request as urlreq
import kanshi_tools.smtp as smtp
import kanshi_config.config as config

url = config.url
FROM_ADDRESS = config.from_address
MY_PASSWORD = config.my_password
TO_ADDRESS = config.to_address
SUBJECT = config.subject
BODY = config.body
msg = smtp.create_message(FROM_ADDRESS,TO_ADDRESS,SUBJECT,BODY)
T = 2

sys.stdout = open("kanshi.log","a")

print(datetime.datetime.now(), end=': ')
try:
    if os.path.exists("./kanshi_tools/old.txt") == False:
        with urlreq.urlopen(url) as f:
            with open('./kanshi_tools/old.txt','w') as u:
                u.write(str(f.read()))
                exit(0)
    
    with urlreq.urlopen(url) as f:
        with open('./kanshi_tools/new.txt','w') as u:
            u.write(str(f.read()))
    
    with open('./kanshi_tools/new.txt') as a:
        with open('./kanshi_tools/old.txt')as f:
            if f.read() == a.read():
                T = 0
            else:
                T = 1
    
    if T == 0:
        smtp.send(FROM_ADDRESS,TO_ADDRESS,msg,MY_PASSWORD)
        print("A notification was sent to " + TO_ADDRESS, end="")
    
    os.remove('./kanshi_tools/old.txt')
    
    os.rename('./kanshi_tools/new.txt','./kanshi_tools/old.txt')
except Exception as e:
    print(e,end='')

if os.path.exists("./kanshi_tools/new.txt") == True:
    os.remove("./kanshi_tools/new.txt")

print('')

sys.stdout.close()
