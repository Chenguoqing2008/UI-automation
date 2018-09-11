#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import time
import unittest

from splinter.browser import Browser

from pages.sapages import SAPages as SAHomePage
from utilities import util


class SAHomePageTest(unittest.TestCase):

    config = util.getConfig()

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('chrome')
        cls.browser.driver.maximize_window()
        cls.sahomepage = SAHomePage(cls.browser)
        # cls.logger = logging.getLogger(cls.__class__.__name__)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_sa_login(self):
        qa_url = __class__.config['QA']['SA']['URL']
        username = self.config['QA']['SA']['username']
        password = self.config['QA']['SA']['password']
        self.sahomepage.open(qa_url)
        self.sahomepage.login(username, password)
        time.sleep(5)

    def test_sa_signout(self):
        self.sahomepage.signout()
        # assert 1 == 2

