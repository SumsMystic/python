'''
Created on Jan 31, 2025

@author: Sumeet Agrawal
'''

from selenium.webdriver.common.by import *
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class ShoppingCartPage:
    
    def _Find_Shopping_Cart_Items(self):
        try:
            self.all_shopping_cart_items_lst = self.driver.find_elements(By.XPATH, '//div[@class="cart_item"]')
            return self.all_shopping_cart_items_lst
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Exception {E} occurred while trying to find if the Shopping Cart is empty")
            # We'll return 'False' so that this exception would cause the test case to fail. This is just for trial for now.
            return None
             
    def Is_Shopping_Cart_Empty(self):
        all_shopping_cart_items_lst = self._Find_Shopping_Cart_Items()
        if len(all_shopping_cart_items_lst) > 0:
            self.proj_logger.debug(f"Shopping Cart is NOT Empty")
            return False
        else:
            self.proj_logger.debug(f"Shopping Cart IS Empty")
            return True
        
    def Get_Cart_Total_Bill_Value(self):
        total_bill = 0
        all_shopping_cart_items_lst = self._Find_Shopping_Cart_Items()
        for each_shopping_cart_item_card in all_shopping_cart_items_lst:
            item_price = (each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_price').text)[1:]
            item_price = float(item_price)
            total_bill += item_price
        return total_bill
    
    def Remove_All_Products_From_Cart(self):
        all_shopping_cart_items_lst = self._Find_Shopping_Cart_Items()
        for each_shopping_cart_item_card in all_shopping_cart_items_lst:
            each_shopping_cart_item_card.find_element(By.XPATH, '//button[contains(text(), "Remove")]')
            self.proj_logger.debug(f"Removed {each_shopping_cart_item_card} from the cart")
            
    def Get_Product_Cart_Price_And_Remove_From_Cart(self, item_to_be_removed):
        sleep(5)
        all_shopping_cart_items_lst = self._Find_Shopping_Cart_Items()
        for each_shopping_cart_item_card in all_shopping_cart_items_lst: 
            shopping_cart_item_name_txt = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_name').text
            self.proj_logger.info(f"shopping_cart_item_name_txt {shopping_cart_item_name_txt}")
            if item_to_be_removed in shopping_cart_item_name_txt:
                item_price = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_price').text[1:]
                each_shopping_cart_item_card.find_element(By.XPATH, './/button[contains(text(), "Remove")]').click()
                self.proj_logger.info(f"Removed {item_to_be_removed} from the cart")
                return float(item_price)
                break
            else:
                continue
            
    def Get_All_Cart_Products_Total_Price(self):
        cart_total = 0
        all_shopping_cart_items_lst = self._Find_Shopping_Cart_Items()
        for each_shopping_cart_item_card in all_shopping_cart_items_lst: 
            item_price = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_price').text[1:]
            cart_total += float(item_price)
            self.proj_logger.info(f"cart_total: {cart_total}")
        return cart_total
            
    def Get_Specified_Product_Price_From_Cart_Page(self, item_name):
        all_shopping_cart_items_lst = self._Find_Shopping_Cart_Items()
        for each_shopping_cart_item_card in all_shopping_cart_items_lst: 
            shopping_cart_item_name_txt = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_name').text
            item_price = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_price').text[1:]
            if item_name in shopping_cart_item_name_txt:
                item_price = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_price').text[1:]
                return float(item_price)
                break
            else:
                continue
            
    def Click_On_Continue_Shopping_Button(self):
        try:
            self.driver.find_element(By.XPATH, '//button[@id="continue-shopping"]').click()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Exception {E} occurred while trying to find Continue Shopping button")
            
    def Click_On_Checkout_Button(self):
        try:
            self.driver.find_element(By.XPATH, '//button[@id="checkout"]').click()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Exception {E} occurred while trying to find Checkout button")
            
    def Get_Number_Of_Shopping_Cart_Items(self):
        
        all_shopping_cart_items_lst = self._Find_Shopping_Cart_Items()
        if all_shopping_cart_items_lst:
            return int(len(all_shopping_cart_items_lst))
        else:
            self.proj_logger.info("Exception occurred while trying to find if the Shopping Cart is empty")
            return int(0)
        
    def Is_Shopping_Cart_Visible(self):
        try:
            self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
            self.proj_logger.debug(f"Found the Shopping Cart to view Details")
            return True
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Failed to find the Shopping Cart. Exception {E} occurred.")
            return False
        
    def Get_No_Of_Items_From_Shopping_Cart_Icon(self):
        try:
            shopped_items_num = self.driver.find_element(By.CLASS_NAME, 'shopping_cart_badge')
            self.proj_logger.debug(f"Found {shopped_items_num} number of items in the Shopping Cart")
            return int(shopped_items_num)
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Failed to find the Shopping Cart. Exception {E} occurred.")
            return int(0) 
