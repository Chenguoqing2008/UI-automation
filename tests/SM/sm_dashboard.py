#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import time
from pages.smpages import SMPages as SMDashBoardPage
from utilities import util
from base.base_page import BasePage
from pages.smpages import SMPages
from splinter.browser import Browser
import unittest


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
        self.assertEquals(1 == 1)
    #
    # def test_sm_logout(self):
    #     SMDashBoardPage.menu_icon().click()
    #     SMDashBoardPage.signout_button().click()
    #     self.assertEquals(1 == 1)

