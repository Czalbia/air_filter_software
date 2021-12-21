import os
import json
import time

#Your api key
apikey=

while True:

    data= os.system(f"curl -X GET     --header 'Accept: application/json'     --header 'apikey: {apikey}'     'https://airapi.airly.eu/v2/measurements/installation?installationId=3328' |json_pp > mydata.json")
    pollution=[0,0,0,0,0,0]
    f=open('mydata.json')
    data = json.load(f)

    counter =0
    for i in data['current']['values']:
        pollution[counter]+=i['value']
        counter+=1
    print(pollution)

    if (pollution[0]>25 or pollution[1]>15 or pollution[2]>10):
        print("Activate the filter!")

    time.sleep(60*15)



# curl -X GET -sD -     --compressed     --header 'Accept: application/json'     --header 'Accept-Encoding: gzip'     --header 'apikey: ykObTynCnnXkvdBM1o2ezfUmXKeRbyrM'     'https://airapi.airly.eu/v2/measurements/installation?installationId=3328'


