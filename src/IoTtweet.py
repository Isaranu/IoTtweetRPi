
import requests
import time

def WriteDashboard(_userid,_key,_slot0,_slot1,_slot2,_slot3,_tw,_twpb):

    #Input data
        userid = _userid
        key = _key
        slot0 = _slot0
        slot1 = _slot1
        slot2 = _slot2
        slot3 = _slot3
        tw = _tw
        twpb = _twpb

        #Merge data
        payload = {'userid':userid, 'key':key, 'slot0':slot0,'slot1':slot1,'slot2':slot2,'slot3':slot3,'tw':tw,'twpb':twpb}

        #Send to IoTtweet 
        r = requests.get('http://api.iottweet.com',params=payload)
        response = r.text
        
        #Display response from IoTtweet server
        return response

def getversion():
    #Get version of IoTtweet.py
        return '0.1' 
