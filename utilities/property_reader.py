from configparser import ConfigParser

config = ConfigParser()
config.read("../configfiles/config.ini")


class ReadConfig:

    @staticmethod
    def get_data(section, key):
        data = config.get(section, key)
        return data
