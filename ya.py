from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

driver.maximize_window()
driver.get("https://ya.ru")
sleep(5)

driver.save_screenshot('./ya_.png')
driver.quit()

def make_screenshoot(driver):
    driver.maximize_window()
    driver.get("https://ya.ru")
    sleep(5)

    driver.save_screenshot('./ya_'+driver.name'.png')
    driver.quit()

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

make_screenshoot(chrome)
make_screenshoot(firefox)
make_screenshoot(edge)