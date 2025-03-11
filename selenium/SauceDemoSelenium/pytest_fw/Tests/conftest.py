'''
Created on Jan 20, 2025

@author: Sumeet Agrawal
'''


import pytest
import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="class")
def login_tests_suite_setup(request):
    """
        BookerHeroku suite setup
    """
    request.cls.proj_logger = logging.getLogger('SauceDemoSelenium')
    request.cls.proj_logger.info("\n")
    request.cls.proj_logger.info("**************  START NEW RUN  **************")
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get('https://www.saucedemo.com')
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(5)
    request.cls.driver.expl_wait_obj = WebDriverWait(request.cls.driver, 10)
    yield
    request.cls.driver.close()


@pytest.fixture(scope="class")
def before_each_test(request):
    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get('https://www.saucedemo.com')
    request.cls.driver.maximize_window()
    request.cls.driver.implicitly_wait(5)
    yield
    request.cls.driver.close()
    request.cls.proj_logger.info("Closed the Browser session and hence this TEST session too!")