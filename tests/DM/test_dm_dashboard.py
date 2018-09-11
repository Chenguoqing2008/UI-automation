#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import time
import unittest

from splinter.browser import Browser

from pages.dmpages import DMPages as DMDashBoardPage
from utilities import util


class DMDashBoardTest(unittest.TestCase):

    config = util.getConfig()

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('chrome')
        cls.browser.driver.maximize_window()
        cls.dmdashboard = DMDashBoardPage(cls.browser)
        # cls.logger = logging.getLogger(cls.__class__.__name__)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_dm_login(self):
        qa_url = __class__.config['QA']['DM']['URL']
        username = self.config['QA']['DM']['username']
        password = self.config['QA']['DM']['password']
        self.dmdashboard.open(qa_url)
        self.dmdashboard.login(username, password)
        time.sleep(5)

    def test_dm_signout(self):
        self.dmdashboard.signout()
        # assert 1 == 2

