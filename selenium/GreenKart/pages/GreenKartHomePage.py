'''
Created on May 16, 2024

@author: Sumeet Agrawal
'''

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GreenKartHomePg:
    
    homepage_search_box = (By.XPATH, "//input[@type='search']")
    veggie_cards_locator = (By.XPATH, "//div[@class='product']")
    add_to_cart_btn_locator = (By.XPATH, "//button[text()='ADD TO CART']")
    home_pg_cart_icon_locator = (By.CLASS_NAME, "cart-icon")
    checkout_btn_locator = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    promocode_apply_btn_locator = (By.XPATH, "//button[text()='Apply']")
    
    ajax_load_sleep = 2
    explicit_wait_timeout = 15
    
    
    def __init__(self, drvobj_from_calling_testcase, loggr):
        self.driver = drvobj_from_calling_testcase
        self.expl_wait = WebDriverWait(driver=self.driver, timeout=GreenKartHomePg.explicit_wait_timeout)
        self.logr = loggr      
    
    
    def search_veggies_in_homepage(self, search_string):
        try:
            search_box = self.driver.find_element(*GreenKartHomePg.homepage_search_box)
        except Exception as e:
            self.driver.save_screenshot('..//screenshots//searchBoxNotFound.jpg')
            self.logr.critical("Search Box Not Found" + str(e))
            return
        search_box.send_keys(search_string)
        sleep(GreenKartHomePg.ajax_load_sleep)
        
    def get_veggie_cards(self):
        try:
            veggie_cards = self.driver.find_elements(*GreenKartHomePg.veggie_cards_locator)
            if len(veggie_cards) > 0:
                return veggie_cards
            else:
                self.logr.error("0 veggie cards found from search")
        except Exception as e:
            self.logr.critical("Veggie Cards locator error. Exception: " + str(e))       
        
    def add_veggie_to_cart(self):
        try:
            self.driver.find_element(*GreenKartHomePg.add_to_cart_btn_locator).click()
            
        except Exception as e:
            self.driver.save_screenshot('..//screenshots//veggies_cart_btns_not_found.jpg')
            self.logr.critical("Unable to add the veggie to the cart! Exception: " + str(e))
            
    def click_to_expand_cart(self):
        try:
            self.driver.find_element(*GreenKartHomePg.home_pg_cart_icon_locator).click()
        except Exception as e:
            self.logr.critical("Unable to view details of the cart. Exception: " + str(e))
            
    def is_cart_empty(self):
        try:
            button_cls = self.driver.find_element(*GreenKartHomePg.checkout_btn_locator).get_attribute("class")
            if button_cls == 'disabled':
                return True
            else:
                return False
        except Exception as e:
            self.logr.critical("Unable to get attributes of the cart 'Proceed' button. Exception: " + str(e))
            
    def checkout_cart(self):
        try:
            self.driver.find_element(*GreenKartHomePg.checkout_btn_locator).click()
            self.expl_wait.until(EC.visibility_of_element_located((GreenKartHomePg.promocode_apply_btn_locator)), "Checking Out the Cart Successfully")
        except Exception as e:
            self.logr.critical("Unable to proceed to checkout. Exception: " + str(e))
