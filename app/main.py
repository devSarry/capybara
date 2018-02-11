# -*- coding: utf-8 -*-
import json

import time, sys
import requests
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

def refresh_token(token):
    refresh_url = "http://sensor.makkaraperuna.com/api/refresh"
    header_token = {'Authorization': 'Bearer ' + token}
    r = requests.get(refresh_url, header_token)
    v = r.headers['Authorization']
    #print(r.headers['Authorization'])
    #print new token key every time refreshing for debugging - take all string except 'Bearer ' (7 words)
    print(v[7:] + '\n')
    return v[7:]

def main():
    # while False:
    #     client.post(READINGS_URL, json=payload)
    #     time.sleep(10)
    #READINGS_URL = 'device/{}/readings?token={}'.format(client.id, x)
    new_token = client.jwt_token
    times = 0

    while True:
        READINGS_URL = 'device/{}/readings?token={}'.format(client.id, new_token)
        readings_from_sensors = []
        for sensor in W1ThermSensor.get_available_sensors():
            readings_from_sensors.append({'uuid': sensor.id , 'value': sensor.get_temperature()})

        payload = {'reading': json.dumps({'sensors': readings_from_sensors})}
        client.post(READINGS_URL, payload)
        time.sleep(10)
        times = times + 1
        #print(times) #To check the times

        #refreshing token key after 33mins ((200*10)/60))
        if times == 200:
            new_token = refresh_token(new_token)
            times = 0

if __name__ == '__main__':
    client = client_init()
    print(client.jwt_token + "\n")
    print("\nPython %s" % sys.version)
    print("IoT Client for Python")
    print("Device: {}".format(client.id))
    print("Starting to send readings...")
    main()
