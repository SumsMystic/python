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
    context.proj_logger.level = logging.INFO
    context.log_file_handler = logging.FileHandler("../logs/default_log_file.log")
    context.log_formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s: %(message)s")
    context.log_file_handler.setFormatter(context.log_formatter)
    context.proj_logger.addHandler(context.log_file_handler)
    context.proj_logger.info("\n **************  START NEW RUN  **************")

    context.driver = webdriver.Chrome()
    context.driver.get('https://www.saucedemo.com')
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.expl_wait_obj = WebDriverWait(context.driver, 10)
    context.products_page = ProductsDisplayPage(context)
    context.shopping_cart_page = ShoppingCartPage(context)
    context.cart_checkout_page = CartCheckOutPage(context)
    context.login_page = LoginPage(context)
    context.cart_total_price = 0

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
    context.login_page.is_website_burger_menu_on_top_left_corner()
    context.login_page.get_website_burger_menu_from_top_left_corner()
    context.login_page.reset_website_state()
    context.login_page.logout()
    context.proj_logger.info("Logging out from the application")
    
