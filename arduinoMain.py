import os
import json
import time
import requests
import logging
import pyfirmata


#opening up required files
classified = json.load(open('classified.json', 'r'))
board = pyfirmata.Arduino('COM4')
R,Y, G=12,11,10
# while loop bc we want to alwyas check the air quality
while True:
    board.digital[R].write(0)
    board.digital[G].write(0)
    board.digital[Y].write(0)
    file = os.system(
        f'''curl -X GET     --header "Accept: application/json"     --header "apikey: {classified['airlyApiKey']}"     "https://airapi.airly.eu/v2/measurements/installation?installationId=3328" > mydata.json''')

    file = json.load(open('mydata.json'))

    # getting  AIRLY_CAQI indes from mydata.json
    pollution = 0
    for i in file['current']['indexes']:
        pollution += i['value']
    # In the future here will be some code for TUYA electrical socket activation
    if  pollution < 30: 
        print(f'Air pollution is small({pollution})')
        board.digital[G].write(1)
    elif pollution > 30:
        print(f'Air pollution is medium({pollution})')
        board.digital[Y].write(1)
    elif pollution > 50:
        print(f'Air pollution is heavy({pollution})')
        board.digital[R].write(1)

    time.sleep(10)
    

f.close()