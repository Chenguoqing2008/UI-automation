#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import pytest
import os
import yaml
from selenium.webdriver.chrome.options import Options
from splinter.browser import Browser
import platform


class Config:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(root_dir, 'config.yaml')
    ITEMS = yaml.load(open(config_path))

    driver_path = os.path.join(root_dir, 'utilities')

    if'Ubuntu' in platform.platform() or 'Darwin' in platform.platform():
        chrome_driver_path = os.path.join(driver_path, 'chromedriver')
    else:
        chrome_driver_path = os.path.join(driver_path, 'chromedriver.exe')

    EXECUTABLE_PATH = {'executable_path': chrome_driver_path}


def pytest_addoption(parser):
    parser.addoption("--remote",  action="store_true",
                     help="Use selenium grid to execute test cases or not.")
    parser.addoption("--env", action="store", default='QA',
                     help="Test environment QA or LIVE.")


def get_remote_browser():
    remote_server_url = Config.ITEMS['remote_url']
    chrome_options = Options()
    chrome_options.add_argument("headless")
    chrome_options.add_argument('--no-sandbox')
    capabilities = chrome_options.to_capabilities()
    browser = Browser(
        driver_name="remote",
        url=remote_server_url,
        browser='chrome',
        desired_capabilities=capabilities)
    return browser


@pytest.fixture(scope="class", autouse=True)
def env(request):
    if request.config.getoption('env') == 'QA':
        request.cls.config = Config.ITEMS['QA']
        yield
    else:
        request.config.config = Config.ITEMS['LIVE']
        yield


@pytest.fixture(scope="class", autouse=True)
def browser_instance(request):
    # remote = request.config.getoption('remote')
    # if not remote:
    #     browser = Browser("chrome", **Config.EXECUTABLE_PATH)
    # else:
    #     browser = get_remote_browser()
    browser = Browser("chrome", **Config.EXECUTABLE_PATH)
    browser.driver.maximize_window()
    request.cls.browser = browser
    yield
    request.cls.browser.quit()

