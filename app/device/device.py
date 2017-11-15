import string
import random
from config.config import Config
from awesome_codename import generate_codename


class Device:
    _NAME = ''
    _PASSWORD = ''
    _configFilePath = ''
    _ID = ''

    def __init__(self):
        self.config = Config()

        self._NAME = self.config.read('NAME')
        self._PASSWORD = self.config.read('PASSWORD')

    def generate_password(self, size=8, chars=string.ascii_letters + string.digits + string.punctuation):
        gen_pw = ''.join(random.choice(chars) for _ in range(size))

        if not self._PASSWORD:
            self._PASSWORD = gen_pw
            self.config.write('PASSWORD', gen_pw)

        return self._PASSWORD

    def generate_name(self):
        gen_name = generate_codename().replace(' ', '_')

        if not self._NAME:
            self._NAME = gen_name
            self.config.write('NAME', gen_name)

        return self._NAME

    @property
    def name(self):
        return self._NAME

    @property
    def password(self):
        return self._PASSWORD

    @property
    def id(self):
        return self._ID

