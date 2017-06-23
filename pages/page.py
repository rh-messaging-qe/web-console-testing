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
        self.wait_for_angular()
        return self.selenium.current_url

    def open(self):
        """Open page"""
        self.selenium.get(self.url)
        self.wait_for_page_to_load()
        self.wait_for_angular()
        return self

    def wait_for_page_to_load(self):
        """Wait until the page is loaded."""
        self.wait.until(lambda s: self.url in s.current_url)
        return self

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

    def wait_for_element_presented(self, *locator):
        self.wait.until(lambda s: self.is_element_present(*locator))
        return self.selenium.find_element(*locator)

    def wait_for_element_displayed(self, *locator):
        """Wait for display element was displayed"""
        self.wait.until(lambda s: self.is_element_visible(*locator))
        return self.selenium.find_element(*locator)

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
        self.selenium.implicitly_wait(0)
        try:
            self.selenium.find_element(*locator).is_displayed()
            return True
        except (NoSuchElementException, ElementNotVisibleException):
            return False
        finally:
            # set back to where you once belonged
            self.selenium.implicitly_wait(self.timeout)

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
