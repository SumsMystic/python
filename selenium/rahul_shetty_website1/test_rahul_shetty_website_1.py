'''
Created on May 6, 2024

@author: Sumeet Agrawal
'''



from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_obj = webdriver.Chrome()
driver_obj.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver_obj.implicitly_wait(5)

driver_obj.find_element(By.XPATH, "//input[@type='search']").send_keys("be")
time.sleep(5)

veggie_cards = driver_obj.find_elements(By.XPATH, "//div[@class='product']")

for each_veggie in veggie_cards:
    each_veggie.find_element(By.XPATH, "//button[test()='ADD TO CART']").click()
