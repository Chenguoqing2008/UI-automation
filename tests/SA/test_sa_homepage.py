#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from locators.salocators import SALocators
from utilities import util
from base.base_page import PreEnv
import time


class SAHomePage(PreEnv):
    config = util.getConfig()

    def test_sa_login(self):
        qa_url = __class__.config['QA']['SA']['URL']
        username = self.config['QA']['SA']['username']
        password = self.config['QA']['SA']['password']
        self.browser.visit(qa_url)
        self.browser.fill(SALocators.name, username)
        self.browser.fill(SALocators.password, password)
        self.browser.find_by_css(SALocators.login).first.click()
        time.sleep(5)

    def test_sa_logout(self):
        self.browser.find_by_css(SALocators.moreicon).first.click()
        self.browser.find_by_css(SALocators.logout).first.click()

