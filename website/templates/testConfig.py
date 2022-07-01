from configparser import ConfigParser

file = 'website/templates/config.ini'
config = ConfigParser()
config.read(file)

print(config.sections())
print(list(config['dark']))
if config['dark']['status'] == 'on':
    print("GELAP")
elif  config['dark']['status'] == 'off':
    print("TERANG")


config.set('dark', 'status', 'off')
with open(file, 'w') as configfile:
    config.write(configfile)