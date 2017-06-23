from pages.base import Base
from selenium.webdriver.common.by import By


class WelcomePage(Base):
    """HawtIO login page"""
    _url = '{base_url}/welcome'

    __welcome_button = (By.XPATH, '//button[@ng-click="stopShowingWelcomePage()"]')

    def __init__(self, base_url, selenium, open_url=True):
        """Creates a new instance of the class and gets the page ready for testing."""
        Base.__init__(self, base_url, selenium, open_url)

    def __click_welcome_button(self):
        self.wait_for_element_displayed(*self.__welcome_button).click()
        # return ArtemisTab @todo when will done Artemis plugin model, implement return for Artemis
        #from pages.artemis import ArtemisPage
        #return ArtemisPage(self.base_url, self.selenium, open_url=False)Page

    @property
    def is_welcome_button_present(self):
        return True if self.is_element_present(self.__welcome_button) else False
