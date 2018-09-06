import configparser


def get_config(section):
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config[section]