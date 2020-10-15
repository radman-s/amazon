from pages.drivers import Drivers
from pages.amazon_page import AmazonPage

# Test case ID: log_am_02

browser = Drivers().chrome()
ap = AmazonPage(driver=browser)

# test data
invalid_gmail = 'ivalid@gmail.com'

# test start
ap.go()

ap.account_list_button.click()

ap.email_input.input_text(invalid_gmail)
ap.continue_button.click()
alert = ap.alert_invalid_email_pw.text
assert alert == 'There was a problem'
print('log_am_02 passed')
browser.quit()



