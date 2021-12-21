import os
import json
import time


classified= json.load(open('classified.json', 'r'))

apikey=classified['airlyApiKey']


while True:

    file= os.system(f"curl -X GET     --header 'Accept: application/json'     --header 'apikey: {apikey}'     'https://airapi.airly.eu/v2/measurements/installation?installationId=3328' |json_pp > mydata.json")
    
    
    file = json.load(open('mydata.json'))

    pollution=0

    for i in file['current']['indexes']:
        pollution+=i['value']
    if pollution>30:
        print('Activate the air filter!')
        #In the future here will be some code for TUYA electrical socket activation

    time.sleep(60*15)

f.close()