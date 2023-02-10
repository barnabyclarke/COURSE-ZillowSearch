from Zillow import ZillowScraper
# import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

ZILLOW_ENDPOINT = "https://www.zillow.com/"


class FormFill(ZillowScraper):

    def __init__(self):
        super().__init__()
        self.chrome_driver_path = Service("C:/Users/BC/Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.chrome_driver_path)
        self.driver.maximize_window()
        self.input_info()

    def input_info(self):
        for number in range(len(self.address_list)):
            self.driver.get(
                "https://docs.google.com/forms/d/e/1FAIpQLSe4Bsqo9B0sWRftdPWoGfcn36SFmeuxUF34F94r006MtGMcGg/viewform?"
                "usp=sf_link")  # Open page
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            )).send_keys(self.address_list[number])  # Address input
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            )).send_keys(self.price_list[number])  # PPM input
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            )).send_keys(f"{ZILLOW_ENDPOINT}{self.link_list[number]}")  # Link input
            ActionChains(self.driver).send_keys(Keys.TAB).perform()    # \/
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()  # Sends form
            time.sleep(1)

# "https://www.zillow.com/b/nob-hill-place-san-francisco-ca-5XkKgw/"
# "https://www.zillow.com/b/nob-hill-place-san-francisco-ca-5XkKg/"
