#! /usr/bin/python3
# _*_ coding:utf-8 _*_


import unittest
from splinter.browser import Browser
from pages.impages import IMPages as IMMaindPage
from utilities import util


class IMMainPageTest(unittest.TestCase):

    config = util.getConfig()

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('chrome')
        cls.browser.driver.maximize_window()
        cls.immainpage = IMMaindPage(cls.browser)
        # cls.logger = logging.getLogger(cls.__class__.__name__)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def test_im_login(self):
        qa_url = __class__.config['QA']['IM']['URL']
        username = self.config['QA']['IM']['username']
        password = self.config['QA']['IM']['password']
        self.immainpage.open(qa_url)
        self.immainpage.login(username, password)

    def test_im_logout(self):
        self.immainpage.logout()

