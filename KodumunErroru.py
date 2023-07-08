import requests
import hashlib

URL = "https://api.pwnedpasswords.com/range/"
pss = "Al"

hashed_pass = hashlib.sha1(pss.encode()).hexdigest().upper()
first_5 = hashed_pass[:5]
last_5 = hashed_pass[5:]
req = requests.get(url=URL+first_5)
hash_list = req.text.split('\r\n')
for x in hash_list:
    hash_part = x.split(":")
    if(hash_part[0] == last_5):
        print(hash_part[0] + " + " + hash_part[1])
        print(pss)    

print(pss.encode())
print(hashlib.sha1(pss.encode()))
