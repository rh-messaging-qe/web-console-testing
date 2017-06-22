import pytest


@pytest.fixture
def selenium(selenium: Remote):
    selenium.implicitly_wait(10)
    return selenium
