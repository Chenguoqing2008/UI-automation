#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from locators.smlocators import SMLocators
from utilities import util
from base.precondition import PreEnv
import time


class SMDashBoardPage(PreEnv):
    config = util.getConfig()

    def test_sm_login(self):
        qa_url = __class__.config['QA']['SM']['URL']
        username = self.config['QA']['SM']['username']
        password = self.config['QA']['SM']['password']
        self.browser.visit(qa_url)
        self.browser.fill(SMLocators.name, username)
        self.browser.fill(SMLocators.password, password)
        self.browser.find_by_id(SMLocators.login).first.click()
        time.sleep(5)

    def test_sm_logout(self):
        self.browser.find_by_css(SMLocators.menu).first.click()
        self.browser.find_by_css(SMLocators.signout).first.click()

