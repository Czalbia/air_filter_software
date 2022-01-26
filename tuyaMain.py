import os
import json
import time
import requests
from tuya_iot import (
    TuyaOpenAPI,
    AuthType,
    TUYA_LOGGER
)
import logging



TUYA_LOGGER.setLevel(logging.DEBUG)

#opening up required files
classified = json.load(open('classified.json', 'r'))
commands =  json.load(open('commands.json', 'r'))

#setting up the Tuya api
tuyaApi = TuyaOpenAPI(
    classified["TuyaEndPoint"], classified["TuyaAccessId"], classified["TuyaAccessKey"],AuthType.CUSTOM)
tuyaApi.connect(classified["TuyaUsername"], classified["TuyaPassword"])

# while loop bc we want to alwyas check the air quality
while True:

    # file = os.system(
    #     f'''curl -X GET     --header "Accept: application/json"     --header "apikey: {classified['airlyApiKey']}"     "https://airapi.airly.eu/v2/measurements/installation?installationId=3328" > mydata.json''')

    file = json.load(open('mydata.json'))

    # getting  AIRLY_CAQI indes from mydata.json
    pollution = 0
    for i in file['current']['indexes']:
        pollution += i['value']
    # checking if it is alright
    if pollution > 40:
        print('Activate the air filter!')
        tuyaApi.post(f'/v1.0/iot-03/devices/{classified["TuyaDeviceId"]}/commands', commands)
        # tuyaApi.post(f'/v1.0/iot-03/devices/{classified["TuyaDeviceId2"]}/commands', commands)
        # In the future here will be some code for TUYA electrical socket activation
    print(pollution)
    time.sleep(60*15)
    

f.close()