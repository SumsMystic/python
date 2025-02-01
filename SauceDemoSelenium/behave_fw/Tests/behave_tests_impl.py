from behave import given, when, then
from time import sleep
from environment import *


context.products_page
context.shopping_cart_page
context.cart_checkout_page
context.login_page

@given('I login as standard user')
def step_impl(context):
    context.login_as_standard_user_before_each_test_scenario()

@when('I add the following items to the cart')
def step_impl(context):
    for row in context.table:
        item_name = row['item_name']
        backpack_item_price = context.Add_Item_To_Cart_And_Get_Its_Price('Sauce Labs Backpack')
        # self.cart_total_price += backpack_item_price
        context.proj_logger.info(f"Price of 'Sauce Labs Backpack' is {backpack_item_price} and has been added to the cart")
        assert context.Is_Shopped_Inventory_Item_Now_Has_Remove_Button('Sauce Labs Backpack')
        context.browser.find_element_by_xpath(f"//div[text()='{item_name}']/following-sibling::button").click()

@when('I remove the following items from the cart')
def step_impl(context):
    for row in context.table:
        item_name = row['item_name']
        context.browser.find_element_by_xpath(f"//div[text()='{item_name}']/following-sibling::button").click()

@when('I add the following items to the cart')
def step_impl(context):
    for row in context.table:
        item_name = row['item_name']
        context.browser.find_element_by_xpath(f"//div[text()='{item_name}']/following-sibling::button").click()

@then('the cart should contain the following items')
def step_impl(context):
    context.browser.find_element_by_class_name('shopping_cart_link').click()
    for row in context.table:
        item_name = row['item_name']
        assert context.browser.find_element_by_xpath(f"//div[text()='{item_name}']")

@then('the cart should show the bill of the items')
def step_impl(context):
    # Assuming the bill is shown on the checkout page
    context.browser.find_element_by_class_name('shopping_cart_link').click()
    context.browser.find_element_by_id('checkout').click()
    assert context.browser.find_element_by_class_name('summary_total_label')

@then('I should be able to checkout using following details')
def step_impl(context):
    context.browser.find_element_by_class_name('shopping_cart_link').click()
    context.browser.find_element_by_id('checkout').click()
    for row in context.table:
        context.browser.find_element_by_id('first-name').send_keys(row['first_name'])
        context.browser.find_element_by_id('last-name').send_keys(row['last_name'])
        context.browser.find_element_by_id('postal-code').send_keys(row['postal_code'])
    context.browser.find_element_by_id('continue').click()
    context.browser.find_element_by_id('finish').click()

@then('the cart should be empty after checkout')
def step_impl(context):
    context.browser.find_element_by_class_name('shopping_cart_link').click()
    assert not context.browser.find_elements_by_class_name('cart_item')