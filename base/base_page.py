#! /usr/bin/python3
# _*_ coding:utf-8 _*_

"""Inspired by  oleg-toporkov in github"""

__author__ = "Robin Chen"

import unittest
from splinter import Browser
import logging
from base.decorators import log_exception


class BasePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('chrome')
        cls.browser.driver.maximize_window()
        cls.logger = logging.getLogger(cls.__class__.__name__)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    @log_exception('Failed open URL: {}')
    def open(self, url):
        self.browser.visit(url)
        self.logger.info('Opened URL: {}'.format(url))

    @log_exception('Failed found form name: {}')
    def fill_from(self, name, value):
        self.browser.fill(name, value)
        self.logger.info('Fill the form name: {}'.format(name))

