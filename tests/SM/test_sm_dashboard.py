#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from pages.smpages import SMPages as SMDashBoardPage
import pytest
from hamcrest import *


class TestSMDashBoard:

    dashboard_title = "DASHBOARD"
    login_text = "login"

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
        assert_that(smdashboard.dashboard_text(), equal_to(self.dashboard_title))

    def test_sm_signout(self, smdashboard):
        smdashboard.signout()
        assert_that(smdashboard.current_url_str(), contains_string(self.login_text))



