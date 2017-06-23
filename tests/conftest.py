import pytest
from os import remove
from os.path import dirname, join
from selenium.webdriver import Remote
from pickle import dump, load
import requests


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

@pytest.fixture()
def session_cookies(base_url, user):
    r = requests.post('%s/hawtio/auth/login' % base_url, auth=(user.username, user.password))
    cookies = r.cookies
    return cookies

#@pytest.fixture(scope="session", autouse=True)
def get_login(request, base_url, selenium, user):
    """
    Users can log in
    @type base_url: string
    @type selenium:
    @type user:
    """
    from pages.login import LoginPage
    login_page = LoginPage(base_url, selenium)
    login_page.login(user.username, user.password)
    file = join(dirname(dirname(__file__)), 'cookies.pkl')
    dump(selenium.get_cookies(), open(file, "wb"))


@pytest.fixture()
def setup_login(base_url, selenium, user):
    from pages.login import LoginPage
    login_page = LoginPage(base_url, selenium)
    login_page.login(user.username, user.password)
    file = join(dirname(dirname(__file__)), 'cookies.pkl')
    dump(selenium.get_cookies(), open(file, "wb"))
    print(selenium.get_cookies())

    selenium.get(base_url)
    selenium.delete_all_cookies()
    print(__file__)
    file = join(dirname(dirname(__file__)), 'cookies.pkl')
    cookies = load(open(file, "rb"))
    for cookie in cookies:
        selenium.add_cookie(cookie)


@pytest.fixture
def teardown_login():
    file = join(dirname(dirname(__file__)), 'cookies.pkl')
    remove(file)
