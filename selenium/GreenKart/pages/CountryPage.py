'''
Created on May 16, 2024

@author: Sumeet Agrawal
'''

from selenium.webdriver.common.by import By
#from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

class CountryPg:
    
    country_selectbox_locator = (By.XPATH, "//Select")
    condtns_agree_checkbox_locator = (By.XPATH, "//input[@type='checkbox']")
    proceed_btn_locator = (By.XPATH, "//button[text()='Proceed']")
    
    
    ajax_load_sleep = 2
    explicit_wait_timeout = 15
    
    
    def __init__(self, drvobj_from_calling_testcase, loggr):
        self.driver = drvobj_from_calling_testcase
        self.expl_wait = WebDriverWait(driver=self.driver, timeout=CountryPg.explicit_wait_timeout)
        self.logr = loggr      
    
    
    def select_country_for_delivery(self, country_str):
        """
            returns a list of 'total' column elements
        """
        try:
            country_select_box = Select(self.driver.find_element(*CountryPg.country_selectbox_locator))
            country_select_box.select_by_visible_text(country_str)
        except Exception as e:
            self.driver.save_screenshot('..//screenshots//CountryNotFound.jpg')
            self.logr.critical("Provided Country Not Found in the Dropdown" + str(e))
            
    def click_checkbox_to_agree_conditions(self):
        try:
            agree_chkbox = self.driver.find_element(*CountryPg.condtns_agree_checkbox_locator)
            agree_chkbox.click()
            return agree_chkbox
        except Exception as e:
            self.driver.save_screenshot('..//screenshots//checkBox.jpg')
            self.logr.critical("Error occurred during agreeing to delivery conditions" + str(e))
            
    def click_proceed_button(self):
        self.driver.find_element(*CountryPg.proceed_btn_locator).click()