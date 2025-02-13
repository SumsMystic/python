'''
Created on Feb 1, 2025

Author: Sumeet Agrawal
'''

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    
    def __init__(self, context):
        self.context = context
        self.driver = context.driver
        self.proj_logger = context.proj_logger

    def get_user_name_textbox(self):
        user_name_txt_box = self.driver.find_element(By.ID, 'user-name')
        user_name_txt_box.click()
        user_name_txt_box.clear()
        self.proj_logger.info("\n")
        self.proj_logger.info("Successfully found the Username textbox")
        return user_name_txt_box
        
    def get_password_textbox(self):
        passwd_txt_box = self.driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
        passwd_txt_box.click()
        passwd_txt_box.clear()
        self.proj_logger.info("Successfully found the Password textbox")
        return passwd_txt_box
    
    def get_login_button(self):
        login_btn = self.driver.find_element(By.XPATH, '//input[@name="login-button"]')
        self.proj_logger.info("Found the Login Button")
        return login_btn
    
    def is_locked_out_user_error_seen(self):
        try:
            self.driver.find_element(By.XPATH, '//div/h3[@data-test="error"]')
            return True
        except NoSuchElementException as E:
            self.proj_logger.info(f"Locked Out User error not found. Exception: {E}")
            return False
        
    def get_website_burger_menu_from_top_left_corner(self):
        logout_options_btn = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        logout_options_btn.click()
        self.proj_logger.info("Found the Logout Options Burger-type Button")
        
    def is_website_burger_menu_on_top_left_corner(self):
        try:
            self.driver.find_element(By.ID, 'react-burger-menu-btn')
            return True
        except NoSuchElementException as E:
            self.proj_logger.info(f"Burger menu not found. Exception: {E}")
            return False
        
    def logout(self):
        logout_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Logout')
        logout_link.click()
        self.proj_logger.info("Logged Out")