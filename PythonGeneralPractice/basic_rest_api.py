'''
Created on Sep 23, 2024

@author: Sumeet Agrawal
'''

# Write a REST API based prog to cover basic commands

import requests
import random

base_url = "https://test.heroku.com"

def get_list_all_custs():
    get_cust_info_url = base_url + "/customers"
    resp = requests.get(url=get_cust_info_url, verify=False)
    assert resp.status_code == 200
    print("Information of all customers is here:", resp.json())

def add_new_cust():
    rand_cust_id = random.randint(1,100)
    post_cust_url = base_url + "/customers"
    new_cust_deets = {"cust_id": rand_cust_id,
        "cust_name": "Symantec",
        "Location": "India"
    }
    resp = requests.post(url=post_cust_url, verify=False, data=new_cust_deets)
    assert resp.status_code == 200

def delete_cust(cust_id):
    if (cust_id <= 0 or cust_id > 100):
        print("Invalid customer ID")
        return
    del_cust_info_url = base_url + "/customers?customer_id=" + cust_id
    resp = requests.delete(url=del_cust_info_url, verify=False)
    if resp.status_code != 200:
        print(f"Customer of customer ID {cust_id} does not exist")
        return
    else:
        print("Deleted customer successfully")