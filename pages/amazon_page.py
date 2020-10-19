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

    # nav hamburger menu 'Shop by category'

    @property
    def open_menu_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[id="nav-hamburger-menu"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button1(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[1]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button2(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button3(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[3]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button4(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[4]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button5(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[5]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button6(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[6]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button7(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[7]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button8(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[8]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button9(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[9]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button10(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[10]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button11(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[11]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button12(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[12]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button13(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[13]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button14(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[14]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button15(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[15]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button16(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[16]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button17(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[17]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button18(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[18]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button19(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[19]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button20(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[20]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button21(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[21]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button22(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[22]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button23(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[23]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def main_menu_button24(self):
        locator = Locator(By.XPATH, '(//div[text()="main menu"])[24]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def shop_by_category_title(self):
        locator = Locator(By.XPATH, '//div[text()="shop by category"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def amazon_music_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="2"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def amazon_music_title(self):
        locator = Locator(By.XPATH, '//div[text()="stream music"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def kindle_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="3"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def kindle_title(self):
        locator = Locator(By.XPATH, '//div[text()="kindle e-readers"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def app_android_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="4"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def app_android_title(self):
        locator = Locator(By.XPATH, '//div[text()="appstore for android"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def electronic_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="5"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def electronic_title(self):
        locator = Locator(By.XPATH, '//div[text()="electronics"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def computers_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="6"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def computers_title(self):
        locator = Locator(By.XPATH, '//div[text()="computers"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def smart_home_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="7"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def smart_home_title(self):
        locator = Locator(By.XPATH, '//div[text()="smart home"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def arts_crafts_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="8"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def arts_crafts_title(self):
        locator = Locator(By.XPATH, '//div[text()="arts & crafts"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def automotive_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="9"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def automotive_title(self):
        locator = Locator(By.XPATH, '//div[text()="automotive"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def baby_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="10"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def baby_title(self):
        locator = Locator(By.XPATH, '//div[text()="baby"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def beauty_care_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="11"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def beauty_care_title(self):
        locator = Locator(By.XPATH, '//div[text()="beauty and personal care"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def women_fashion_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="12"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def women_fashion_title(self):
        locator = Locator(By.XPATH, '(//ul[@data-menu-id="12"]/li)[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def man_fashion_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="13"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def man_fashion_title(self):
        locator = Locator(By.XPATH, '(//ul[@data-menu-id="13"]/li)[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def girl_fashion_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="14"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def girl_fashion_title(self):
        locator = Locator(By.XPATH, '(//ul[@data-menu-id="14"]/li)[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def boy_fashion_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="15"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def boy_fashion_title(self):
        locator = Locator(By.XPATH, '(//ul[@data-menu-id="15"]/li)[2]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def healt_house_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="16"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def healt_house_title(self):
        locator = Locator(By.XPATH, '//div[text()="health and household"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def home_kitchen_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="17"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def home_kitchen_title(self):
        locator = Locator(By.XPATH, '//div[text()="home and kitchen"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def industrial_science_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="18"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def industrial_science_title(self):
        locator = Locator(By.XPATH, '//div[text()="industrial and scientific"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def luggage_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="19"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def luggage_title(self):
        locator = Locator(By.XPATH, '//div[text()="luggage"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def movie_tv_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="20"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def movie_tv_title(self):
        locator = Locator(By.XPATH, '//div[text()="movies & television"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def pet_supplies_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="21"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def pet_supplies_title(self):
        locator = Locator(By.XPATH, '//div[text()="pet supplies"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def software_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="22"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def software_title(self):
        locator = Locator(By.XPATH, '//div[text()="software"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sport_outdoor_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="23"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def sport_outdoor_title(self):
        locator = Locator(By.XPATH, '//div[text()="sports and outdoors"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def tools_home_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="24"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def tools_home_title(self):
        locator = Locator(By.XPATH, '(//div[text()="tools & home improvement"])')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def toys_games_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="25"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def toys_games_title(self):
        locator = Locator(By.XPATH, '//div[text()="toys and games"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def video_games_button(self):
        locator = Locator(By.CSS_SELECTOR, 'a[data-menu-id="26"]')
        return BaseElement(driver=self.driver, locator=locator)

    @property
    def video_games_title(self):
        locator = Locator(By.XPATH, '//div[text()="video games"]')
        return BaseElement(driver=self.driver, locator=locator)














