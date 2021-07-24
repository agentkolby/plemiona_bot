import time
import os

from dotenv import load_dotenv 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from utilities.get_cookies import get_cookies

from tasks.scavenge import task_url

load_dotenv()
cookies = get_cookies()

driver = webdriver.Chrome('drivers\windows_chromedriver')

DOMAIN = 'https://www.plemiona.pl'

driver.get(DOMAIN)

time.sleep(2)

driver.delete_all_cookies()
for cookie_name, cookie_value in cookies.items():
    driver.add_cookie({"name": cookie_name, "value": cookie_value})

driver.refresh()

time.sleep(2)

driver.find_element_by_class_name('world_button_active').click()

time.sleep(2)

print(task_url)


driver.close()



