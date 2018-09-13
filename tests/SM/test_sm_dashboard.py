#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from pages.smpages import SMPages as SMDashBoardPage


class TestSMDashBoard:

    def test_sm_login(self):
        url = self.config['SM']['URL']
        username = self.config['SM']['username']
        password = self.config['SM']['password']
        self.smdashboard = SMDashBoardPage(self.browser)
        self.smdashboard.open(url)
        self.smdashboard.login(username, password)

    def test_sm_signout(self):
        self.smdashboard = SMDashBoardPage(self.browser)
        self.smdashboard.signout()



