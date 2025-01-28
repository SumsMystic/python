'''
Created on Jan 21, 2025

@author: Sumeet Agrawal
'''

# import pytest
from selenium.webdriver.common.by import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



class ProductsDisplayPage:
  
    def Handle_Browser_Alert_For_Leaked_Passwords(self):
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_obj = self.driver.switch_to.alert()
            alert_text = alert_obj.text
            assert "found in a data breach" in alert_text
            alert_obj.accept()
            self.proj_logger.info("Passwords Leaked Browser Alert dismissed")
        except TimeoutException:
            self.proj_logger.info("Passwords Leaked Browser Alert Not Found. Continue...")
            
    def Is_Inventory_Item_Present(self, shopping_item_name):
        all_shopping_items_objs_lst = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')
        for each_shopping_item in all_shopping_items_objs_lst:
            self.proj_logger.debug(f"Current Shopping Test Item {each_shopping_item.text}")
            
            shopping_item_nameobj = each_shopping_item.find_element(By.CLASS_NAME, 'inventory_item_name')
            if shopping_item_name in shopping_item_nameobj.text:
                self.proj_logger.info(f"Specified Test Item {shopping_item_name} Found in the Shopping Inventory")
                return True
            
            else:
                self.proj_logger.info(f"Specified Test Item {shopping_item_name} NOT Found in the Shopping Inventory")
                return False
            
    def Add_Item_To_Cart_And_Get_Its_Price(self, shopping_item_name):
        try:
            # First check if at least 1 inventory item is present and then proceed.
            self.driver.find_element(By.CLASS_NAME, 'inventory_item')
        
            all_shopping_items_objs_lst = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')
            for each_shopping_item in all_shopping_items_objs_lst:
                self.proj_logger.debug(f"Current Shopping Test Item {each_shopping_item.text}")
                
                shopping_item_nameobj = each_shopping_item.find_element(By.CLASS_NAME, 'inventory_item_name')
                if shopping_item_name in shopping_item_nameobj.text:
                    self.proj_logger.info(f"Specified Test Item {shopping_item_name} Found in the Shopping Inventory")
                    shopping_item_price = each_shopping_item.find_element(By.CLASS_NAME, 'inventory_item_price').text
                    each_shopping_item.find_element(By.XPATH, './/button[contains(text(),"Add to cart")]').click()
                    sleep(5)
                    return shopping_item_price
                else:
                    self.proj_logger.info(f"Not able to find the Specified Test Item {shopping_item_name} in the item cards yet. Continuing...")
        except Exception as E:
            self.proj_logger.info(f"Perhaps not present on the products page. Exception {E} occurred.")
        