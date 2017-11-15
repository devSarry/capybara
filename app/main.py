# -*- coding: utf-8 -*-
import json

import helpers
import urllib, time, sys

from api.auth import Auth
from device.device import Device

device = Device()

NAME = device.name
PASSWORD = device.password
READINGS_URL = ''


def client_init():
    reg = Auth()
    try:
        if not NAME:
            d_name = device.generate_name()
            d_pass = device.generate_password(20)
            d_token = device.config.read('SECRET_KEY')

            reg.register(d_name, d_pass, d_token)
            JWT_TOKEN = reg._jwt_token
            return reg
        else:
            reg.login(device_name=NAME, password=PASSWORD)
            JWT_TOKEN = reg._jwt_token
            return reg
    except:
        print('Authenticaion Failed. Device not initilized')


def main():


    # while False:
    #     client.post(READINGS_URL, json=payload)
    #     time.sleep(10)
    READINGS_URL = 'device/{}/readings?token={}'.format(client.id, client.jwt_token)

    while True:
        temp_v = 10
        reading = json.dumps({'temp_senors': {'t_1': temp_v, 't_2': temp_v + 12}, "pylon": "a_1"})
        payload = { 'reading': reading}
        client.post(READINGS_URL, payload)
        time.sleep(10)
        temp_v += 1


if __name__ == '__main__':
    client = client_init()

    print("\nPython %s" % sys.version)
    print("IoT Client for Python")

    print("Starting to send readings...")
    while True:
        main()
