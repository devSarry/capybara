import requests
from config.config import Config


class ApiBase(object):
    _base_url = 'http://sensor.makkaraperuna.com/api/'
    _api_version = 'v1'
    _jwt_token = ''
    _id = ''

    def __init__(self):
        self._config = Config()

    def refresh_token(self):
        pass

    # Post data to server
    #
    # endpoint(string) : required
    #       relative endpoint url
    # payload (dictionary) : re
    def post(self, endpoint, payload=None, json=None):
        endpoint_url = self._base_url + endpoint

        try:
            if json:
                r = requests.post(endpoint_url, json=json)
            else:
                r = requests.post(endpoint_url, data=payload)
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            print('Request failed: {}'.format(e))
            raise

    def get(self, endpoint):
        endpoint_url = self._base_url + endpoint
        try:
            r = requests.get(endpoint_url).raise_for_status()
            r = requests.get(endpoint_url).json()
            return r
        except requests.RequestException as e:
            print('Request failed: {}'.format(e))
            raise

