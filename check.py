import os

with open('aaaa') as a:    
    with open('memo1')as f:
        if f.read() == a.read():
            print(0)
        else:
            print(1)

os.remove('aaaa')