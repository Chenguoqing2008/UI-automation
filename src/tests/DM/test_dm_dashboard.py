#! /usr/bin/python3
# _*_ coding:utf-8 _*_


from pages.dmpages import DMPages as DMDashBoardPage
import pytest
from hamcrest import *
from base.util import Logging


class TestDMDashBoardTest(Logging):

    dashboard_title = "DASHBOARD"
    login_text = "login"

    @pytest.fixture()
    def dmdashboard(self):
        dmdashboard = DMDashBoardPage(self.browser)
        return dmdashboard

    def test_dm_login(self, dmdashboard):
        url = self.config['DM']['URL']
        username = self.config['DM']['username']
        password = self.config['DM']['password']
        dmdashboard.open(url)
        dmdashboard.login(username, password)
        assert_that(dmdashboard.dashboard_text(), equal_to(self.dashboard_title))

    def test_dm_signout(self, dmdashboard):
        dmdashboard.signout()
        assert_that(dmdashboard.current_url_str(), contains_string(self.login_text))


