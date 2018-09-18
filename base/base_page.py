#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from selenium.webdriver.support.expected_conditions import presence_of_all_elements_located as all_elements_located
from selenium.webdriver.support.expected_conditions import presence_of_element_located as element_located
from selenium.webdriver.support.expected_conditions import element_to_be_clickable as element_clickable
from selenium.webdriver.support.ui import WebDriverWait
from splinter.browser import Browser
from selenium.webdriver.common.action_chains import ActionChains
import logging
import sys
from base.decorators import log_exception

"""Inspired by  oleg-toporkov in github"""
"""Inspired by  Marcin Koprek in github"""

__author__ = "Robin Chen"


class BasePage(object):
    FORMATTER = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s — %(message)s")

    def __init__(self, browser):
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.FORMATTER)
        self.browser = browser
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.addHandler(console_handler)
        self.timeout = 15

    @log_exception('Failed open URL: {}')
    def open(self, url):
        self.browser.visit(url)
        self.logger.info('Opened URL: {}'.format(url))

    @log_exception('Failed found form name: {}')
    def fill_from(self, name, value):
        form_string = name + ' ' + value
        self.browser.fill(name, value)
        self.logger.info('Fill the form name: {}'.format(form_string))

    @log_exception('Failed to get web element with by_selector: {}')
    def _get_elements(self, *locator, expected_condition=all_elements_located, wait=None):
        if wait is None:
            wait = self.timeout

        wd_wait = WebDriverWait(self.browser.driver, wait)
        element = wd_wait.until(expected_condition(locator))

        if element:
            by_selector = locator[0] + ' ' + locator[1]
            self.logger.info('Got web elements of: {}'.format(by_selector))
        return element

    @log_exception('Failed to get web element with by_selector: {}')
    def _get_element(self, *locator, expected_condition=element_located, wait=None):
        if wait is None:
            wait = self.timeout

        wd_wait = WebDriverWait(self.browser.driver, wait)
        element = wd_wait.until(expected_condition(locator))

        if element:
            by_selector = locator[0] + ' ' + locator[1]
            self.logger.info('Got web element of:{}'.format(by_selector))
        return element

    def get_web_elements(self, *locator):
        self._get_elements(*locator)
        elements = self.browser.driver.find_elements(*locator)
        return elements

    def get_web_element(self, *locator):
        self._get_element(*locator)
        element = self.browser.driver.find_element(*locator)
        return element

    @log_exception('Failed to mouse over web element with by_selector: {}')
    def mouse_over_click(self, *locator):
        by_selector = locator[0] + '  ' + locator[1]
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(self.get_web_element(*locator)).perform()
        self.click_webelement(*locator)
        self.logger.info('Mouse over web element with by_selector: {}'.format(by_selector))

    def click_webelement(self, *locator):
        self._get_element(*locator, expected_condition=element_clickable).click()

    def wait(self, seconds=3):
        self.browser.driver.implicitly_wait(seconds)

    def get_text(self, *locator):
        return self.get_web_element(*locator).text

    def current_url_str(self):
        return str(self.browser.driver.current_url)

    def get_current_url(self):
        return self.browser.driver.current_url




