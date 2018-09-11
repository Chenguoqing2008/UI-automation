#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import time
import unittest

from splinter.browser import Browser

from pages.smpages import SMPages as SMDashBoardPage
from utilities import util


class SMDashBoardTest(unittest.TestCase):

    config = util.getConfig()

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('chrome')
        cls.browser.driver.maximize_window()
        cls.smdashboard = SMDashBoardPage(cls.browser)
        # cls.logger = logging.getLogger(cls.__class__.__name__)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_sm_login(self):
        qa_url = __class__.config['QA']['SM']['URL']
        username = self.config['QA']['SM']['username']
        password = self.config['QA']['SM']['password']
        self.smdashboard.open(qa_url)
        self.smdashboard.login(username, password)
        time.sleep(5)

    def test_sm_signout(self):
        self.smdashboard.signout()
        # assert 1 == 2



