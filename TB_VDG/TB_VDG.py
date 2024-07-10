import time
import random
import json
import requests

url = "http://YOURDOMAIN/api/v1/YOURTOKEN/telemetry"

data = []

for j in range (0,100) :
    random_number = random.randint(190,300)

    datas = {"v":random_number}
    data.append(datas)

with open('data.json','w') as j_files:
    json.dump(data,j_files,indent=4)
with open ("data.json","r") as j_files :
    file = json.load(j_files)

loop = 0
for loop in range (0,100) :

    send = requests.post(url,json=file)

    if send.status_code == 200 :
        print ("Request succesfull.")
    else :
        print ("Request failed.")

    check = send.status_code
    print ("Status Code:",check)

    print (send)

    time.sleep(1)
