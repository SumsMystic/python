'''
Created on Fe 1, 2025

Author: Sumeet Agrawal
'''

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC

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
        all_shopping_cart_items_lst = self._find_shopping_cart_items()
        if all_shopping_cart_items_lst:
            for each_shopping_cart_item_card in all_shopping_cart_items_lst:
                item_name = each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_name').text
                if item_name == item_to_be_removed:
                    item_price = (each_shopping_cart_item_card.find_element(By.CLASS_NAME, 'inventory_item_price').text)[1:]
                    item_price = float(item_price)
                    each_shopping_cart_item_card.find_element(By.XPATH, '//button[contains(text(), "Remove")]').click()
                    self.proj_logger.debug(f"Removed {item_name} from the cart")
                    return item_price
        return None