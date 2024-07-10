import time
import random
import json
import requests

url = "http://(yourdomain)/api/v1/(yourtoken)/telemetry"

loop = 0
for loop in range (0,100) :

    random_number = random.randint(190,300)
    print ("Number Generated:",random_number)

    data = {"v":random_number}
    with open('data.json', 'w') as dosya:
        json.dump(data, dosya, indent=4)
    with open ("data.json","r") as j_files :
        file = json.load(j_files)

    send = requests.post(url,json=file)

    if send.status_code == 200 :
        print ("Request succesfull.")
    else :
        print ("Request failed.")

    check = send.status_code
    print ("Status Code:",check)

    print (send)

    time.sleep(1)
