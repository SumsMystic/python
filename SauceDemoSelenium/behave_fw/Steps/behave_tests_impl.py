from behave import given, when, then
from time import sleep


@given('I login as standard user')
def step_impl(context):
    context.login_page.get_user_name_textbox().send_keys('standard_user')
    context.login_page.get_password_textbox().send_keys('secret_sauce')
    context.login_page.get_login_button().click()
    context.products_page.handle_browser_alert_for_leaked_passwords()

"""
@when('I add the following items to the cart')
def step_impl(context):
    for row in context.table:
        itm_name = row['item_name']
        backpack_item_price = context.products_page.add_item_to_cart_and_get_its_price(itm_name)
        # self.cart_total_price += backpack_item_price
        context.proj_logger.info(f"Price of '{itm_name}' is {backpack_item_price} and has been added to the cart")
        assert context.products_page.does_shopped_inventory_item_now_have_remove_button(itm_name)
    
    shopping_items_number_from_icon = context.products_page.get_no_of_items_from_shopping_cart_icon()
    context.products_page.click_on_shopping_cart_to_view_cart_contents()
    shopping_cart_items = context.shopping_cart_page.get_number_of_shopping_cart_items()
    assert shopping_items_number_from_icon == shopping_cart_items
"""

@when('I remove the following items from the cart')
def step_impl(context):
    assert context.shopping_cart_page.is_shopping_cart_empty() == False
    context.cart_total_price = context.shopping_cart_page.get_cart_total_bill_value()
    for row in context.table:
        itm_name = row['item_name']
        removed_item_price = context.shopping_cart_page.get_product_cart_price_and_remove_from_cart(itm_name)
        context.cart_total_price -= removed_item_price
        sleep(5)
    # After removing all list-items as per the test, click Continue Shopping
    context.shopping_cart_page.click_on_continue_shopping_button()

@when('I add the following items to the cart')
def step_impl(context):
    for row in context.table:
        itm_name = row['item_name']
        item_price = context.products_page.add_item_to_cart_and_get_its_price(itm_name)
        context.cart_total_price += item_price
        context.proj_logger.info(f"Price of '{itm_name}' is {item_price} and has been added to the cart")
        assert context.products_page.does_shopped_inventory_item_now_have_remove_button(itm_name)
    
    shopping_items_number_from_icon = context.products_page.get_no_of_items_from_shopping_cart_icon()
    context.products_page.click_on_shopping_cart_to_view_cart_contents()
    shopping_cart_items = context.shopping_cart_page.get_number_of_shopping_cart_items()
    assert shopping_items_number_from_icon == shopping_cart_items

@then('the cart should contain the following items')
def step_impl(context):
    for row in context.table:
        itm_name = row['item_name']
        assert (context.shopping_cart_page.is_item_present_in_shopping_cart(itm_name)) == True
        

@then('the cart should show the bill of the items')
def step_impl(context):
    cart_calculated_total_bill = context.shopping_cart_page.get_cart_total_bill_value()
    context.cart_total_price = round(context.cart_total_price, 2)
    assert context.cart_total_price == cart_calculated_total_bill

@then('I should be able to checkout using following details')
def step_impl(context):
    context.shopping_cart_page.click_on_checkout_button()
    for row in context.table:
        context.cart_checkout_page.add_first_name(row['first_name'])
        context.cart_checkout_page.add_last_name(row['last_name'])
        context.cart_checkout_page.add_postal_code(row['postal_code'])
    
    context.cart_checkout_page.click_continue_button()
    billing_page_subtotal = context.cart_checkout_page.get_item_total_price_from_final_billing_page()
    assert context.cart_total_price == billing_page_subtotal
    context.cart_checkout_page.click_finish_button()


@then('the cart should be empty after checkout')
def step_impl(context):
    assert (context.cart_checkout_page.is_shopping_cart_empty()) == True
    