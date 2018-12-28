import urllib.request as urlreq

path = 'URL'

with urlreq.urlopen(path) as f:
     with open('test.txt','w') as u:
         u.write(str(f.read()))