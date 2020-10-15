from pages.drivers import Drivers
from pages.amazon_page import AmazonPage

# Test case ID: log_am_05

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
ap.pw_input.input_text(pw_gmail)
ap.signin_button.click()

msg = ap.hello_message.text
assert msg == 'Hello, Radek'

print('log_am_05 passed')
browser.quit()



