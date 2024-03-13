import configparser
import os

wd = os.getcwd()
riab = wd + '/riab.ini'
  
config = configparser.ConfigParser()
config.read('riab.ini')

credentials_file = " "
project_id = " "
user_number = " " 

for key in config['bigquery']:
    config['bigquery'][key] = config['bigquery'][key].replace('{user_number}', user_number).replace('{project_id}', project_id).replace('{credentials_file}', credentials_file)

config['bigquery']['user_number'] = user_number

with open('riab.ini', 'w') as configfile:
    config.write(configfile)