'''
Created on Jan 31, 2025

@author: Sumeet Agrawal
'''



from selenium.webdriver.common.by import *
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC


class CartCheckOutPage:
    
    def Validate_Checkout_Page_Title(self):
        try:
            self.expl_wait_obj.until(EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']")))
            page_title_text = self.driver.find_element(By.CLASS_NAME, 'title').text
            if 'Checkout' in page_title_text:
                return True
            else:
                return False
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Exception {E} occurred while trying to find if the Shopping Cart is empty")
            # We'll return 'False' so that this exception would cause the test case to fail. This is just for trial for now.
            return None
             
    def Add_First_Name(self, first_name):
        firstname_txtbox = self.expl_wait_obj.until(EC.presence_of_element_located((By.XPATH, "//input[@id='first-name']")))
        firstname_txtbox.clear()
        firstname_txtbox.send_keys(first_name)
        
    def Add_Last_Name(self, last_name):
        lastname_txtbox = self.expl_wait_obj.until(EC.presence_of_element_located((By.XPATH, "//input[@id='last-name']")))
        lastname_txtbox.clear()
        lastname_txtbox.send_keys(last_name)
        
    def Add_Postal_Code(self, postal_code):
        postalcode_txtbox = self.expl_wait_obj.until(EC.presence_of_element_located((By.XPATH, "//input[@id='postal-code']")))
        postalcode_txtbox.clear()
        postalcode_txtbox.send_keys(postal_code)
        
    def Click_Cancel_Button(self):
        try:
            self.driver.find_element(By.XPATH, '//button[@id="cancel"]').click()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.error(f"Exception {E} occurred while trying to click on Cancel from Checkout Page")
            
    def Click_Continue_Button(self):
        try:
            self.driver.find_element(By.XPATH, '//input[@id="continue"]').click()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.error(f"Exception {E} occurred while trying to click on Continue from Checkout Page")
            
    def Get_Item_Total_Price_From_Final_Billing_Page(self):
        try:
            self.expl_wait_obj.until(EC.presence_of_element_located((By.CLASS_NAME, 'summary_info_label'))) 
            cart_subtotal_txt = self.expl_wait_obj.until(EC.presence_of_element_located((By.CLASS_NAME, 'summary_subtotal_label'))).text
            cart_subtotal_int = float(cart_subtotal_txt.split('$')[1])
            return cart_subtotal_int
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.info(f"Exception {E} occurred while trying to find if the Shopping Cart is empty")
            # We'll return 'False' so that this exception would cause the test case to fail. This is just for trial for now.
            return float(0)
        
    def Click_Finish_Button(self):
        try:
            self.driver.find_element(By.XPATH, '//button[@id="finish"]').click()
        except (TimeoutException, NoSuchElementException, ElementNotVisibleException) as E:
            self.proj_logger.error(f"Exception {E} occurred while trying to click on Finish from Checkout Overview Page")