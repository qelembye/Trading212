__author__ = 'cromox'

from time import sleep
import inspect
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Forex_CFD.base.basepage import BasePage
import Forex_CFD.utilities.custom_logger as cl
import logging

class FxMainPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def autologin_firstwindows(self, base_url, username, passwd):
        self.log.info("-> " + inspect.stack()[0][3] + " started")
        self.log.info("--> Trading212 user = " + str(username))
        self.driver.get(base_url)
        self.driver.find_element_by_id("cookie-bar").click()
        self.driver.find_element_by_id("login-header-desktop").click()
        self.driver.find_element_by_id("username-real").send_keys(username + Keys.ENTER)
        print('Trading212 user = ', username)
        self.driver.find_element_by_id("pass-real").send_keys(passwd + Keys.ENTER)
        sleep(2)

    def close_popup_ask_upload_docs(self):
        self.log.info("--> " + inspect.stack()[0][3] + " started")
        # CSS selector - >  #upload-popup-3 > div.popup-header > div.close-icon.svg-icon-holder
        # xpath1 = '//div[@id="onfido-upload"]//div[@class="close-icon svg-icon-holder"]'   # old one
        # xpath2 = '//div[@id="upload-popup-3"]//div[@class="close-icon svg-icon-holder"]'  # new one
        xpathx = '//div[contains(@id, "upload")]//div[@class="close-icon svg-icon-holder"]'
        try:
            self.driver.find_element_by_xpath(xpathx).click()
        except:
            print('no pop-up')

    def mode_live_or_demo(self, mode):
        self.log.info("--> " + inspect.stack()[0][3] + " started // Mode = " + str(mode))
        print('Mode use = ', mode)
        current_url = self.driver.current_url
        urlmode = current_url.split('//')[-1].split(".")[0]  # -- > live or demo
        if urlmode == "live" and mode == "Practice":
            elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "account-menu-button")))
            elem.click()
            try:
                elem = self.driver.find_element_by_class_name("green")
                elem.click()
            except:
                print('already on Practice mode')
        elif urlmode == "demo" and mode == "Real":
            elem = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "account-menu-button")))
            elem.click()
            try:
                elem = self.driver.find_element_by_class_name("blue")
                elem.click()
            except:
                print('already on Real mode')