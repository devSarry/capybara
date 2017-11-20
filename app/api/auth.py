from device.device import Device
from abc import ABCMeta, abstractmethod
from api.base import ApiBase


class IAuth(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def register(self, device_name, password, token):
        pass

    @abstractmethod
    def login(self, device_name, password):
        pass


# Auth Class
# Example how to use the class
#     reg = Auth()
#
#     device = Device()
#     d_name = device.generate_name()
#     d_pass = device.generate_password(20)
#
#     print(reg.register(d_name, d_pass, device.config.read('SECRET_KEY')))
class Auth(IAuth, ApiBase):
    _base_auth_url = 'auth/device/'

    def __init__(self):
        self._jwt_token = ''
        self._id = ''
        pass

    def register(self, device_name=None, device_password=None, token=None):
        if not self.is_registered(device_name):
            signup_url = self._base_auth_url + 'signup'
            payload = {'name': device_name, 'password': device_password, 'secret_client_token': token}

            r = self.post(signup_url, payload)
            print(r['token'])
            if r['token']:
                self._jwt_token = r['token']
                self._id = r['device']['id']

            return r
        else:
            return False

    def login(self, device_name, password):
        login_url = self._base_auth_url + 'login'
        data = {"device_name": device_name, "password": password}

        r = self.post(login_url, data)

        self._jwt_token = r['token']
        self._id = r['device']['id']

        # TODO save device id for later

    def is_registered(self, device_name):
        check_url = self._base_auth_url + 'check'
        payload = {'device_name': device_name}
        r = self.post(check_url, payload)
        device_exists = r['device']

        return device_exists

    @property
    def id(self):
        return self._id

    @property
    def jwt_token(self):
        return self._jwt_token


            # reg = Auth()
# device = Device()
# d_name = device.generate_name()
# d_pass = device.generate_password(20)
# d_token = device.config.read('SECRET_KEY')
#
# print(reg.register(d_name, d_pass, d_token))