from pages.page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

"""from pages.regions.notification import Notification"""


class Base(Page):
    def __init__(self, base_url, selenium, **kwargs):
        super(Base, self).__init__(base_url, selenium, **kwargs)
        self.open()
        self.menu = Base.Menu(base_url, selenium, **kwargs)

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
    def notification_text(self):
        """
        Wait for notification and get back text
        @todo Implement model for notifications regions/notifications.py
        @return:
        """
        __message_text_locator = (By.CLASS_NAME, 'toast-message')
        return self.wait_for_element_displayed(*__message_text_locator).text

