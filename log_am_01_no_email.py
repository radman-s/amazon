from pages.drivers import Drivers
from pages.amazon_page import AmazonPage

# Test case ID: log_am_01

browser = Drivers().chrome()
ap = AmazonPage(driver=browser)

# test start
ap.go()

ap.account_list_button.click()
ap.continue_button.click()
alert = ap.alert_enter_emal.text
assert alert == 'Enter your email or mobile phone number'
print('log_am_01 passed')
browser.quit()












