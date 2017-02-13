# Simple code to send data from Raspberry Pi to IoTtweet.com
# Raspberry Pi should have WiFi dongle or built-in WiFi module
# Coding : Isaranu Janthong
# 2017.Feb.13
# version : 0.0.1A

import requests
import time

while True:
	# Read CPU temperature of RPi
	cpu_temp = int(open('/sys/class/thermal/thermal_zone0/temp').read())/1e3

	# Input data
	userid = 'your user id'     #An IoTtweet account user ID 
	key = 'your device key'     #A key of device registered in IoTtweet 'My IoT garage'
	slot0 = cpu_temp
	slot1 = 0	#not use now
	slot2 = 0	#not use now
	slot3 = 0	#not use now
	tw = 'RaspberryPi3 Temp.'
	twpb = ''	#not use now

	# Merge data
	payload = {'userid':userid, 'key':key, 'slot0':slot0,'slot1':slot1,'slot2':slot2,'slot3':slot3,'tw':tw,'twpb':twpb}

	# Send to IoTtweet 
	r = requests.get('http://api.iottweet.com',params=payload)

	print ('RPi 3 Core temperature : ', cpu_temp, ' celcuis')
	print(r.url)

	# Display response from IoTtweet server
	print(r.text)

	print('Wait refresh..')
	time.sleep(15)	# Wait at least 15 sec.
