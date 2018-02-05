#!/usr/bin/python

import os
import os.path
import sys
import json

os.system("sudo modprobe w1-gpio")
os.system("sudo modprobe w1-therm")

sys.path.insert(0, "/usr/local/lib/python3.5/dist-packages/")
from w1thermsensor import W1ThermSensor


#This class is used to create Sensor's objects according to their addresss
class Sensor:
    def __init__(self, Sensor_ID):
        self.Sensor_ID = Sensor_ID

    def getID(self):
        return "{}\n".format(self.Sensor_ID)

    def getTemp(self):
        temperature = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, self.Sensor_ID)
        Temp_C = temperature.get_temperature()
        return "Sensor_ID: {0}, value: {1}".format(self.Sensor_ID, Temp_C)


SensorList = []

#Reading the input arrguments from Pibakery and adding sensor's objects to SensorList
#from argument 2nd to 9th
for x in range(2, 9):
    sensor = Sensor(sys.argv[x])
    SensorList.append(sensor)

#Exporting the result in one line
#Reading = json.dumps({'Pylong': [{'name': sys.argv[1], 'Sensors': [u.getTemp() for u in SensorList]}]})

#Exporting the result in separate lines - to test the sensor cable on every boot state (store in everyboot.log)
Reading = json.dumps({'Pylon': [{'name': sys.argv[1], 'Sensors': [u.getTemp() for u in SensorList]}]}, indent=4, sort_keys=True)
print(Reading)

#Exporting the result to readingData file - to test the sensor cable on the every boot state (store in readingData file)
with open("/home/pi/readingData{}".format(sys.argv[1]), "w+") as readingData:
    readingData.write(Reading + '\n')

# Checking whether Sensor dir is not exist (to store the sensor's addresses of cables in different files)
if not os.path.exists("/home/pi/Sensor"):
    os.system("mkdir -p /home/pi/Sensor")

#Export the sensor address to files and the file names are named according to their Pylon's ID
with open("/home/pi/Sensor/sensor_list_{}".format(sys.argv[1]), "w+") as sensor_list:
    sensor_list.write(sys.argv[1] + "\n")
    for item in SensorList:
        sensor_address = item.getID()
        sensor_list.write(sensor_address)

