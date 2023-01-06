from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService

service = FirefoxService(executable_path=GeckoDriverManager().install())

def _init_driver():
    ff_option = webdriver.FirefoxOptions()
    ff_option.headless = True
    return webdriver.Firefox(service=service, options=ff_option)

async def go_to(url: str):
    driver = _init_driver()
    driver.get(url)
    title = driver.title
    driver.close()
    return title