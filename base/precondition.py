#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import unittest
from splinter import Browser
import logging
import os
import platform


class PreEnv(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        chrome_driver_path = cls._getDriverPath()
        executable_path = {'executable_path': chrome_driver_path}
        cls.browser = Browser('chrome', **executable_path)
        cls.browser.driver.maximize_window()
        cls.logger = logging.getLogger(cls.__class__.__name__)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    @staticmethod
    def _getDriverPath():
        home_path = os.path.abspath(os.pardir)
        if 'Ubuntu' in platform.platform() or 'Darwin' in platform.platform():
            chrome_driver_path = os.path.join(os.path.join(home_path, 'utilities'), 'chromedriver')
        else:
            chrome_driver_path = os.path.join(os.path.join(home_path, 'utilities'), 'chromedriver.exe')
        return chrome_driver_path

