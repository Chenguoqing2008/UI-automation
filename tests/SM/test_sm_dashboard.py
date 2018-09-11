#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import unittest
from splinter.browser import Browser
from selenium import webdriver
from pages.smpages import SMPages as SMDashBoardPage
from utilities import util


class SMDashBoardTest(unittest.TestCase):

    config = util.getConfig()
    remote_server_url = 'http://YOUR_SAUCE_USERNAME:YOUR_SAUCE_ACCESS_KEY@ondemand.saucelabs.com:80/wd/hub'

    @classmethod
    def setUpClass(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--headless")
        # cls.browser = Browser('chrome', options=chrome_options)
        cls.browser = Browser(
            #driver_name="remote",
             #                 url=cls.remote_server_url,
                              'chrome',
                              # name='Test chrome in headless mode',
                              options=chrome_options
                              )
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

    def test_sm_signout(self):
        self.smdashboard.signout()



