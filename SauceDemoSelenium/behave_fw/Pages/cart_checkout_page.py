"""
Created on Feb 1, 2025

Author: Sumeet Agrawal
"""

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC

class CartCheckOutPage:
    
    def __init__(self, context):
        self.context = context
        self.driver = context.driver
        self.expl_wait_obj = context.expl_wait_obj
        self.proj_logger = context.proj_logger

    def validate_checkout_page_title(self):
        try:
            self.expl_wait_obj.until(EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']")))
            page_title_text = self.driver.find_element(By.CLASS_NAME, 'title').text
            if 'Checkout' in page_title_text:
                return True
            else:
                return False
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Exception {E} occurred while trying to find if the Shopping Cart is empty")
            return None
             
    def add_first_name(self, first_name):
        firstname_txtbox = self.expl_wait_obj.until(EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']")))
        firstname_txtbox.clear()
        firstname_txtbox.send_keys(first_name)
        
    def add_last_name(self, last_name):
        lastname_txtbox = self.expl_wait_obj.until(EC.presence_of_element_located((By.XPATH, "//input[@id='last-name']")))
        lastname_txtbox.clear()
        lastname_txtbox.send_keys(last_name)
        
    def add_postal_code(self, postal_code):
        postalcode_txtbox = self.expl_wait_obj.until(EC.presence_of_element_located((By.XPATH, "//input[@id='postal-code']")))
        postalcode_txtbox.clear()
        postalcode_txtbox.send_keys(postal_code)
        
    def click_cancel_button(self):
        try:
            self.driver.find_element(By.XPATH, '//button[@id="cancel"]').click()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.error(f"Exception {E} occurred while trying to click on Cancel from Checkout Page")