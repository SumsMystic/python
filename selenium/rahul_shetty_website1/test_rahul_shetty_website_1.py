'''
Created on May 6, 2024

@author: Sumeet Agrawal
'''



from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver_obj = webdriver.Chrome()
driver_obj.maximize_window()
driver_obj.implicitly_wait(5)

expl_wait = WebDriverWait(driver=driver_obj, timeout=15)

driver_obj.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver_obj.find_element(By.XPATH, "//input[@type='search']").send_keys("be")
time.sleep(5)

veggie_cards = driver_obj.find_elements(By.XPATH, "//div[@class='product']")

for each_veggie in veggie_cards:
    driver_obj.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()

#Click on the cart
driver_obj.find_element(By.CLASS_NAME, "cart-icon").click()

driver_obj.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(5)

# Get total amount in each row in table
amounts_lst = driver_obj.find_elements(By.XPATH, "//tr/td[5]")
final_amts_lst = amounts_lst[1:]

basket_total = 0
for each_total_amt in final_amts_lst:
    basket_total += int(each_total_amt.text)
    
website_basket_total = driver_obj.find_element(By.XPATH, "//span[@class='totAmt']").text
assert int(website_basket_total) == basket_total

# Now apply the Promocode
driver_obj.find_element(By.XPATH, "//input[@class='promoCode']").send_keys("rahulshettyacademy")
driver_obj.find_element(By.XPATH, "//button[text()='Apply']").click()

expl_wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='promoInfo']")), "Code Applied Successfully")
discount = driver_obj.find_element(By.XPATH, "//span[@class='discountPerc']").text
assert discount == '10%'

driver_obj.find_element(By.XPATH, "//button[text()='Place Order']").click()
time.sleep(5)
# Select Country
drop_down_obj = Select(driver_obj.find_element(By.XPATH, "//Select"))
drop_down_obj.select_by_visible_text("India")

agree_box = driver_obj.find_element(By.XPATH, "//input[@type='checkbox']")
agree_box.click()

assert agree_box.is_enabled()

driver_obj.find_element(By.XPATH, "//button[text()='Proceed']").click()
