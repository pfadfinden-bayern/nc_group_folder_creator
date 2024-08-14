import contextlib
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as SeWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import tomli
from dotmap import DotMap
import time

def load_config(path):
    with open(path, 'rb') as f:
        config = DotMap(tomli.load(f),)
        config._dynamic = False
    return config

def load_cookie(driver, path):
    with open(path, 'r') as cookiesfile:
        cookies = json.load(cookiesfile)
    for cookie in cookies:
        driver.add_cookie(cookie)

def main():
    config = load_config('config/config.toml')
    driver = get_driver(config)

    # load_page_with_cookies(config, driver)
    driver.get(config.target.url)
    # input('log in and press enter in python console')

    name = 'test_folder'
    groups = ['group 1', 'group 2']
    quota = '24MB'

    SeWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'groupfolders-react-root')))
    base_table = driver.find_element(By.ID, 'groupfolders-react-root').find_element(By.TAG_NAME, 'tbody')
    items = base_table.find_elements(By.TAG_NAME, 'tr')

    for item in items:
        with contextlib.suppress(NoSuchElementException):
            name = item.find_element(By.CLASS_NAME, 'mountpoint').text
            groups_edit = item.find_element(By.CLASS_NAME, 'groups').find_element(By.TAG_NAME, 'span').find_element(By.TAG_NAME, 'a')
            groups_edit.click()
            for group in groups:
                group_edit = driver.find_element(By.CLASS_NAME, 'group-edit').find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')[-1]
                # select = Select(group_edit)
                x = 1+1
                # group_edit.click()
                pass


                group_edit.send_keys(group)
                group_edit.send_keys(Keys.ENTER)

            print(name)
    # folder_name = driver.find_element(By.CSS_SELECTOR, '.newgroup-name')
    # folder_name.send_keys(name)
    # folder_name.send_keys(Keys.ENTER)

    time.sleep(10)
    driver.close()
    pass

def load_page_with_cookies(config, driver):
    driver.get(config.target.url)
    time.sleep(1)
    load_cookie(driver, config.script.cookie_file)
    time.sleep(1)
    driver.get(config.target.url)

def get_driver(config):
    match config.script.driver:
        case 'firefox':
            return webdriver.Firefox()
        case _:
            raise NotImplementedError

if __name__ == "__main__":
    main()