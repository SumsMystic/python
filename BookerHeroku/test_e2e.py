'''
Created on Sep 18, 2024

@author: Sumeet Agrawal
'''


import requests
import os
import pytest
import logging
#import json

# logging.basicConfig(filename='logs.txt', format=logging.BASIC_FORMAT)
proj_logger = logging.getLogger(__name__)
proj_logger.level = logging.DEBUG
log_file_handler = logging.FileHandler("logs/default_log_file.log")
log_formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s: %(message)s")
log_file_handler.setFormatter(log_formatter)
proj_logger.addHandler(log_file_handler)
proj_logger.debug("\n **************  START NEW RUN  **************")

@pytest.mark.smoke
def test_correct_auth():
    
    # bs_url = str(os.environ.get("base_url"))
    # print(bs_url)
    # bs_url = "https://restful-booker.herokuapp.com"
    
    heads = {"Content-Type": "application/json"}
    data = {"username": "admin", "password": "password123"}
    resp = requests.post("https://restful-booker.herokuapp.com/auth", verify=False, headers=heads, json=data)
    # print(resp.status_code)
    # print(resp.json())
    proj_logger.debug("Testing the DEBUG level logging without initializing")
    proj_logger.debug(resp.status_code)
    proj_logger.debug(resp.json())
    