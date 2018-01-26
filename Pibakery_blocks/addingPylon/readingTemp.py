#!/usr/bin/python

import os
import sys
import json

os.system("sudo modprobe w1-gpio")
os.system("sudo modprobe w1-therm")

#include w1thermsensor - which needs for reading DS18B20 temperature sensors
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


#Reading every file which contains sensor address in Sensor directory
path = "/home/pi/Sensor"
for filename in os.listdir(path):
        filename = os.path.join(path, filename)
        SensorList = []

        #Reading Pylon's ID in sensor_list file
        with open(filename, "r") as sensor_file:
                Pylon_ID = sensor_file.readline().strip()
        sensor_file.close()


        #Reading sensor's address in sensor_list file
        with open(filename, "r") as sensor_file:
                next(sensor_file)
                for line in sensor_file:
                        sensor = Sensor(line.strip())
                        SensorList.append(sensor)
        sensor_file.close()


        #Export the result in one line
        #Reading = json.dumps({'Pylong': [{'name': sys.argv[1], 'Sensors': [u.getTemp() for u in SensorList]}]})

        #Export the result in separate lines
        Reading = json.dumps({'Pylon': [{'name': Pylon_ID, 'Sensors': [u.getTemp() for u in SensorList]}]}, indent=4, sort_keys=True)
        print(Reading)

        #Export the result to readingData files according to Pylon's ID
        with open("/home/pi/readingData_{}".format(Pylon_ID), "w+") as readingData:
                readingData.write(Reading + '\n')


#To check the W1ThermSensor
#for sensor_reading in W1ThermSensor.get_available_sensors():
#       print("Sensor %s has temperature %.2f" % (sensor_reading.id, sensor_reading.get_temperature()))

