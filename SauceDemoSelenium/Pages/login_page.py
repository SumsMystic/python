'''
Created on Jan 20, 2025

@author: Sumeet Agrawal
'''


#import pytest
from selenium.webdriver.common.by import *


class LoginPage:
  
    def Get_User_Name_TextBox(self):
        user_name_txt_box = self.driver.find_element(By.ID, 'user-name')
        user_name_txt_box.click()
        user_name_txt_box.clear()
        self.proj_logger.info("\n")
        self.proj_logger.info("Successfully found the Username textbox")
        return user_name_txt_box
        
    def Get_Password_TextBox(self):
        passwd_txt_box = self.driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')
        passwd_txt_box.click()
        passwd_txt_box.clear()
        self.proj_logger.info("Successfully found the Password textbox")
        return passwd_txt_box
    
    def Get_Login_Button(self):
        login_btn = self.driver.find_element(By.XPATH, '//input[@name="login-button"]')
        self.proj_logger.info("Found the Login Button")
        return login_btn
    
    def Is_Locked_Out_User_Error_Seen(self):
        try:
            self.driver.find_element(By.XPATH, '//div/h3[@data-test="error"]')
            return True
        except Exception as E:
            self.proj_logger.info(f"Locked Out User error not found. Exception: {E}")
            return False
        
    def Get_Website_Burger_Menu_From_Top_Left_Corner(self):
        logout_options_btn = self.driver.find_element(By.ID, 'react-burger-menu-btn')
        logout_options_btn.click()
        self.proj_logger.info("Found the Logout Options Burger-type Button")
        
    def Is_Website_Burger_Menu_On_Top_Left_Corner(self):
        try:
            logout_options_btn = self.driver.find_element(By.ID, 'react-burger-menu-btn')
            css_props_of_logout_ops_btn = logout_options_btn.get_attribute('style')
            self.proj_logger.debug(f"Logout Options Button CSS Props: {css_props_of_logout_ops_btn}")
            assert 'left: 0px; top: 0px;' in css_props_of_logout_ops_btn
            self.proj_logger.info("Logout Options Button IS present at Correct location of Top Left Corner")
            return True
        except Exception as E:
            self.proj_logger.info(f"Logout Options Button Not present at Correct location of Top Left Corner! Exception: {E}")
            return False

    def Logout(self):
        logout_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Logout')
        logout_link.click()
        self.proj_logger.info("Logged Out")
    
    
    