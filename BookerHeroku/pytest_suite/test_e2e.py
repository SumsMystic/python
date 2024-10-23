'''
Created on Sep 18, 2024

@author: Sumeet Agrawal
'''


import requests
import pytest
from random import choice


@pytest.mark.usefixtures("suite_setup")
class Test_BookerHerokuActionsBaseClass:
    # All request.cls.<variables> will be set in 'suite_setup' through conftest.py due to usage of 'fixtures' at scope class level.
    
    @pytest.mark.smoke
    def test_correct_auth(self):
        self.proj_logger.info(" ---- Executing test_correct_auth() ---- ")
        data = {"username": "admin", "password": "password123"}
        resp = requests.post(self.bs_url + "/auth", verify=False, headers=self.json_header, json=data)
        assert resp.status_code == 200
        self.proj_logger.info("Response Status Code: {}".format(resp.status_code))
        
    @pytest.mark.negative
    def test_incorrect_auth(self):
        self.proj_logger.info(" ---- Executing test_incorrect_auth() ---- ")
        data = {"username": "admin", "password": "random"}
        resp = requests.post(self.bs_url + "/auth", verify=False, headers=self.json_header, json=data)
        assert resp.status_code != 200
        self.proj_logger.info("Response Status Code: {}".format(resp.status_code))
    
        
    @pytest.mark.slow
    def test_get_auth_token(self):
        self.proj_logger.info(" ---- Executing  test_get_auth_token ---- ")
        data = {"username": "admin", "password": "password123"}
        resp = requests.post(self.bs_url + "/auth", verify=False, headers=self.json_header, json=data)
        assert resp.status_code == 200
        auth_token_json = resp.json()
        self.auth_token = str(auth_token_json['token'])
        self.proj_logger.info("Token is: {}".format(self.auth_token))

    
    @pytest.mark.slow
    def test_get_all_bookings(self):
        self.proj_logger.info(" ---- Executing  test_get_all_bookings ---- ")
        resp = requests.get(self.bs_url + "/booking", verify=False, headers=self.json_header)
        assert resp.status_code == 200
        self.resp_dict = resp.json()
    
      
    @pytest.mark.negative
    def test_get_details_of_random_bookingID(self):
        self.proj_logger.info(" ---- Executing  test_get_details_of_random_bookingID ---- ")
        books_ids_lst = self.resp_dict.values()
        target_book_id = choice(books_ids_lst)
        self.proj_logger.info("Random Book ID Selected is: {}".format(target_book_id))
        resp = requests.get(self.bs_url + "/booking/" + target_book_id, verify=False, headers=self.json_header)
        assert resp.status_code == 200
        rsp_json = resp.json()
        self.proj_logger.info("Details of the Booking ID: {}".format(rsp_json))
        

    @pytest.mark.slow
    def test_add_book_to_library(self):
        self.proj_logger.info(" ---- Executing  test_add_book_to_library ---- ")
        test_book_json = {
                        "firstname" : "SUMS",
                        "lastname" : "Brown",
                        "totalprice" : 111,
                        "depositpaid" : "true",
                        "bookingdates" : {
                            "checkin" : "2018-01-01",
                            "checkout" : "2019-01-01"
                        },
                        "additionalneeds": "Breakfast"
                    }
        resp = requests.post(self.bs_url + "/booking", verify=False, headers=self.json_header, json=test_book_json)
        assert resp.status_code == 200
        rsp_json = resp.json()
        self.test_book_booking_id = str(rsp_json['bookingid'])
        self.proj_logger.info("New Test Book added with Booking ID: {}".format(self.test_book_booking_id))   
        
    @pytest.mark.slow
    def test_delete_newly_added_book(self):
        self.proj_logger.info(" ---- Executing  test_delete_newly_added_book ---- ")
        cooks = {'token': self.auth_token}
        self.proj_logger.info("cooks: {}".format(cooks))
        self.proj_logger.info("final URL: {}".format(self.bs_url + "/booking/" + self.test_book_booking_id))
        resp = requests.delete(self.bs_url + "/booking/" + self.test_book_booking_id, verify=False, headers=self.json_header, cookies=cooks)
        assert resp.status_code == 200  