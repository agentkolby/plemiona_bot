import time
import os

from dotenv import load_dotenv 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

load_dotenv()

USER = os.environ.get("USERNAME")

print(USER)

driver = webdriver.Chrome('drivers/mac_chromedriver')

driver.get("https://www.plemiona.pl")
time.sleep(5)
driver.close()