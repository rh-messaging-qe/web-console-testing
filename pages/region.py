class Region(object):
    _root_locator = None

    def __init__(self, base_url, selenium, root=None):
        self.base_url = base_url
        self.selenium = selenium
        self.root_element = root

    @property
    def root(self):
        if self.root_element is None and self._root_locator is not None:
            self.root_element = self.selenium.find_element(*self._root_locator)
        return self.root_element
