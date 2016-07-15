from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException


class Page(object):
    """
    Page class
    """
    _url = None

    def __init__(self, base_url, selenium, **kwargs):
        """Constructor for page"""
        self.base_url = base_url
        self.selenium = selenium
        self.timeout = 10
        self.wait = WebDriverWait(self.selenium, self.timeout)
        self.kwargs = kwargs

    @property
    def url(self):
        """
        Set url address for page
        @return: url address
        """
        if self._url is not None:
            return self._url.format(base_url=self.base_url)
        return self.base_url

    def open(self):
        """Open page"""
        self.selenium.get(self.url)
        self.wait_for_page_to_load()
        return self

    def wait_for_page_to_load(self):
        """Wait until the page is loaded."""
        self.wait.until(lambda s: self.url in s.current_url)
        return self

    def is_element_present(self, *locator):
        """
        Check if the element is present on page.
        @param locator:
        @return: bool
        """
        self.selenium.implicitly_wait(0)
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.timeout)

    def is_element_visible(self, *locator):
        """
        Check if the element is visible on page.
        @param locator:
        @return: bool
        """
        try:
            return self.selenium.find_element(*locator).is_displayed()
        except (NoSuchElementException, ElementNotVisibleException):
            return False

    def go_back(self):
        """
        Get back in history.
        """
        self.selenium.back()

    def refresh(self):
        """
        Refresh page (like F5).
        """
        self.selenium.refresh()

    def get_relative_path(self, url):
        """
        Get relative path from url.
        @param url:
        @type url:
        @return: string
        """
        self.selenium.get(u'%s%s' % (self.base_url, url))
