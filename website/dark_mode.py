from configparser import ConfigParser
def get_dark():
    file = 'website/config.ini'
    config = ConfigParser()
    config.read(file)
    return config['dark']['status']

def set_dark(mode):
    file = 'website/config.ini'
    config = ConfigParser()
    config.read(file)
    config.set('dark', 'status', mode)
    with open(file, 'w') as configfile:
        config.write(configfile)