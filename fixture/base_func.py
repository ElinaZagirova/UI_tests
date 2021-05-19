from selenium.webdriver.common.keys import Keys

# Base common functions helper
class BaseFunc():

    def __init__(self, app):
        self.app = app
        self.wd = app.wd

    def click_by_xpath(self, path):
        self.wd.find_element_by_xpath(path).click()

    # insert text (by default without enter clicking)
    def send_keys_by_name(self, path, value='', click_enter=False):
        self.app.wd.find_element_by_name(path).clear()
        self.app.wd.find_element_by_name(path).send_keys(value)
        if click_enter:
            self.app.wd.find_element_by_name(path).send_keys(Keys.ENTER)

    def get_text_by_xpath(self, path):
        return self.wd.find_element_by_xpath(path).text
