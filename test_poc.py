import logging
import time
import pytest



from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

LOG_FORMAT = "%(asctime)s %(levelname)s - %(message)s"
logging.basicConfig(filename="demo.log", level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()


def test_shopping():
    logger.info("Demo for pytest automation")
    service_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(2)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@class='submit-button btn_action']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "button[data-test$='add-to-cart-sauce-labs-onesie']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Zerah")
    driver.find_element(By.CSS_SELECTOR, "input[data-test*='lastName']").send_keys("Mpako")
    driver.find_element(By.XPATH, "//input[@id='postal-code']").send_keys("54-611")
    driver.find_element(By.CSS_SELECTOR, ".submit-button.btn.btn_primary.cart_button.btn_action").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, ".btn.btn_action.btn_medium.cart_button").click()
    time.sleep(3)
    # driver.find_element(By.CSS_SELECTOR, "button[name$='finish']").click()
    message = driver.find_element(By.CSS_SELECTOR, ".complete-header").text
    print(message)
    message_2 = driver.find_element(By.CSS_SELECTOR, ".complete-text").text
    print(message_2)
    driver.execute_script("window.scrollBy(0,0)", "")
    driver.get_screenshot_as_file("screen_login.png")
    assert "Thank you for your order!" in message
    driver.find_element(By.CSS_SELECTOR, ".btn.btn_primary.btn_small").click()
    time.sleep(3)


def test_ebay():
    logger.info("Demo for ebay shopping pytest automation")
    service_obj = Service("/Users/laurentzerahmpakondema/Desktop/Drivers/chromedriver")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(2)
    driver.get("https://www.ebay.com/")
    driver.maximize_window()
    # driver.find_element(By.XPATH, "//button[@aria-label='Accept privacy terms and settings']").click()
    driver.find_element(By.CSS_SELECTOR,"a[href='https://signin.ebay.com/ws/eBayISAPI.dll?SignIn&ru=https%3A%2F%2Fwww.ebay.com%2F']").click()
    driver.find_element(By.CSS_SELECTOR, "#userid").send_keys("testautomation861@gmail.com")
    driver.find_element(By.XPATH, "//button[@id='signin-continue-btn']").click()
    driver.find_element(By.XPATH, "//input[@id='pass']").send_keys("Cameroun_1960")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn--fluid.btn--large.btn--primary").click()
    driver.find_element(By.CSS_SELECTOR,".webauthn-may-be-later.btn.btn--fluid.btn--large-truncated.btn--secondary").click()
    driver.find_element(By.CSS_SELECTOR, ".gh-tb.ui-autocomplete-input").send_keys("shoes jordan")
    time.sleep(2)
    driver.find_element(By.ID, "gh-btn").click()
    driver.find_element(By.XPATH, "(//input[@aria-label='Jordan'])[1]").click()
    driver.find_element(By.XPATH, "//input[@aria-label='Nike']").click()
    driver.find_element(By.LINK_TEXT, "9.5").click()
    # driver.execute_script("window.scrollBy(0,2000)","")
    # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    driver.find_element(By.XPATH, "//ul[@class='srp-results srp-grid clearfix']//span[@role='heading'][contains(text(),'Nike Air Jordan 1 Retro Hi OG Purple 555088-500 Sn')]").click()
    parent_handle = driver.current_window_handle
    print(parent_handle)  # parent window

    handles = driver.window_handles  # return all the values of opened browser windows
    print(handles)
    for handle in handles:
        if handle != parent_handle:
            driver.switch_to.window(handle)
            driver.find_element(By.CSS_SELECTOR, "div[class='vim x-atc-action overlay-placeholder'] span[class='ux-call-to-action__text']").click()
            # driver.find_element(By.CSS_SELECTOR, "a[class='btn btn-prim vi-VR-btnWdth-XL '] span span").click()
            driver.find_element(By.XPATH, "//span[contains(text(),'Checkout 1 item')]").click()
            response = driver.find_element(By.XPATH, "//body/div[@id='root']/div[@class='bodyContent']/div[@id='mainContent']/div[@class='two-column container no-gutters']/div[@class='row no-gutters']/div[@class='left-column col-7 col-lg-8']/section[@class='module shipping-address auto-address-container']/div[1]").text
            print(response)
            driver.execute_script("window.scrollBy(0,0)", "")
            driver.get_screenshot_as_file("screen_ebay.png")

    driver.switch_to.window(parent_handle)
    driver.refresh()
    driver.find_element(By.CLASS_NAME, "gh-cart-icon").click()
    driver.find_element(By.CLASS_NAME, "fake-link").click()
    time.sleep(4)
    driver.execute_script("window.scrollBy(0,0)", "")
    driver.get_screenshot_as_file("screen_ebay_deleting.png")





