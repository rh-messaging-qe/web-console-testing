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

    class Menu(Page):
        # Menu
        __menu_locator = (By.CLASS_NAME, 'dropdown')

        # Menu items
        __preferences_locator = (By.LINK_TEXT, 'Preferences')
        __logout_locator = (By.LINK_TEXT, 'Log out')
        __about_locator = (By.LINK_TEXT, 'About')

        def click_menu(self):
            self.selenium.find_element(*self.__menu_locator).click()

        def click_logout(self):
            self.click_menu()
            self.selenium.find_element(*self.__logout_locator).click()

        def click_preferences(self):
            self.click_menu()
            self.selenium.find_element(*self.__preferences_locator).click()

        def click_about(self):
            self.click_menu()
            self.selenium.find_element(*self.__about_locator).click()

    class Navigation(Page):
        """
        Navigation where is viewed activated plugins
        """
        # Menu
        __artemis_locator = (By.LINK_TEXT, 'Artemis')
        __connect_locator = (By.LINK_TEXT, 'Connect')
        __dashboard_locator = (By.LINK_TEXT, 'Dashboard')
        __jmx_locator = (By.LINK_TEXT, 'JMX')

        def click_artemis(self):
            self.selenium.find_element(*self.__artemis_locator).click()

        def click_connect(self):
            self.selenium.find_element(*self.__connect_locator).click()

        def click_dashboard(self):
            self.selenium.find_element(*self.__dashboard_locator).click()

        def click_jmx(self):
            self.selenium.find_element(*self.__jmx_locator).click()
