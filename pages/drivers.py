from selenium import webdriver

class Drivers:

    def chrome(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
        return driver

