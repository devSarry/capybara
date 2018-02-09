# -*- coding: utf-8 -*-
import json

import time, sys

from api.auth import Auth
from device.device import Device
from random import randint
from w1thermsensor import W1ThermSensor

device = Device()

NAME = device.name
PASSWORD = device.password
READINGS_URL = ''


def client_init():
    sensor = W1ThermSensor()
    reg = Auth()
    try:
        if not NAME:
            d_name = device.generate_name()
            d_pass = device.generate_password(20)
            d_token = device.config.read('SECRET_KEY')

            reg.register(d_name, d_pass, d_token)
            JWT_TOKEN = reg.jwt_token
            return reg
        else:
            reg.login(device_name=NAME, password=PASSWORD)
            JWT_TOKEN = reg.jwt_token
            return reg
    except:
        print('Authenticaion Failed. Device not initilized')


def main():
    # while False:
    #     client.post(READINGS_URL, json=payload)
    #     time.sleep(10)
    READINGS_URL = 'device/{}/readings?token={}'.format(client.id, client.jwt_token)

    while True:
        readings_from_sensors = []
        for sensor in W1ThermSensor.get_available_sensors():
            readings_from_sensors.append({'uuid': sensor.id , 'value': sensor.get_temperature()})

        payload = {'reading': json.dumps({'sensors': readings_from_sensors})}
        client.post(READINGS_URL, payload)
        time.sleep(10)


if __name__ == '__main__':
    client = client_init()

    print("\nPython %s" % sys.version)
    print("IoT Client for Python")
    print("Device: {}".format(client.id))
    print("Starting to send readings...")
    main()
