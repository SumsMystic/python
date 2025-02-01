"""
Created on Feb 1, 2025

Author: Sumeet Agrawal
"""

import logging
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from behave_fw.Pages.login_page import LoginPage
from behave_fw.Pages.product_display_page import ProductsDisplayPage
from behave_fw.Pages.shopping_cart_page import ShoppingCartPage
from behave_fw.Pages.cart_checkout_page import CartCheckOutPage

def before_all(context):
    """
    Setup that runs before the entire test suite
    """
    context.proj_logger = logging.getLogger('SauceDemoSelenium')
    context.proj_logger.info("\n")
    context.proj_logger.info("**************  START NEW RUN  **************")
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com')
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.expl_wait_obj = WebDriverWait(context.driver, 10)
    context.products_page = ProductsDisplayPage(context)
    context.shopping_cart_page = ShoppingCartPage(context)
    context.cart_checkout_page = CartCheckOutPage(context)
    context.login_page = LoginPage(context)

def after_all(context):
    """
    Teardown that runs after the entire test suite
    """
    context.driver.close()
    context.proj_logger.info("Closed the Browser session and hence this TEST session too!")

def after_scenario(context, scenario):
    """
    Teardown that runs after each scenario
    """
    context.Is_Website_Burger_Menu_On_Top_Left_Corner()
    context.Get_Website_Burger_Menu_From_Top_Left_Corner()
    context.Logout()


def login_as_standard_user_before_each_test_scenario(context):
    """
    Setup that runs before each scenario
    """
    context.login_page.get_user_name_textbox().send_keys('standard_user')
    context.login_page.get_password_textbox().send_keys('secret_sauce')
    context.login_page.get_login_button().click()
    context.login_page.Handle_Browser_Alert_For_Leaked_Passwords()

