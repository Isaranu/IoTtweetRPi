from IoTtweet import *

#Get version of IoTtweet.py
version = getversion()
print(version)

#An IoTtweet account userid (6 digits)
userid = 'YOUR USERID AN IoTtweet account'

#An IoTtweet registered iot device key (My IoT garage)
key = 'YOUR IoT device key'

while True:
    #Read CPU temperature of RPi
    cpu_temp = int(open('/sys/class/thermal/thermal_zone0/temp').read())/1e3
    print('CPU temperature : ' ,cpu_temp, ' celcius')
    
    #Prepare data
    slot1 = 0	#not use now
    slot2 = 0	#not use now
    slot3 = 0	#not use now
    tw = 'RaspberryPi3 Temp.'
    twpb = ''	#not use now

    #Send data to IoTtweet dashboard.
    res = WriteDashboard(userid, key, cpu_temp, slot1, slot2, slot3, tw, twpb)

    #Print response JSON from IoTtweet
    print(res)

    #Wait for 15 sec.
    time.sleep(15)
