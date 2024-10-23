'''
Created on Oct 21, 2024

@author: Sumeet Agrawal
'''

import configparser

def get_config_option(confSectionName, confOptioname, fileName='pytest.ini'):
    config = configparser.ConfigParser()
    config.read(fileName)
    conf_option_val = config.get(confSectionName, confOptioname)
    return conf_option_val
    # print(conf_option_val)