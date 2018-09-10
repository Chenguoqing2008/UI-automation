#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from locators.dmlocators import DMLocators
from utilities import util
from base.base_page import PreEnv
import time


class DMDashBoardPage(PreEnv):
    config = util.getConfig()

    def test_dm_dashboard_login(self):
        qa_url = __class__.config['QA']['DM']['URL']
        username = self.config['QA']['DM']['username']
        password = self.config['QA']['DM']['password']
        self.browser.visit(qa_url)
        self.browser.fill(DMLocators.name, username)
        self.browser.fill(DMLocators.password, password)
        self.browser.find_by_id(DMLocators.login).first.click()
        time.sleep(5)

    def test_dm_dashboard_logout(self):
        self.browser.find_by_css(DMLocators.menu).first.click()
        self.browser.find_by_css(DMLocators.signout).first.click()

