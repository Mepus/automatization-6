from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

serch_input = driver.get("https://www.saucedemo.com/")
serch_input = driver.find_element(By.CSS_SELECTOR, "input#user-name.input_error.form_input")
serch_input.send_keys("standard_user")


serch_input = driver.find_element(By.CSS_SELECTOR, "input#password.input_error.form_input")
serch_input.send_keys("secret_sauce")
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "input#login-button.submit-button.btn_action")
serch_input.send_keys(Keys.RETURN)
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack.btn.btn_primary.btn_small.btn_inventory")
serch_input.send_keys(Keys.RETURN)
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt.btn.btn_primary.btn_small.btn_inventory")
serch_input.send_keys(Keys.RETURN)
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie.btn.btn_primary.btn_small.btn_inventory")
serch_input.send_keys(Keys.RETURN)
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "button#checkout.btn.btn_action.btn_medium.checkout_button").click()

sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "input#first-name.input_error.form_input")
serch_input.send_keys("Бичико")
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "input#last-name.input_error.form_input")
serch_input.send_keys("Мепуришвили")
sleep(2)
serch_input = driver.find_element(By.CSS_SELECTOR, "input#postal-code.input_error.form_input")
serch_input.send_keys("146326382")
sleep(2)
serch_input = driver.quit()




