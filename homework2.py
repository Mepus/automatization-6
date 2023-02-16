from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(20)

driver.get("http://uitestingplayground.com/textinput")

serch_locator = "input#newButtonName.form-control"
serch_input = driver.find_element(By.CSS_SELECTOR, serch_locator)
serch_input.send_keys("SkyPro")
sleep(5)
serch_input = driver.find_element(By.CSS_SELECTOR, "button#updatingButton")
serch_input.send_keys(Keys.RETURN)
sleep(5)

content = driver.find_element(By.CSS_SELECTOR, "button#updatingButton").text
print(content)

driver.quit()