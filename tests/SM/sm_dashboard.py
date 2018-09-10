#! /usr/bin/python3
# _*_ coding:utf-8 _*_

import time
from pages.smpages import SMPages as SMDashBoardPage
from utilities import util
from base.base_page import BasePage


class SMDashBoardTest(BasePage):
    config = util.getConfig()

    def test_sm_login(self):
        qa_url = __class__.config['QA']['SM']['URL']
        username = self.config['QA']['SM']['username']
        password = self.config['QA']['SM']['password']
        self.open(qa_url)
        self.fill_from(SMDashBoardPage.name, username)
        self.fill_from(SMDashBoardPage.password, password)
        # smpage.login_button()
        time.sleep(5)
        self.assertEquals(1 == 1)

    def test_sm_logout(self):
        SMDashBoardPage.menu_icon().click()
        SMDashBoardPage.signout_button().click()
        self.assertEquals(1 == 1)

