from pages.page import Page
#from pages.regions.navigation import Navigation
from pages.regions.menu import Menu
#from pages.regions.notification import Notifications
#from pages.regions.console import Console

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Remote


class Base(Page):
    def __init__(self, base_url, selenium: Remote, open_url=True, **kwargs):
        super(Base, self).__init__(base_url, selenium, **kwargs)
        if open_url:
            self.open()
        else:
            self.wait_for_page_to_load()
        self.wait_for_angular()

    @property
    def page_title(self):
        """Page title"""
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.selenium.title
        )
        return self.selenium.title

    @property
    def logged(self):
        """
        Check login state
        @return: bool
        """
        __login_button_locator = (By.CSS_SELECTOR, 'button.btn.btn-success')
        return False if self.is_element_present(__login_button_locator) else True

    @property
    def notification(self):
        """
        Wait for notification and get back text
        @todo Implement model for notifications regions/notifications.py
        @return:
        """
        __message_text_locator = (By.CLASS_NAME, 'toast-message')
        #return self.wait_for_element_displayed(*__message_text_locator).text
        text = self.selenium.find_element(*__message_text_locator).text
        return text
