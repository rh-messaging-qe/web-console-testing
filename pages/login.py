from pages.base import Base
from selenium.webdriver.common.by import By


class LoginPage(Base):
    """HawtIO login page"""
    _url = '{base_url}/login'

    __username_locator = (By.ID, 'username')
    __password_locator = (By.ID, 'password')
    __login_button_locator = (By.CLASS_NAME, 'btn-success')
    __remember_me_check_locator = (By.ID, 'rememberMe')

    __forbidden_msg = 'Failed to log in, Forbidden'

    def click_login(self):
        self.wait_for_element_displayed(*self.__login_button_locator).click()

    def type_username(self, username):
        self.wait_for_element_displayed(*self.__username_locator).send_keys(username)

    def type_password(self, password):
        self.wait_for_element_displayed(*self.__password_locator).send_keys(password)

    def check_remember_me(self):
        self.wait_for_element_displayed(*self.__remember_me_check_locator).click()

    def login(self, username, password, remember=False):
        """
        Login to console with username and password
        @param username: Used username for login
        @param password: Used password for login
        @param remember: Check remember
        @return:
        """
        self.type_username(username)
        self.type_password(password)
        if remember:
            self.check_remember_me()
        self.click_login()

    @property
    def is_forbidden(self):
        return True if self.__forbidden_msg in self.notification_text else False
