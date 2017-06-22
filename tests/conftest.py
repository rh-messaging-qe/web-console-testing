import pytest
from selenium.webdriver import Remote


@pytest.fixture
def selenium(selenium: Remote):
    selenium.implicitly_wait(10)
    return selenium


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

@pytest.fixture
def user(variables):
    var = variables['user']
    username = var['username']
    password = var['password']
    user = User(username, password)
    return user
