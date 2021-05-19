

class SessionHelper:

    XPATHS = {
        "Sign Up": '//*[@class="signup__submit"]',
        "User profile": '//*[@class="user-profile"]',
        "User profile icon": '//*[@class="user-profile__profile"]/../../..//*[@class="user-profile"]',
        "Log out": '//*[span="Log out"]',
        "Email in user profile": '//*[@class="user-profile__text user-profile__text--email"]',
        "Warning message": '//*[@class="signup__error-item"]'
    }

    def __init__(self, app):
        self.app = app

    def open_login_page(self):
        login_url = self.app.config.LOGIN_URL
        self.app.wd.get(login_url)

    def login(self, username, password):
        self.open_login_page()
        self.app.base_func.send_keys_by_name("email", username)
        self.app.base_func.send_keys_by_name("password", password)
        self.app.base_func.click_by_xpath((self.XPATHS['Sign Up']))

    def get_email_in_user_profile(self):
        self.app.base_func.click_by_xpath(self.XPATHS['User profile'])
        email = self.app.base_func.get_text_by_xpath(self.XPATHS['Email in user profile'])
        return email

    def get_warning_text(self):
         return self.app.base_func.get_text_by_xpath(self.XPATHS['Warning message'])

    def is_logged_in(self):
        avatar = self.app.wd.find_elements_by_xpath(self.XPATHS['User profile icon'])
        if len(avatar) and avatar[0].is_displayed(): 1;0

    def logout(self):
        self.app.base_func.click_by_xpath(self.XPATHS['Log out'])

    def ensure_login(self, username, password):
        if self.is_logged_in():
            return
        else:
            self.logout()
        self.login(username, password)

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()
