from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .locator import Locator
from .base_page import BasePage

class AmazonPage(BasePage):

    url = 'https://www.amazon.com/'

    # login

    @property
    def account_list_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="nav-link-accountList"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def email_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="ap_email"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def pw_input(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="ap_password"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def continue_button(self):
        locator = Locator(By.CSS_SELECTOR, 'span[id="continue"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def signin_button(self):
        locator = Locator(By.CSS_SELECTOR, 'input[id="signInSubmit"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def alert_enter_emal(self):
        locator = Locator(By.XPATH, '(//div[@class="a-alert-content"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def alert_invalid_email_pw(self):
        locator = Locator(By.XPATH, '//div[@class="a-box-inner a-alert-container"]/h4')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def alert_enter_pw(self):
        locator = Locator(By.XPATH, '(//div[@class="a-alert-content"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def hello_message(self):
        locator = Locator(By.XPATH, '//div[@class="nav-line-1-container"]/span')
        return BaseElement(driver=self.driver, locator=locator)





