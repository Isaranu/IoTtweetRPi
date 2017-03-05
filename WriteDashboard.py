from IoTtweet import *

#Get version of IoTtweet.py
version = getversion()
print(version)

#An IoTtweet account userid (6 digits)
userid = 'YOUR USERID AN IoTtweet account'

#An IoTtweet registered iot device key (My IoT garage)
key = 'YOUR IoT device key'

#Edit your data
slot0 = 'your data'
slot1 = 'your data'
slot2 = 'your data'
slot3 = 'your data'
tw = 'your message'
twpb = 'your message'

#Send data to IoTtweet dashboard.
res = WriteDashboard(userid, key, slot0, slot1, slot2, slot3, tw, twpb)

#Print response JSON from IoTtweet
print(res)
