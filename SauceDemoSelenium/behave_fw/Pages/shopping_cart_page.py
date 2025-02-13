'''
Created on Fe 1, 2025

Author: Sumeet Agrawal
'''

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class ShoppingCartPage:
    
    def __init__(self, context):
        self.context = context
        self.driver = context.driver
        self.expl_wait_obj = context.expl_wait_obj
        self.proj_logger = context.proj_logger
    
    def _find_shopping_cart_items(self):
        try:
            self.all_shopping_cart_items_lst = self.driver.find_elements(By.XPATH, '//div[@class="cart_item"]')
            return self.all_shopping_cart_items_lst
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Exception {E} occurred while trying to find if the Shopping Cart is empty")
            return None
             
    def is_shopping_cart_empty(self):
        all_shopping_cart_items_lst = self._find_shopping_cart_items()
        if all_shopping_cart_items_lst and len(all_shopping_cart_items_lst) > 0:
            self.proj_logger.debug(f"Shopping Cart is NOT Empty")
            return False
        else:
            self.proj_logger.debug(f"Shopping Cart IS Empty")
            return True
        
    def get_cart_total_bill_value(self):
        total_bill = 0
        all_shopping_cart_items_lst = self._find_shopping_cart_items()
        if all_shopping_cart_items_lst:
            for each_shopping_cart_item_card in all_shopping_cart_items_lst:
                item_price = (each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_price').text)[1:]
                item_price = float(item_price)
                total_bill += item_price
        return total_bill
    
    def remove_all_products_from_cart(self):
        all_shopping_cart_items_lst = self._find_shopping_cart_items()
        if all_shopping_cart_items_lst:
            for each_shopping_cart_item_card in all_shopping_cart_items_lst:
                each_shopping_cart_item_card.find_element(By.XPATH, '//button[contains(text(), "Remove")]').click()
                self.proj_logger.debug(f"Removed {each_shopping_cart_item_card} from the cart")
            
    def get_product_cart_price_and_remove_from_cart(self, item_to_be_removed):
        sleep(5)
        all_shopping_cart_items_lst = self._find_shopping_cart_items()
        if all_shopping_cart_items_lst:
            for each_shopping_cart_item_card in all_shopping_cart_items_lst:
                shopping_cart_item_name_txt = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_name').text
                if item_to_be_removed in shopping_cart_item_name_txt:
                    item_price = (each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_price').text)[1:]
                    item_price = float(item_price)
                    each_shopping_cart_item_card.find_element(By.XPATH, '//button[contains(text(), "Remove")]').click()
                    self.proj_logger.debug(f"Removed {item_to_be_removed} from the cart")
                    return item_price
        return None

            
    def get_specified_product_price_from_cart_page(self, item_name):
        all_shopping_cart_items_lst = self._find_shopping_cart_items()
        for each_shopping_cart_item_card in all_shopping_cart_items_lst: 
            shopping_cart_item_name_txt = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_name').text
            item_price = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_price').text[1:]
            if item_name in shopping_cart_item_name_txt:
                item_price = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_price').text[1:]
                return float(item_price)
            else:
                continue

    def is_item_present_in_shopping_cart(self, item_name):
        self.proj_logger.info(f"Is this item present in the cart?:  {item_name}")
        all_shopping_cart_items_lst = self._find_shopping_cart_items()
        for each_shopping_cart_item_card in all_shopping_cart_items_lst: 
            shopping_cart_item_name_txt = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_name').text
            if str(item_name) in shopping_cart_item_name_txt:
                return True
            else:
                return False
            
    def click_on_continue_shopping_button(self):
        try:
            self.driver.find_element(By.XPATH, '//button[@id="continue-shopping"]').click()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Exception {E} occurred while trying to find Continue Shopping button")
            
    def click_on_checkout_button(self):
        try:
            self.driver.find_element(By.XPATH, '//button[@id="checkout"]').click()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Exception {E} occurred while trying to find Checkout button")
            
    def get_number_of_shopping_cart_items(self):
        
        all_shopping_cart_items_lst = self._find_shopping_cart_items()
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