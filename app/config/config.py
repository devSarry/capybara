import yaml
import os
import sys


class Config:
    def __init__(self, config_path='config.yaml'):
        #self._configFilePath = os.path.join(os.getcwd(), config_path)
        #checking whether python3.5 dir is existent

        if (sys.version_info.major == 3):
            _BASE_DIR_ = "/usr/local/lib/python3.5/"
        else:
            _BASE_DIR_ = "/usr/local/lib/python2.7/"

        if os.path.exists(_BASE_DIR_):
            self._configFilePath = os.path.abspath(_BASE_DIR_ + "dist-packages/capybara-0.1-py3.5.egg/app/config.yaml")
        else:
            print("Error while getting path");

        try:
            stream = open(self._configFilePath, 'r')
            self.config = yaml.load(stream)
        except IOError as e:
            print('An IOError occurred. {}'.format(e.args[-1]))
        finally:
            stream.close()

    def read(self, key=None):
        try:
            stream = open(self._configFilePath, 'r')
            self.config = yaml.load(stream)
        except IOError as e:
            print('An IOError occurred. {}'.format(e.args[-1]))
        finally:
            stream.close()
        return self.config[key]

    def write(self, key, value):
        try:
            stream = open('config.yaml', 'r')
            data = yaml.load(stream)
            data[key] = value

            with open('config.yaml', 'w') as yaml_file:
                yaml_file.write(yaml.dump(data, default_flow_style=False))
        except IOError as e:
            print('An IOError occurred. {}'.format(e.args[-1]))
        finally:
            stream.close()