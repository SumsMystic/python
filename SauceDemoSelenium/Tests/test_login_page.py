'''
Created on Jan 20, 2025

@author: Sumeet Agrawal
'''


import pytest
from Pages.login_page import LoginPage
# from selenium import webdriver

@pytest.mark.usefixtures('login_tests_suite_setup')
class Test_LoginPage(LoginPage):
    
    @pytest.mark.negative
    def test_blocked_user_login(self):
        self.Get_User_Name_TextBox().send_keys('locked_out_user')
        self.Get_Password_TextBox().send_keys('secret_sauce')
        self.Get_Login_Button().click()
        assert self.Is_Locked_Out_User_Error_Seen()
        self.proj_logger.info("Executed the negative test case of blocked user login")
        
    """    
    @pytest.mark.negative
    def test_problem_user_login(self):
        self.Get_User_Name_TextBox().send_keys('locked_out_user')
        self.Get_Password_TextBox().send_keys('secret_sauce')
        self.Get_Login_Button().click()
        assert self.isLockedOutUserErrorSeen()
        self.proj_logger.info("Executed the negative test case of blocked user login")
    
        
    @pytest.mark.negative
    def test_performance_glitch_user_login(self):
        self.Get_User_Name_TextBox().send_keys('locked_out_user')
        self.Get_Password_TextBox().send_keys('secret_sauce')
        self.Get_Login_Button().click()
        assert self.isLockedOutUserErrorSeen()
        self.proj_logger.info("Executed the negative test case of blocked user login")
    
        
    @pytest.mark.negative
    def test_error_user_login(self):
        self.Get_User_Name_TextBox().send_keys('locked_out_user')
        self.Get_Password_TextBox().send_keys('secret_sauce')
        self.Get_Login_Button().click()
        assert self.isLockedOutUserErrorSeen()
        self.proj_logger.info("Executed the negative test case of blocked user login")
    
       
    @pytest.mark.negative
    def test_visual_user_login(self):
        self.Get_User_Name_TextBox().send_keys('locked_out_user')
        self.Get_Password_TextBox().send_keys('secret_sauce')
        self.Get_Login_Button().click()
        assert self.isLockedOutUserErrorSeen()
        self.proj_logger.info("Executed the negative test case of blocked user login")

     
    @pytest.mark.negative
    def test_valid_user_login(self):
        self.Get_User_Name_TextBox().send_keys('standard_user')
        self.Get_Password_TextBox().send_keys('secret_sauce')
        self.Get_Login_Button().click()
        self.proj_logger.info("Executed the valid user login scenario for SauceDemo website!")
        
    """
    