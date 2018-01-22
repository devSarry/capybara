#!/usr/bin/python

import os
import sys
import json

os.system("sudo modprobe w1-gpio")
os.system("sudo modprobe w1-therm")

sys.path.insert(0, "/usr/local/lib/python3.5/dist-packages/")
from w1thermsensor import W1ThermSensor



class Sensor:
    def __init__(self, Sensor_ID):
        self.Sensor_ID = Sensor_ID

    def getID(self):
        self.Sensor_ID

    def getTemp(self):
        temperature = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, self.Sensor_ID)
        Temp_C = temperature.get_temperature()
        return "Sensor_ID: {0}, value: {1}".format(self.Sensor_ID, Temp_C)


SensorList = []

for x in range(2, 9):
    sensor = Sensor(sys.argv[x])
    SensorList.append(sensor)

#Export the result in one line
#Reading = json.dumps({'Pylong': [{'name': sys.argv[1], 'Sensors': [u.getTemp() for u in SensorList]}]})

#Export the result in separate lines
Reading = json.dumps({'Pylon': [{'name': sys.argv[1], 'Sensors': [u.getTemp() for u in SensorList]}]}, indent=4, sort_keys=True)
print(Reading)

#Export the result to readingData file
with open("/home/pi/readingData", "w+") as readingData:
    readingData.write(Reading + '\n')
