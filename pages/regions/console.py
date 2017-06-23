from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.region import Region
from pages.base import Base


class ConsoleItem(Region):
    """
    Data model for items in logging console
    """
    __message_text_locator = (By.CLASS_NAME, 'toast-message')
    __notification_locator = (By.CLASS_NAME, 'toast')

    # Get text from notify
    @property
    def text(self):
        return self.root.find_element(*self.__message_text_locator).text
    @property
    def component(self):
        return self
    # Get class from entity and
    @property
    def state(self):
        """
        Get state of notification
        @return: 0=success, 1=error, 2=warning
        """
        __class = self.__notification_locator.__getattribute__("class")
        if "INFO" in __class:
            return 0
        elif "ERROR" in __class:
            return 1
        elif "WARN" in __class:
            return 2
        elif "DEBUG" in __class:
            return 3
        return self

class Console(Base):
    """
    Logging console
    """

    __console_log_panel = (By.CLASS_NAME, 'log-panel-statements')
    __console_log_item = (By.TAG_NAME, 'li')
    __console_close_locator = (By.ID, 'close')
    __console_copy_all = (By.ID, 'close')
    __console_clear_all = (By.ID, 'close') # @todo find right locator
    __console_open_locator = (By.CSS_SELECTOR, 'i.icon-desktop')  # @todo Report request for missing ID

    def __init__(self, base_url, selenium):
        Base.__init__(self, base_url, selenium)
        WebDriverWait(self.selenium, self.timeout).until(
            lambda s: len(s.find_elements(*self.__console_log_item)) > 0
        )

    """def click_to_clear_all(self):
        self._root_element.find_element(*self._name_locator).click()
    """
    @property
    def items(self):
        """
        Console items
        @return: List
        """
        container = self.selenium.find_element(*self.__console_log_panel)
        elements = container.find_elements(*self.__console_log_item)
        return [ConsoleItem(self.selenium, n) for n in elements]
