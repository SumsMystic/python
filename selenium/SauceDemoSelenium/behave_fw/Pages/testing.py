from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pywinauto import Desktop

windows = Desktop(backend="uia").windows()
print([w.window_text() for w in windows])

"""
driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com')
driver.maximize_window()
driver.implicitly_wait(5)
expl_wait_obj = WebDriverWait(driver, 10)

win_handles = driver.window_handles
print(f"Window Handles: {win_handles}")
print(f"Current Window Handle: {driver.current_window_handle}")
"""