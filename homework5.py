import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

driver.find_element(By.CSS_SELECTOR, "input#delay").clear()
driver.find_element(By.CSS_SELECTOR, "input#delay").send_keys(45)
sleep(2)

driver.find_element(By.XPATH, '//*[text()="7"]').click()
driver.find_element(By.XPATH, '//*[text()="+"]').click()
driver.find_element(By.XPATH, '//*[text()="8"]').click()
driver.find_element(By.XPATH, '//*[text()="="]').click()
sleep(45)

@pytest.mark.parametrize( 'locator',[('.screen')])
def test_result(locator):
    assert driver.find_element(By.CSS_SELECTOR, locator).text == "15"

driver.quit()