import ConfigParser

config_file = ConfigParser()
config_file.read("../config.ini")
sections = config_file.sections()

def get_value(section, key) :
    try :
        return config_file.get(section,key)
    except:
        return None