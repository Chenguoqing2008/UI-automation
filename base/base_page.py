#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from splinter.browser import Browser

"""Inspired by  oleg-toporkov in github"""
"""Inspired by  Marcin Koprek in github"""

__author__ = "Robin Chen"


class BasePage(object):

    def __init__(self, browser):
        self.browser = browser
        # self.browser = Browser('chrome')
        self.timeout = 15

    # @log_exception('Failed open URL: {}')
    def open(self, url):
        self.browser.visit(url)
        # self.logger.info('Opened URL: {}'.format(url))

    # @log_exception('Failed found form name: {}')
    def fill_from(self, name, value):
        self.browser.fill(name, value)
        # self.logger.info('Fill the form name: {}'.format(name))

    # @log_exception('Failed to get web element with xpath: {}')
    def _get_elements(self, *locator, expected_condition=expected_conditions.presence_of_all_elements_located, wait=None):
        if wait is None:
            wait = self.timeout

        wd_wait = WebDriverWait(self.browser.driver, wait)
        element = wd_wait.until(expected_condition(locator))

        # if element:
        #     self.logger.debug('Got web element!')
        return element

    # @log_exception('Failed to get web element with xpath: {}')
    def _get_element(self, *locator, expected_condition=expected_conditions.presence_of_element_located, wait=None):
        if wait is None:
            wait = self.timeout

        wd_wait = WebDriverWait(self.browser.driver, wait)
        element = wd_wait.until(expected_condition(locator))

        # if element:
        #     self.logger.debug('Got web element!')
        return element

    def get_web_elements(self, *locator):
        self._get_elements(*locator)
        elements = self.browser.driver.find_elements(*locator)
        return elements

    def get_web_element(self, *locator):
        self._get_element(*locator)
        element = self.browser.driver.find_element(*locator)
        return element

