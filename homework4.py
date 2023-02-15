from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

class Register:
    def browser(self):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

def input_first_name(self,locator:str, txt:str):  
    driver.find_element(By.CSS_SELECTOR, locator).click()
    first_name = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
    return first_name


def input_last_name(self,locator:str, txt:str):  
    driver.find_element(By.CSS_SELECTOR, locator).click()
    last_name = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
    return last_name


def input_address(self,locator:str, txt:str):  
    driver.find_element(By.CSS_SELECTOR, locator).click()
    address = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
    return address

def input_zip_code(self,locator:str, txt:str):  
    driver.find_element(By.CSS_SELECTOR, locator).click()
    zip_code = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
    return zip_code


def input_city(self,locator:str, txt:str):  
    driver.find_element(By.CSS_SELECTOR, locator).click()
    city = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
    return city


def input_country(self,locator:str, txt:str):  
    driver.find_element(By.CSS_SELECTOR, locator).click()
    country = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
    return country


def input_job_position(self,locator:str, txt:str):  
    driver.find_element(By.CSS_SELECTOR, locator).click()
    job_position = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
    return job_position

def input_company(self,locator:str, txt:str):  
    driver.find_element(By.CSS_SELECTOR, locator).click()
    company = driver.find_element(By.CSS_SELECTOR, locator).send_keys(txt)
    return company

def button_click(self,button):
    driver.find_element(By.CSS_SELECTOR, button).click()




@pytest.mark.parametrize("locator, data", ["[name='first-name']", "Иван"])
def test_fill_field_first_name(locator, data):
    registrated = Register()
    registrated.input_first_name(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='last-name']", "Петров"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_last_name(locator, data)


@pytest.mark.parametrize("locator, data", ["[name='address']", "Ленина, 55-3"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_address(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='zip-code']", "", "#zip-code"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_zip_code(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='city']", "Москва"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_city(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='country']", "Россия"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_country(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='job-position']", "QA"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_job_position(locator, data)

@pytest.mark.parametrize("locator, data", ["[name='company']", "SkyPro"])
def test_fill_field_last_name(locator, data):
    registrated = Register()
    registrated.input_company(locator, data)