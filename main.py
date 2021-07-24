import time
import os
import schedule

from dotenv import load_dotenv 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

from utilities.get_cookies import get_cookies

# from tasks.scavenge import task_url

load_dotenv()
cookies = get_cookies()

driver = webdriver.Chrome('drivers\windows_chromedriver')

DOMAIN = 'https://www.plemiona.pl'

def login():

    driver.get(DOMAIN)

    time.sleep(2)

    driver.delete_all_cookies()
    for cookie_name, cookie_value in cookies.items():
        driver.add_cookie({"name": cookie_name, "value": cookie_value})

    driver.refresh()

    time.sleep(1)

    driver.find_element_by_class_name('world_button_active').click()

    time.sleep(1)

def back_to_main():
    driver.get('https://pl167.plemiona.pl/game.php?screen=overview&intro')
    time.sleep(2)

def zbieractwo():

    # IDZIESZ NA STRONE ZBIERACTWA
    driver.get('https://pl167.plemiona.pl/game.php?village=9182&screen=place&mode=scavenge')
    time.sleep(1)

    try:
        driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div[3]/div[3]/div/div[2]/a[1]')
    except NoSuchElementException:
        back_to_main()
        return

    driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[1]/tbody/tr/td/table/tbody/tr[2]/td[2]/ul/li[7]/span/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div[3]/div[3]/div/div[2]/a[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[1]/tbody/tr/td/table/tbody/tr[2]/td[2]/ul/li[7]/span/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div[2]/div[3]/div/div[2]/a[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[1]/tbody/tr/td/table/tbody/tr[2]/td[2]/ul/li[7]/span/a').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td[2]/table[3]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/div/div/div[2]/div[1]/div[3]/div/div[2]/a[1]').click()
    time.sleep(1)
    

def login_if_not_logged():

    try:
        if driver.find_element_by_class_name('world_button_active'):
            driver.find_element_by_class_name('world_button_active').click()
    except ElementClickInterceptedException:
        return


def close_tab():

    driver.close()

if __name__ == "__main__":

    schedule.every(30).seconds.do(zbieractwo)
    schedule.every(60).seconds.do(login_if_not_logged)
    
    login()

    while 1:
        schedule.run_pending()
        time.sleep(1)
    


