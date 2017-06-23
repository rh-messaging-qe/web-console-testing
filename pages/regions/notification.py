from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.region import Region
from pages.base import Base


class Notification(Region):
    __message_close_locator = (By.CLASS_NAME, 'toast-close-button')
    __message_text_locator = (By.CLASS_NAME, 'toast-message')
    __notification_locator = (By.CLASS_NAME, 'toast')

    # Get text from notify
    @property
    def text(self):
        return self.root.find_element(*self.__message_text_locator).text

    # Get class from entity and
    @property
    def state(self):
        """
        Get state of notification
        @return: 0=success, 1=error, 2=warning
        """
        __class = self.__notification_locator.__getattribute__("class")
        if "toast-success" in __class:
            return 0
        elif "toast-error" in __class:
            return 1
        elif "toast-warning" in __class:
            return 2
        return self

    def click_close(self):
        self.selenium.find_element(*self.__message_close_locator).click()


class Notifications(Base):
    # Notification
    __notification_container = (By.CLASS_NAME, 'toast-container')
    __message_text_locator = (By.CLASS_NAME, 'toast-message')

    def __init__(self, base_url, selenium):
        Base.__init__(self, base_url, selenium)
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: self.is_no_results_present or
                      len(s.find_elements(*self._results_locator)) > 0)

    # Do available all notification on page which shows.
    @property
    def notifications(self):
        container = self.selenium.find_element(*self.__notification_container)
        elements = container.selenium.find_elements(*self.__message_text_locator)
        return [Notification(self.selenium, n) for n in elements]
