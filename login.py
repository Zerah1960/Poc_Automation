from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# wait = WebDriverWait(driver, 10)

# chrome driver
service_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@class='submit-button btn_action']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
time.sleep(2)
driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[data-test$='add-to-cart-sauce-labs-onesie']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#checkout").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Zerah")
driver.find_element(By.CSS_SELECTOR, "input[data-test*='lastName']").send_keys("Mpako")
driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("54-611")
driver.find_element(By.CSS_SELECTOR, ".submit-button.btn.btn_primary.cart_button.btn_action").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, ".btn.btn_action.btn_medium.cart_button").click()
time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "button[name$='finish']").click()
message = driver.find_element(By.CSS_SELECTOR, ".complete-header").text
print(message)
message_2 = driver.find_element(By.CSS_SELECTOR, ".complete-text").text
print(message_2)
driver.execute_script("window.scrollBy(0,0)","")
driver.get_screenshot_as_file("screen_login.png")

assert "Thank you for your order!" in message
driver.find_element(By.CSS_SELECTOR, ".btn.btn_primary.btn_small").click()

