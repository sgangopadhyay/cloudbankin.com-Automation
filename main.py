# Login URL : https://qatest.uat.cloudbankin.com/
# Username: qatest@habile.in
# Password: Qatest123$

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from Data.data import AppData
from Locators.web_locators import AppLocators


class Suman:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(AppData().url)
        self.driver.implicitly_wait(15)

    def login(self):
        self.start()

    def shutdown(self):
        self.driver.quit()


Suman().login()

Suman().shutdown()
