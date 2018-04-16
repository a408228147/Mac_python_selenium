
import configparser
import os

from selenium import  webdriver
from framework.logger import  Logger
logger = Logger(logger="BrowserEngine").getlog()
class BrowserEngine(object):

    def __init__(self):
        global driver

    def open_browser(self):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType","browserName")
        url = config.get("testServer","URL")
        if browser=="Chrome":
            driver = webdriver.Chrome()
            logger.info("chrome")
        elif browser=="Firefox":
            driver = webdriver.Firefox()
        else:
            driver =webdriver.Ie()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver

    def quit_browser(self,driver):
        driver.quit()
