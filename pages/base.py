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

    def wait_for_angular(self):
        """
        Wait until the page is done with AngularJS render page
        @return:
        """
        # waitForAngular()
        # https://github.com/angular/protractor/blob/71532f055c720b533fbf9dab2b3100b657966da6/lib/clientsidescripts.js
        script_wait = """callback = arguments[arguments.length - 1];
           angular.element('body').injector().get('$browser').notifyWhenNoOutstandingRequests(callback);"""

        self.selenium.set_script_timeout(self.timeout)
        self.selenium.execute_async_script(script=script_wait)
        return self

    @property
    def logged(self):
        """
        Check login state
        @return: bool
        """
        __login_button_locator = (By.CSS_SELECTOR, 'button.btn.btn-success')
        return self.is_not_element_present(__login_button_locator)

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
