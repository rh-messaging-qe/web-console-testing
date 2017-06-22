import pytest
from selenium.webdriver import Remote


@pytest.fixture
def selenium(selenium: Remote):
    selenium.implicitly_wait(10)
    return selenium
