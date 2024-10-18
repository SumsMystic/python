'''
Created on May 15, 2024

@author: Sumeet Agrawal
'''

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def suite_setup(request, brwrname):
    """
        Greenkart suite setup
    """
    
    if brwrname == "chrome":
        driver = webdriver.Chrome()
    elif brwrname == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    request.cls.driver_obj = driver
    yield
    driver.close()
    

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="choose browser for Selenium runs: chrome or firefox"
    )


@pytest.fixture(scope="class")
def brwrname(request):
    return request.config.getoption("--browser")