#! /usr/bin/python3
# _*_ coding:utf-8 _*_


from pages.dmpages import DMPages as DMDashBoardPage


class TestDMDashBoardTest:

    def test_dm_login(self):
        url = self.config['DM']['URL']
        username = self.config['DM']['username']
        password = self.config['DM']['password']
        self.dmdashboard = DMDashBoardPage(self.browser)
        self.dmdashboard.open(url)
        self.dmdashboard.login(username, password)

    def test_dm_signout(self):
        self.dmdashboard = DMDashBoardPage(self.browser)
        self.dmdashboard.signout()


