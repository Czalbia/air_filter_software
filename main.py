import os
import json
import time

apikey=input()

while True:

    file= os.system(f"curl -X GET     --header 'Accept: application/json'     --header 'apikey: {apikey}'     'https://airapi.airly.eu/v2/measurements/installation?installationId=3328' |json_pp > myfile.json")
    pollution=[0,0,0,0,0,0]
    f=open('mydata.json')
    file = json.load(f)

    counter =0
    for i in file['current']['values']:
        pollution[counter]+=i['value']
        counter+=1
    print(pollution)

    if pollution[0]>25 or pollution[1]>15 or pollution[2]>10:
        print("Activate the filter!")
        #In the future here will be some code for TUYA electrical socket activation

    time.sleep(60*15)