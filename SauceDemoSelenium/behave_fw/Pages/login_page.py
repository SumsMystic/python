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
            error_msg = self.driver.find_element(By.CLASS_NAME, 'error-message-container error').text
            if 'Sorry, this user has been locked out' in error_msg:
                self.proj_logger.info("Locked Out User error is seen")
                return True
            else:
                self.proj_logger.info("Error Message found but incorrect message displayed as: " + error_msg)
                return False
        except NoSuchElementException as E:
            self.proj_logger.info(f"Locked Out User error not found. Exception: {E}")
            return False
        
    def get_website_burger_menu_from_top_left_corner(self):
        logout_options_btn = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        logout_options_btn.click()
        self.proj_logger.info("Found the Logout Options Burger-type Button")

    def reset_website_state(self):
        self.driver.find_element(By.ID, 'reset_sidebar_link').click()
        self.proj_logger.info("Resetting the app state before logging off...")
        
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

    def verify_locked_out_user_error(self):
        assert self.is_locked_out_user_error_seen() == True