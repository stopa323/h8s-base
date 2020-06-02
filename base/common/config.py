import configparser

CONF = None


def get_config() -> configparser.ConfigParser:
    global CONF

    if not CONF:
        CONF = configparser.ConfigParser()
        CONF.read("../etc/base.ini")

    return CONF
