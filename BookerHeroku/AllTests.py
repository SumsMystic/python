'''
Created on Sep 18, 2024

@author: Sumeet Agrawal
'''


import requests
#import json

heads = {"Content-Type": "application/json"}
data = {"username": "admin", "password": "password123"}
resp = requests.post("https://restful-booker.herokuapp.com/auth", verify=False, headers=heads, json=data)
print(resp.status_code)
print(resp.json())