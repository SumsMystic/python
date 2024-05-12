'''
Created on May 6, 2024

@author: Sumeet Agrawal
'''


import pytest
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from pytest_fw.GreenkartLogger import Greenkart_Logging
from pytest_fw.pytest_fixtures import suite_setup


# @pytest.mark.usefixtures(suite_setup)

class Test_GreenKartFirst(suite_setup):
    def test_e2e(self):
        driver_obj = self.driver
        logger_obj = Greenkart_Logging().get_logger(__name__)
        expl_wait = WebDriverWait(driver=driver_obj, timeout=15)
        logger_obj.info("Website loaded")
        
        driver_obj.find_element(By.XPATH, "//input[@type='search']").send_keys("be")
        time.sleep(5)
        logger_obj.info("Website search box found")
        
        veggie_cards = driver_obj.find_elements(By.XPATH, "//div[@class='product']")
        logger_obj.info("Multiple veggie cards found!!")
        
        for each_veggie in veggie_cards:
            driver_obj.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()
        
        logger_obj.info("Veggies added to cart")
        
        #Click on the cart
        driver_obj.find_element(By.CLASS_NAME, "cart-icon").click()
        
        driver_obj.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
        time.sleep(5)
        logger_obj.info("Checking out with veggies in the cart")
        
        # Get total amount in each row in table
        amounts_lst = driver_obj.find_elements(By.XPATH, "//tr/td[5]")
        final_amts_lst = amounts_lst[1:]
        
        basket_total = 0
        for each_total_amt in final_amts_lst:
            basket_total += int(each_total_amt.text)
            
        website_basket_total = driver_obj.find_element(By.XPATH, "//span[@class='totAmt']").text
        assert int(website_basket_total) == basket_total
        logger_obj.info("Assertion Successful. Calculated basket total equal to the one shown on website")
        
        # Now apply the Promocode
        driver_obj.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
        driver_obj.find_element(By.XPATH, "//button[text()='Apply']").click()
        
        expl_wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='promoInfo']")), "Code Applied Successfully")
        discount = driver_obj.find_element(By.XPATH, "//span[@class='discountPerc']").text
        assert discount == '10%'
        logger_obj.info("Promocode applied successfully")
        
        driver_obj.find_element(By.XPATH, "//button[text()='Place Order']").click()
        time.sleep(5)
        # Select Country
        drop_down_obj = Select(driver_obj.find_element(By.XPATH, "//Select"))
        drop_down_obj.select_by_visible_text("India")
        logger_obj.info("Country selected")
        
        agree_box = driver_obj.find_element(By.XPATH, "//input[@type='checkbox']")
        agree_box.click()
        logger_obj.info("Conditions accepted")
        
        assert agree_box.is_enabled()
        
        driver_obj.find_element(By.XPATH, "//button[text()='Proceed']").click()
        logger_obj.info("Test case completed successfully")
