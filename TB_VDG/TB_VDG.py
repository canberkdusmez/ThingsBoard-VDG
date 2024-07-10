import time
import datetime as dt
import random
import json
import requests

url = "http://YOURDOMAIN/api/v1/YOURTOKEN/telemetry"

data = []

a=190
b=300
c=0

for j in range (0,100) :
    random_number = random.randint(a,b)
    time_rn = dt.datetime.now()
    time_rn_j = time_rn.isoformat()
    datas = {
        "v":random_number,
        "RequestTime":time_rn_j,
        }
    data.append(datas)
    c = random_number/10
    a = random_number-c
    b = random_number+c
    a = round(a)
    b = round(b)
    if a < 190 :
        a = 190
    if b > 300 :
        b = 300

    with open('data.json','w') as j_files:
        json.dump(data,j_files,indent=4)

    print ("Voltage:",random_number)
    print ("Time:",time_rn)

    send = requests.post(url,json=datas)

    if send.status_code == 200 :
        print ("Request succesfull.")
    else :
        print ("Request failed.")

    check = send.status_code
    print ("Status Code:",check)

    print (send)

    time.sleep(1)
