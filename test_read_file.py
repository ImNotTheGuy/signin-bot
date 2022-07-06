from jproperties import Properties

configs = Properties()

with open('config.properties', 'rb') as config_file:
    configs.load(config_file)
    
print(configs.get("username").data)
print(configs.get("password").data)