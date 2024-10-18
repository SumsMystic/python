'''
Created on May 15, 2024

@author: Sumeet Agrawal
'''


from utils.base import GreenKartBaseClass
from pages.GreenKartHomePage import GreenKartHomePg
from pages.CartDetailsPage import CartDetailsPg
from pages.CountryPage import CountryPg
import time
#from selenium.webdriver.common.by import By

class Test_GreenKartFirst(GreenKartBaseClass):
    def test_e2e_1(self):
        #self.driver_obj = self.driver
        logger_obj = self.get_logger()
        logger_obj.info("Website loaded")
        
        # Initialize the Page Objects
        HomePgObj = GreenKartHomePg(self.driver_obj, logger_obj)
        CartPgObj = CartDetailsPg(self.driver_obj, logger_obj)
        CountryPgObj = CountryPg(self.driver_obj, logger_obj)
        
        
        HomePgObj.search_veggies_in_homepage("be")
        logger_obj.info("Website search box found")
        
        veggie_cards = HomePgObj.get_veggie_cards()
        logger_obj.info("Veggie cards found!!")
        
        for _ in veggie_cards:
            HomePgObj.add_veggie_to_cart()
        
        logger_obj.info("All filtered Veggies added to the cart")
        
        #Click on the cart
        HomePgObj.click_to_expand_cart()
        
        HomePgObj.checkout_cart()
        logger_obj.info("Checking out with veggies in the cart")
        
        # Get total amount in each row in table
        amounts_lst = CartPgObj.get_value_from_total_colm_in_table()
        # First value in the list is of the table header - 'total' title in this case. Hence ignore that. 
        final_amts_lst = amounts_lst[1:]
        
        evaluated_basket_total = 0
        for each_total_amt in final_amts_lst:
            evaluated_basket_total += int(each_total_amt.text)

                    
        website_basket_total = CartPgObj.get_website_basket_total()
        assert int(website_basket_total) == evaluated_basket_total
        logger_obj.info("Assertion Successful. Calculated basket total equal to the one shown on website")
        time.sleep(5)
        
        # Now apply the Promocode
        CartPgObj.apply_valid_promocode()
        # self.driver_obj.find_element(By.XPATH, "//button[text()='Apply']").click()        
        CartPgObj.wait_for_discount_msg()
        
        discount = CartPgObj.get_discount_percent()
        assert discount == '10%'
        logger_obj.info("Promocode applied successfully")
        
        CartPgObj.click_place_order()
        time.sleep(5)
        # Select Country
        
        CountryPgObj.select_country_for_delivery("India")
        logger_obj.info("Country selected")
        
        agree_box = CountryPgObj.click_checkbox_to_agree_conditions()
        logger_obj.info("Conditions accepted")
        
        assert agree_box.is_enabled()
        
        CountryPgObj.click_proceed_button()
        logger_obj.info("Test case completed successfully")
