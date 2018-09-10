#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

"""Inspired by  oleg-toporkov in github"""
"""Inspired by  Marcin Koprek in github"""

__author__ = "Robin Chen"


class BasePage(object):

    def __init__(self, browser):
        self.browser = browser
        self.timeout = 5

    # @log_exception('Failed open URL: {}')
    def open(self, url):
        self.browser.visit(url)
        # self.logger.info('Opened URL: {}'.format(url))

    # @log_exception('Failed found form name: {}')
    def fill_from(self, name, value):
        self.browser.fill(name, value)
        # self.logger.info('Fill the form name: {}'.format(name))

    # @log_exception('Failed to get web element with xpath: {}')
    # def _get_element(self, expected_condition=expected_conditions.presence_of_element_located, *location, wait=None):
    #     if wait is None:
    #         wait = self.timeout
    #
    #     if isinstance(element, str):
    #         self.logger.debug('Waiting {} seconds for web element with condition: {}'
    #                           .format(wait, expected_condition.__name__))
    #
    #         wd_wait = WebDriverWait(self.browser, wait)
    #         element = wd_wait.until(expected_condition(*location))
    #
    #     if element:
    #         self.logger.debug('Got web element!')
    #
    #         if Config.HIGHLIGHT:
    #             self._highlight(element)
    #
    #     return element

