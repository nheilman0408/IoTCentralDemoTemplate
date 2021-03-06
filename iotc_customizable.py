import time
import random
import uuid
import datetime
import random
import json
import sys
import logging
import datetime
import time
import threading
import os
import iotc
from iotc import IOTConnectType

################################
#SAMPLE TELEMETRY CONFIGURATION#
################################
#Enter 3 pieces of telemetry you would like to visualize
#These will be the same as what you defined in the IoT Central Device Template
#Telemetry 1 Name, Minimum & Maximum Values
t1name = 'temperature'
t1min = 70
t1max = 100
#Telemetry 2 Name, Minimum & Maximum Values
t2name = 'humidity'
t2min = 70
t2max = 100
#Telemetry 3 Name, Minimum & Maximum Values
t3name = 'motion'
t3min = 0
t3max = 1

#Specify the cadence in which you would like to send values (seconds)
seconds = 2

#############################
#IOT CENTRAL CONNECTION INFO#
#############################
#Enter in your Credential Type, Certificate, Scope ID and Device ID from the IoT Central UI.
credType = IOTConnectType.IOTC_CONNECT_SYMM_KEY
keyORcert = "************************"
scopeId = '*******'
deviceId = '********'


#Establish IoT Central Connection with those values
device = iotc.Device(scopeId, keyORcert, deviceId, credType)
device.connect()

#Construct a JSON payload of telemetry and properties to send to IoTC at the specified cadence.
#A UUID and timestamep are generated by default as part of the properties. 
def sendMessage():
    telemetryvalues = {t1name: random.randint(t1min, t1max), t2name: random.randint(t2min, t2max), t3name: random.randint(t3min,t3max)}
    propertyvalues = {'source': 'python-script', 'id': uuid.uuid4().hex, 'timestamp': str(datetime.datetime.utcnow())}      
    telemetry = json.dumps(telemetryvalues)
    properties = json.dumps(propertyvalues)    
    print("Sending telemetry Message(s)" + telemetry)
    print("Sending property Message(s)" + properties)
    device.sendTelemetry(telemetry)
    device.sendProperty(properties)

ticker = threading.Event()
while not ticker.wait(seconds):
    sendMessage()

