from selenium import webdriver
from fixture.session import SessionHelper
from fixture.base_func import BaseFunc
import os

# Main setup class
class Application:
    def __init__(self, base_url, config):
        ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))
        driver = webdriver.Chrome(executable_path=os.path.join(ROOT_DIR, 'chromedriver'))
        self.wd = driver
        driver.maximize_window()
        self.session = SessionHelper(self)
        self.base_func = BaseFunc(self)
        self.config = config
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
