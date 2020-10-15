from pages.drivers import Drivers
from pages.amazon_page import AmazonPage

# Test case ID: log_am_03

browser = Drivers().chrome()
ap = AmazonPage(driver=browser)

# test data
user_gmail = 'test.integrate.10@gmail.com'
pw_gmail = 'testpw_02'

# test start
ap.go()

ap.account_list_button.click()

ap.email_input.input_text(user_gmail)
ap.continue_button.click()
ap.signin_button.click()

alert = ap.alert_enter_pw.text
assert alert == 'Enter your password'

print('log_am_03 passed')
browser.quit()