from pages.drivers import Drivers
from pages.amazon_page import AmazonPage

# Test case ID: log_am_04

browser = Drivers().chrome()
ap = AmazonPage(driver=browser)

# test data
user_gmail = 'test.integrate.10@gmail.com'
pw_gmail = 'invalid_pw'

# test start
ap.go()

ap.account_list_button.click()
ap.email_input.input_text(user_gmail)
ap.continue_button.click()
ap.pw_input.input_text(pw_gmail)
ap.signin_button.click()

alert = ap.alert_invalid_email_pw.text
assert alert == 'There was a problem'

print('log_am_04 passed')
browser.quit()
