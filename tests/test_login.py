import pytest
from pages.login import LoginPage
from pages.welcome import WelcomePage

from os.path import dirname, join
from pickle import dump

@pytest.mark.nondestructive
def test_login_valid(base_url, selenium, user):
    """
    Users can log in
    @param base_url:
    @param selenium:
    @param user: fixtures
    @type base_url: string
    @type selenium:
    @type user:
    """
    login_page = LoginPage(base_url, selenium)
    welcome_page = login_page.login(user.username, user.password)
    assert welcome_page.is_the_current_page


@pytest.mark.nondestructive
def test_login_invalid_password(base_url, selenium, user):
    """
    Users cannot login with wrong password
    @type base_url: string
    @type selenium:
    @type user: strings
    """
    login_page = LoginPage(base_url, selenium)
    login = login_page.login(user.username, user.password + 'x')
    assert login_page.is_the_current_page
    #assert login_page.is_forbidden


@pytest.mark.nondestructive
def test_login_invalid_username(base_url, selenium, user):
    """
    Attempt to log in with an invalid username
    @type base_url: string
    @type selenium:
    @type user: strings
    """
    login_page = LoginPage(base_url, selenium)
    login = login_page.login(user.username + 'x', user.password)
    assert login_page.is_the_current_page
    #assert login_page.is_forbidden

@pytest.mark.nondestructive
def test_login_invalid_password_username(base_url, selenium, user):
    """
    Users cannot login with wrong password
    @type base_url: string
    @type selenium:
    @type user: strings
    """
    login_page = LoginPage(base_url, selenium)
    login = login_page.login(user.username + 'x', user.password + 'x')
    assert login_page.is_the_current_page
    #assert login_page.is_forbidden

@pytest.mark.nondestructive
def test_logout(base_url, selenium, user):
    """
    Users can logout
    @type base_url: string
    @type selenium:
    @type user: strings
    """
    login_page = LoginPage(base_url, selenium)
    welcome_page = login_page.login(user.username, user.password)
    assert welcome_page.is_the_current_page
    #welcome.Menu.click_logout()
    #assert login_page.is_the_current_page

@pytest.mark.nondestructive
def test_logon_fixture(base_url, selenium, user, setup_login):
    """
    Users can logout
    @type base_url: string
    @type selenium:
    @type user: strings
    """
    assert WelcomePage.is_the_current_page