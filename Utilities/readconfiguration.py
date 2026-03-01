from configparser import ConfigParser


def read_configuration(category,key):
    config = ConfigParser()
    config.read(r"C:\Users\Dell\PycharmProjects\PythonProject\Utilities\config.ini")
    return config.get(category,key)
