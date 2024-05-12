'''
Created on May 12, 2024

@author: Sumeet Agrawal
'''

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def suite_setup(request):
    driver_obj = webdriver.Chrome()
    driver_obj.maximize_window()
    driver_obj.implicitly_wait(5)
    driver_obj.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    request.cls.driver = driver_obj