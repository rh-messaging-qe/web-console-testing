import pytest


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    return selenium
