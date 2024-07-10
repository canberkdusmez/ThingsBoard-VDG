import time
import random
import json
import requests

url = "http://YOURDOMAIN/api/v1/YOURTOKEN/telemetry"

data = [{"v": random.randint(190, 300)} for _ in range(100)]

with open('data.json','w') as j_files:
    json.dump(data,j_files,indent=4)
with open ("data.json","r") as j_files :
    file = json.load(j_files)

for item in file :

    send = requests.post(url,json=item)

    if send.status_code == 200 :
        print ("Request succesfull.")
    else :
        print ("Request failed.")

    check = send.status_code
    print ("Status Code:",check)

    print (send)

    time.sleep(1)
