from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import py

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# chrome driver
service_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
# service_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/geckodriver")
driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(2)
driver.get("https://www.ebay.com/")
driver.maximize_window()
# driver.find_element(By.XPATH, "//button[@aria-label='Accept privacy terms and settings']").click()
# driver.find_element(By.LINK_TEXT, "Sign in").click()
driver.find_element(By.CSS_SELECTOR, "a[href='https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F']").click()
driver.find_element(By.CSS_SELECTOR, "#userid").send_keys("testautomation861@gmail.com")
driver.find_element(By.XPATH, "//button[@id='signin-continue-btn']").click()
driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("Cameroun_1960")
driver.find_element(By.CSS_SELECTOR, ".btn.btn--fluid.btn--large.btn--primary").click()
# driver.find_element(By.CSS_SELECTOR, ".webauthn-may-be-later.btn.btn--fluid.btn--large-truncated.btn--secondary").click()
driver.find_element(By.CSS_SELECTOR, ".gh-tb.ui-autocomplete-input").send_keys("shoes jordan")
time.sleep(2)
driver.find_element(By.ID, "gh-btn").click()
driver.find_element(By.XPATH, "(//input[@aria-label='Jordan'])[1]").click()
driver.find_element(By.XPATH, "//input[@aria-label='Nike']").click()
driver.find_element(By.XPATH, "//input[@aria-label='Converse']").click()
driver.find_element(By.LINK_TEXT, "9.5").click()
# driver.execute_script("window.scrollBy(0,2000)","")
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.find_element(By.XPATH, "//li[3]//div[1]//div[1]//div[1]//a[1]//div[1]").click()
parent_handle = driver.current_window_handle
print(parent_handle)  # parent window

handles = driver.window_handles  # return all the values of opened browser windows
print(handles)
for handle in handles:
    if handle != parent_handle:
        driver.switch_to.window(handle)
        driver.find_element(By.XPATH, "//button[@id='bidBtn_btn']").click()
        # driver.find_element(By.CSS_SELECTOR, "a[class='btn btn-prim vi-VR-btnWdth-XL '] span span").click()
        driver.find_element(By.CSS_SELECTOR, "#s0-0-1-1-3-placebid-section-offer-section-price-10-textbox").send_keys("30")
#         response = driver.find_element(By.XPATH, "//body/div[@id='root']/div[@class='bodyContent']/div[@id='mainContent']/div[@class='two-column container no-gutters']/div[@class='row no-gutters']/div[@class='left-column col-7 col-lg-8']/section[@class='module shipping-address auto-address-container']/div[1]").text
#         print(response)
#         driver.execute_script("window.scrollBy(0,0)","")
#         driver.get_screenshot_as_file("screen_ebay.png")
#
# driver.switch_to.window(parent_handle)
# driver.refresh()
# driver.find_element(By.CLASS_NAME, "gh-cart-icon").click()
# driver.find_element(By.CLASS_NAME, "fake-link").click()
# time.sleep(4)
# driver.execute_script("window.scrollBy(0,0)","")
# driver.get_screenshot_as_file("screen_ebay_deleting.png")


