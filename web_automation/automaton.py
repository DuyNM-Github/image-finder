from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.service import Service as FirefoxService
from retry import retry

service = FirefoxService(executable_path=GeckoDriverManager().install())

def _init_driver():
    ff_option = webdriver.FirefoxOptions()
    ff_option.headless = True
    return webdriver.Firefox(service=service, options=ff_option)

async def go_to_web_and_fetch_title(url: str):
    driver = _init_driver()
    driver.get(url)
    title = driver.title
    driver.close()
    return title

async def find_images_on_google(prompt: str):
    # Init driver and navigate to Google Image
    driver = _init_driver()
    driver.get("https://google.com")
    gg_image = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[1]/div/div[2]/a')
    gg_image.click()

    # Input prompt to search bar
    search_bar = driver.find_element(By.TAG_NAME, "input")
    search_bar.send_keys(prompt + Keys.ENTER)

    # Gather images
    img_links = []
    image_elems = WebDriverWait(driver, timeout=5).until(lambda d: d.find_elements(By.XPATH, '/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div'))
    for elem in image_elems:
        elem.click()
        side_bar = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element(By.ID, 'islsp'))
        try:
            img_region: WebElement = side_bar.find_element(By.CSS_SELECTOR, "[role='region']")
        except NoSuchElementException:
            break
        target_img = img_region.find_element(By.CSS_SELECTOR, "a > img")
        img_links.append(target_img.get_attribute("src"))

    driver.close()

    if img_links.__len__ == 0:
        find_images_on_google(str)

    return img_links