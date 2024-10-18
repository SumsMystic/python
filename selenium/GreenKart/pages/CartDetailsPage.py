'''
Created on May 16, 2024

@author: Sumeet Agrawal
'''

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartDetailsPg:
    
    cart_pg_totl_colm_locator = (By.XPATH, "//tr/td[5]")
    site_basket_total = (By.XPATH, "//span[@class='totAmt']")
    promocode_txtbox_locator = (By.XPATH, "//input[@class='promoCode']")
    promocode_apply_btn_locator = (By.XPATH, "//button[text()='Apply']")
    discount_perct_locator = (By.XPATH, "//span[@class='discountPerc']")
    place_order_btn_locator = (By.XPATH, "//button[text()='Place Order']")
    cntry_label_locator = (By.XPATH, "//label[text()='Choose Country']")
    disc_msg_txt_span = (By.XPATH, "//span[@class='promoInfo']")

    
    ajax_load_sleep = 2
    explicit_wait_timeout = 15
    
    
    def __init__(self, drvobj_from_calling_testcase, loggr):
        self.driver = drvobj_from_calling_testcase
        self.expl_wait = WebDriverWait(driver=self.driver, timeout=CartDetailsPg.explicit_wait_timeout)
        self.logr = loggr      
    
    
    def get_value_from_total_colm_in_table(self):
        """
            returns a list of 'total' column elements
        """
        try:
            return self.driver.find_elements(*CartDetailsPg.cart_pg_totl_colm_locator)
            
        except Exception as e:
            self.driver.save_screenshot('..//screenshots//totalColElemsNotFound.jpg')
            self.logr.critical("Total Column Elements Not Found" + str(e))
            return
        
    def get_website_basket_total(self):
        return int(self.driver.find_element(*CartDetailsPg.site_basket_total).text)
    
    def wait_for_discount_msg(self):
        try:
            self.expl_wait.until(EC.visibility_of_element_located((CartDetailsPg.disc_msg_txt_span)), "Code Applied Successfully")
        except Exception as e:
            self.logr.critical("Discount Message didn't appear even after {} seconds. Exception: {}".format(CartDetailsPg.explicit_wait_timeout, str(e)))
            
    def apply_valid_promocode(self):
        try:
            self.driver.find_element(*CartDetailsPg.promocode_txtbox_locator).send_keys("rahulshettyacademy")
            sleep(5)
            self.driver.find_element(*CartDetailsPg.promocode_apply_btn_locator).click()
        except Exception as e:
            self.logr.critical("Exception when applying Promocode: {}".format(CartDetailsPg.explicit_wait_timeout, str(e)))
            
    def apply_invalid_promocode(self):
        try:
            self.driver.find_element(*CartDetailsPg.promocode_txtbox_locator).send_keys("rahulacademy")
            self.driver.find_element(*CartDetailsPg.promocode_apply_btn_locator).click()
        except Exception as e:
            self.logr.critical("Exception when applying Promocode: {}".format(CartDetailsPg.explicit_wait_timeout, str(e)))
            
    def get_discount_percent(self):
        return self.driver.find_element(*CartDetailsPg.discount_perct_locator).text
    
    def click_place_order(self):
        try:
            self.driver.find_element(*CartDetailsPg.place_order_btn_locator).click()
            self.expl_wait.until(EC.visibility_of_element_located((CartDetailsPg.cntry_label_locator)), "Next page loaded Successfully")
        except Exception as e:
            self.logr.critical("Couldn't click on 'Place Order': {}".format(CartDetailsPg.explicit_wait_timeout, str(e)))    