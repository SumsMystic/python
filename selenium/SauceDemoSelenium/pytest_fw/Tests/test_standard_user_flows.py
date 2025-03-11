'''
Created on Jan 21, 2025

@author: Sumeet Agrawal
'''


import pytest
from pytest_fw.Pages.login_page import LoginPage
from pytest_fw.Pages.product_display_page import ProductsDisplayPage
from pytest_fw.Pages.shopping_cart_page import ShoppingCartPage
from pytest_fw.Pages.cart_checkout_page import CartCheckOutPage
from time import sleep


class Test_StdUser_Shopping_Flows(LoginPage, ProductsDisplayPage, ShoppingCartPage, CartCheckOutPage):
    
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
    @pytest.mark.usefixtures('login_tests_suite_setup')
    @pytest.mark.run(number='1')
    def test_01_add_backpack_to_cart(self):
        backpack_item_price = self.Add_Item_To_Cart_And_Get_Its_Price('Sauce Labs Backpack')
        # self.cart_total_price += backpack_item_price
        self.proj_logger.info(f"Price of 'Sauce Labs Backpack' is {backpack_item_price} and has been added to the cart")
        assert self.Is_Shopped_Inventory_Item_Now_Has_Remove_Button('Sauce Labs Backpack')
        
    
    @pytest.mark.smoke
    @pytest.mark.usefixtures('login_tests_suite_setup')
    @pytest.mark.run(number='2')
    def test_02_add_fleece_jacket_to_cart(self):
        fleece_jacket_item_price = self.Add_Item_To_Cart_And_Get_Its_Price('Sauce Labs Fleece Jacket')
        # self.cart_total_price += fleece_jacket_item_price
        
        #If required, item_price assertion can also be added later. 
        self.proj_logger.info(f"Price of 'Sauce Labs Fleece Jacket' is {fleece_jacket_item_price} and has been added to the cart")
        assert self.Is_Shopped_Inventory_Item_Now_Has_Remove_Button('Sauce Labs Fleece Jacket')
        shopping_items_number = self.Get_No_Of_Items_From_Shopping_Cart_Icon()
        assert shopping_items_number == 2
        self.Click_On_Shopping_Cart_To_View_Cart_Contents()
        shopping_cart_items = self.Get_Number_Of_Shopping_Cart_Items()
        assert shopping_items_number == shopping_cart_items
        
        
    @pytest.mark.smoke
    @pytest.mark.usefixtures('login_tests_suite_setup')
    @pytest.mark.run(number='3')
    def test_03_remove_fleece_jacket_and_add_onesie_and_checkout(self):
        self.Click_On_Shopping_Cart_To_View_Cart_Contents()
        assert self.Is_Shopping_Cart_Empty() == False
        self.cart_total_price = self.Get_All_Cart_Products_Total_Price()
        fleece_jacket_item_price = self.Get_Product_Cart_Price_And_Remove_From_Cart('Sauce Labs Fleece Jacket')
        self.cart_total_price -= fleece_jacket_item_price
        shopping_cart_items = self.Get_Number_Of_Shopping_Cart_Items()
        sleep(5)
        assert shopping_cart_items == 1
        self.Click_On_Continue_Shopping_Button()
        onesie_item_price = self.Add_Item_To_Cart_And_Get_Its_Price('Sauce Labs Onesie')
        self.proj_logger.info(f"Price of 'Sauce Labs Onesie' is {onesie_item_price} and has been added to the cart")
        self.cart_total_price += onesie_item_price
        assert self.Is_Shopped_Inventory_Item_Now_Has_Remove_Button('Sauce Labs Onesie')
        shopping_items_number = self.Get_No_Of_Items_From_Shopping_Cart_Icon()
        assert shopping_items_number == 2
        self.Click_On_Shopping_Cart_To_View_Cart_Contents()
        shopping_cart_items = self.Get_Number_Of_Shopping_Cart_Items()
        assert shopping_items_number == shopping_cart_items
        cart_calculated_total_bill = self.Get_Cart_Total_Bill_Value()
        self.cart_total_price = round(self.cart_total_price, 2)
        assert self.cart_total_price == cart_calculated_total_bill
        self.Click_On_Checkout_Button()
        self.Add_First_Name('standard')
        self.Add_Last_Name('user')
        self.Add_Postal_Code('420586')
        self.Click_Continue_Button()
        billing_page_subtotal = self.Get_Item_Total_Price_From_Final_Billing_Page()
        assert self.cart_total_price == billing_page_subtotal
        self.Click_Finish_Button()
