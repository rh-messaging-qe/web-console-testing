from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Remote
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    """
    Page class
    """
    _url = None

    def __init__(self, base_url: str, selenium: Remote, **kwargs):
        """Page constructor"""
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
            return self._url.format(base_url=self.base_url, **self.kwargs)
        return self.base_url

    def get_url(self, url: url):
        self.selenium.get(url)

    def get_url_current_page(self):
        return self.selenium.current_url

    def open(self):
        """Open page"""
        self.selenium.get(self.url)
        self.wait_for_page_to_load()
        return self

    def wait_for_page_to_load(self):
        """Wait until the page is loaded."""
        self.wait.until(lambda s: self.is_page_loaded())
        return self

    @property
    def is_the_current_page(self):
        return self.url in self.get_url_current_page()

    def wait_for_element_presented(self, *locator):
        self.wait.until(lambda s: self.is_element_present(*locator))
        return self.selenium.find_element(*locator)

    def wait_for_element_displayed(self, *locator):
        """Wait for display element was displayed"""
        self.wait.until(lambda s: self.is_element_visible(*locator))
        return self.selenium.find_element(*locator)

    def is_page_loaded(self):
        """
        Check if the page is loaded
        @param locator:
        @return: bool
        """
        script = "complete" in self.selenium.execute_script("return document.readyState")
        return script


    def is_element_present(self, *locator, timeout=0):
        """
        Check if the element is present on page.
        @param locator:
        @return: bool
        """
        self.selenium.implicitly_wait(timeout)
        try:
            self.selenium.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.timeout)

    def is_not_element_present(self, *locator, timeout=0):
        """
        Check if the element is not present on page.
        @param locator:
        @return: bool
        """
        self.selenium.implicitly_wait(timeout)
        try:
            self.selenium.find_element(*locator)
            return False
        except NoSuchElementException:
            return True
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
            self.selenium.find_element(*locator).is_displayed()
            return True
        except (NoSuchElementException, ElementNotVisibleException):
            return False

    def is_not_element_visible(self, *locator):
        """
        Check if the element is not visible on page.
        @param locator:
        @return: bool
        """
        try:
            self.selenium.find_element(*locator).is_displayed()
            return False
        except (NoSuchElementException, ElementNotVisibleException):
            return True

    def go_back(self):
        """
        Get back in history.
        """
        self.selenium.back()

    def refresh(self):
        """
        Refresh page.
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
