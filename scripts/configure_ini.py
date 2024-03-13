import configparser
import os

wd = os.getcwd()
riab = wd + '/riab.ini'
print(riab)    

config = configparser.ConfigParser()
config.read('riab.ini')

user_number = '1' 
project_id = 'mineral-order-416422'
credentials_file = 'mineral-order-416422-688fb24e116f'

for key in config['bigquery']:
    config['bigquery'][key] = config['bigquery'][key].replace('{user_number}', user_number).replace('{project_id}', project_id).replace('{credentials_file}', credentials_file)

config['bigquery']['user_number'] = user_number

with open('riab.ini', 'w') as configfile:
    config.write(configfile)