import pytest
from pages.login import LoginPage


@pytest.mark.nondestructive
def test_login_valid(base_url: str, selenium, variables):
    """
    Users can log in
    @type base_url: string
    @type selenium:
    @type variables: strings
    """
    login_page = LoginPage(base_url, selenium)
    login_page.login(variables['username'], variables['password'])


@pytest.mark.nondestructive
def test_login_invalid_password(base_url, selenium, variables):
    """
    Users cannot login with wrong password
    @type base_url: string
    @type selenium:
    @type variables: strings
    """
    login_page = LoginPage(base_url, selenium)
    login_page.login(variables['username'], variables['password'] + 'x')
    assert login_page.is_forbidden


@pytest.mark.nondestructive
def test_login_invalid_username(base_url, selenium, variables):
    """
    Attempt to log in with an invalid username
    @type base_url: string
    @type selenium:
    @type variables: strings
    """
    login_page = LoginPage(base_url, selenium)
    login_page.login(variables['username'] + 'x', variables['password'])
    assert login_page.is_forbidden


@pytest.mark.nondestructive
def test_login_invalid_password_username(base_url, selenium, variables):
    """
    Users cannot login with wrong password
    @type base_url: string
    @type selenium:
    @type variables: strings
    """
    login_page = LoginPage(base_url, selenium)
    login_page.login(variables['username'] + 'x', variables['password'] + 'x')
    assert login_page.is_forbidden


@pytest.mark.nondestructive
def test_logout(base_url, selenium, variables):
    """
    Users can logout
    @type base_url: string
    @type selenium:
    @type variables: strings
    """
    login_page = LoginPage(base_url, selenium)
    login_page.login(variables['username'], variables['password'])
    assert 'welcome' in login_page.get_url_current_page()
