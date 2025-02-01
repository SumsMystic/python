'''
Created on Feb 1, 2025

Author: Sumeet Agrawal
'''

from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ProductsDisplayPage:
    
    def __init__(self, context):
        self.context = context
        self.driver = context.driver
        self.expl_wait_obj = context.expl_wait_obj
        self.proj_logger = context.proj_logger

    def handle_browser_alert_for_leaked_passwords(self):
        try:
            self.expl_wait_obj.until(EC.alert_is_present())
            alert_obj = self.driver.switch_to.alert
            alert_text = alert_obj.text
            assert "found in a data breach" in alert_text
            alert_obj.accept()
            self.proj_logger.info("Passwords Leaked Browser Alert dismissed")
        except TimeoutException:
            self.proj_logger.info("Passwords Leaked Browser Alert Not Found. Continue...")
            
    def is_inventory_item_present(self, shopping_item_name):
        all_shopping_items_objs_lst = self.driver.find_elements(By.CLASS_NAME, 'inventory_item')
        for each_shopping_item in all_shopping_items_objs_lst:
            self.proj_logger.debug(f"Current Shopping Test Item {each_shopping_item.text}")
            
            shopping_item_nameobj = each_shopping_item.find_element(By.CLASS_NAME, 'inventory_item_name')
            if shopping_item_name in shopping_item_nameobj.text:
                self.proj_logger.info(f"Specified Test Item {shopping_item_name} Found in the Shopping Inventory")
                return True
            
        self.proj_logger.info(f"Specified Test Item {shopping_item_name} NOT Found in the Shopping Inventory")
        return False
            
    def is_products_page_website_title_seen(self):
        try:
            products_pg_title_text = self.driver.find_element(By.XPATH, '//span[@class="title"]').text
            if 'Products' in products_pg_title_text:
                self.proj_logger.info(f"'Products' text found as Title of the page.")
                return True
            else:
                return False
        except (NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Exception {E} occurred while trying to find the Products page title")
            return False