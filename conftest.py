from fixture.application import Application
import pytest

fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseurl")
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
        fixture.session.ensure_login(username=username, password=password)
    elif not fixture.is_valid():
        fixture = Application(browser=browser, base_url=base_url)
        fixture.session.ensure_login(username=username, password=password)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def finalizer():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(finalizer)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseurl", action="store", default="http://localhost/addressbook/")
    parser.addoption("--username", action="store", default="admin")
    parser.addoption("--password", action="store", default="")
