'''
Created on Jan 21, 2025

@author: Sumeet Agrawal
'''


import pytest
from Pages.login_page import LoginPage
from Pages.product_display_page import ProductsDisplayPage


class Test_StdUser_Shopping_Flows(LoginPage, ProductsDisplayPage):
    
    @pytest.fixture(autouse=True)
    def test_setup(self):
        self.Get_User_Name_TextBox().send_keys('standard_user')
        self.Get_Password_TextBox().send_keys('secret_sauce')
        self.Get_Login_Button().click()
        self.Handle_Browser_Alert_For_Leaked_Passwords()
        yield
        self.Is_Website_Burger_Menu_On_Top_Left_Corner()
        self.Get_Website_Burger_Menu_From_Top_Left_Corner()
        self.Logout()
    
    
    @pytest.mark.smoke
    # @pytest.mark.usefixtures('login_tests_suite_setup')
    def test_add_backpack_to_cart(self, login_tests_suite_setup):
        item_price = self.Add_Item_To_Cart_And_Get_Its_Price('Sauce Labs Backpack')
        self.proj_logger.info(f"Price of 'Sauce Labs Backpack' is {item_price} and has been added to the cart")
        
    
    @pytest.mark.smoke
    # @pytest.mark.usefixtures('login_tests_suite_setup')
    def test_add_fleece_jacket_to_cart(self, login_tests_suite_setup):
        item_price = self.Add_Item_To_Cart_And_Get_Its_Price('Sauce Labs Fleece Jacket')
        self.proj_logger.info(f"Price of 'Sauce Labs Fleece Jacket' is {item_price} and has been added to the cart")
