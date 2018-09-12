#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import unittest
from splinter.browser import Browser
from selenium.webdriver.chrome.options import Options
from pages.smpages import SMPages as SMDashBoardPage
from utilities import util
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

class SMDashBoardTest(unittest.TestCase):

    config = util.getConfig()
    remote_server_url = 'http://192.168.0.115:4444/wd/hub'

    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("headless")
        capabilities = chrome_options.to_capabilities()
        cls.browser = Browser(
                             driver_name="remote",
                             url=cls.remote_server_url,
                             browser='chrome',
                             desired_capabilities=capabilities)

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

    def test_sm_signout(self):
        self.smdashboard.signout()



