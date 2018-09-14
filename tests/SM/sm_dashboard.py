#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from pages.smpages import SMPages as SMDashBoardPage
import pytest


class TestSMDashBoard:

    @pytest.fixture()
    def smdashboard(self):
        smdashboard = SMDashBoardPage(self.browser)
        return smdashboard

    def test_sm_login(self, smdashboard):
        url = self.config['SM']['URL']
        username = self.config['SM']['username']
        password = self.config['SM']['password']
        smdashboard.open(url)
        smdashboard.login(username, password)

    def test_sm_signout(self, smdashboard):
        smdashboard.signout()



