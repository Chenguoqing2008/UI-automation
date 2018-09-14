#! /usr/bin/python3
# _*_ coding:utf-8 _*_


from pages.dmpages import DMPages as DMDashBoardPage
import pytest


class TestDMDashBoardTest:

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

    def test_dm_signout(self, dmdashboard):
        dmdashboard.signout()


