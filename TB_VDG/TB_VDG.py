import time
import datetime as dt
import random
import json
import requests

url = "http://YOURDOMAIN/api/v1/YOURTOKEN/telemetry"

data = []

min=190
max=300
count=0

for j in range (0,100) :
    random_number = random.randint(min,max)
    time_rn = dt.datetime.now()
    time_rn_j = time_rn.isoformat()
    datas = {
        "v":random_number,
        "RequestTime":time_rn_j,
        }
    data.append(datas)
    count = random_number/10
    min = random_number-count
    max = random_number+count
    min = round(min)
    max = round(max)
    if min < 190 :
        min = 190
    if max > 300 :
        max = 300

    with open('data.json','w') as j_files:
        json.dump(data,j_files,indent=4)

    print ("Voltage:",random_number)
    print ("Time:",time_rn)

    send = requests.post(url,json=datas)

    if send.status_code == 200 :
        print ("Request succesfull.")
    else :
        print ("Request failed.")
        break

    check = send.status_code
    print ("Status Code:",check)

    print (send)

    time.sleep(1)
