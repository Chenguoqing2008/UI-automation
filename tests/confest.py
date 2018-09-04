import os

import pytest

from selenium import webdriver


@pytest.yield_fixture(scope='function')
def browser(request):
    """Fixture to create a web browser."""
    browser = webdriver.Chrome()

    def close_browser():
        """Handle closing browser object."""
        browser.quit()
    request.addfinalizer(close_browser)

    return browser


@pytest.fixture(scope='session')
def page(request):
    '''Fixture to provide a testable web page.'''
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return '{}{}{}'.format('file://', dir_path, '/data/page.html')


def pytest_addoption(parser):
   parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")


@pytest.fixture(scope="module", autouse=True)
def driver(request):
   browser = request.config.getoption("--driver")
   if browser == 'chrome':
       browser = webdriver.Chrome()
       browser.get("about:blank")
       browser.implicitly_wait(10)
       browser.maximize_window()
       return browser
   else:
       print('only chrome is supported at the moment')


