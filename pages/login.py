from pages.base import BasePage
import yaml
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        with open('../locators/locators.yaml') as file:
            self.locators = yaml.safe_load(file)['LoginPage']

    def login(self, username, password):
        self.enter_text(username, By.XPATH, self.locators['username'])
        self.enter_text(password, By.XPATH, self.locators['password'])
        self.click(By.XPATH, self.locators['login_button'])
