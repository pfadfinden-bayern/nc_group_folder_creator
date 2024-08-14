import json
from selenium import webdriver
import tomli
from dotmap import DotMap

def load_config(path):
    with open(path, 'rb') as f:
        config = DotMap(tomli.load(f),)
        config._dynamic = False
    return config

def save_cookie(driver, path):
    with open(path, 'w') as filehandler:
        json.dump(driver.get_cookies(), filehandler)

def main():
    config = load_config('config/config.toml')
    driver = get_driver(config)

    driver.get(config.target.url)
    input('log in and press enter in python console')
    save_cookie(driver, config.script.cookie_file)
    driver.close()
    print(f'cookies saved to {config.script.cookie_file}')

def get_driver(config):
    match config.script.driver:
        case 'firefox':
            return webdriver.Firefox()
        case _:
            raise NotImplementedError

if __name__ == "__main__":
    main()