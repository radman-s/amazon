from pages.drivers import Drivers
from pages.amazon_page import AmazonPage

# Test case ID: log_am_06

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

# make srceenshot of hidden password
ap.pw_input.screen_shot('C:\\Users\\radss\PycharmProjects\\amazon\\test_cases_login\\screenshot_log_am_06.png')

print('log_am_06 passed')
print('Screenshot of hidden password uploaded to test_cases directory as "screenshot_log_am_06.png".')
browser.quit()

