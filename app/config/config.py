import yaml
import os


class Config:
    def __init__(self, config_path='config.yaml'):
        self._configFilePath = os.path.join(os.getcwd(), config_path)
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
