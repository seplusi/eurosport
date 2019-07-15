from src.main.configs.config import Config


configs = Config()
#config = configparser.ConfigParser()
#config.read('src/main/configs/properties.ini')

print(configs.sections())

print(configs.get('DatabaseSection', 'database.dbname'))
print('Hello World')