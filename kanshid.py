import os
import sys
import datetime
import urllib.request as urlreq
import kanshi_tools.smtp as smtp
import kanshi_config.config as config

url = config.url
T = 0

sys.stdout = open("kanshi.log","a")

print(datetime.datetime.now(), end=': ')

if os.path.exists("old.txt") == False:
    with urlreq.urlopen(url) as f:
        with open('old.txt','w') as u:
            u.write(str(f.read()))

with urlreq.urlopen(url) as f:
    with open('new.txt','w') as u:
        u.write(str(f.read()))

with open('new.txt') as a:
    with open('old.txt')as f:
        if f.read() == a.read():
            T = 0
        else:
            T = 1

os.remove('old.txt')

os.rename('new.txt','old.txt')

print(T)

sys.stdout.close()
