#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from locators.smlocator import SMLocator
from utilities import util
from base.precondition import PreEnv


class SMDashBoardPage(PreEnv):
    config = util.getConfig()

    def test_sm_dashboard_login(self):
        qa_url = __class__.config['QA']['SM']['URL']
        username = self.config['QA']['SM']['username']
        password = self.config['QA']['SM']['password']
        self.browser.visit(qa_url)
        self.browser.fill(SMLocator.name, username)
        self.browser.fill(SMLocator.password, password)
        self.browser.find_by_id(SMLocator.login).first.click()

    def test_sm_dashboard_logout(self):
        self.browser.find_by_css(SMLocator.menu).first.click()
        self.browser.find_by_css(SMLocator.signout).first.click()

