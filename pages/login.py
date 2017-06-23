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

    def __init__(self, base_url, selenium, open_url=True):
        """Creates a new instance of the class and gets the page ready for testing."""
        Base.__init__(self, base_url, selenium, open_url)

    def __click_login(self):
        self.wait_for_element_displayed(*self.__login_button_locator).click()
        from pages.welcome import WelcomePage
        return WelcomePage(self.base_url, self.selenium, open_url=False)

    def __type_username(self, username):
        self.wait_for_element_displayed(*self.__username_locator).send_keys(username)

    def __type_password(self, password):
        self.wait_for_element_displayed(*self.__password_locator).send_keys(password)

    def __check_remember_me(self):
        self.wait_for_element_displayed(*self.__remember_me_check_locator).click()

    def login(self, username, password, remember=False):
        """
        Login to console with username and password
        @param username: Used username for login
        @param password: Used password for login
        @param remember: Check remember
        @return:
        """
        self.__type_username(username)
        self.__type_password(password)
        if remember:
            self.__check_remember_me()
        login = self.__click_login()
        return login

    @property
    def is_forbidden(self):
        """
        Check if login was forbidden
        @return: Boolean
        """
        return self.__forbidden_msg in self.notification

