#! /usr/bin/python3
# _*_ coding:utf-8 _*_


from pages.impages import IMPages as IMMaindPage
import pytest


class TestIMMainPageTest:

    @pytest.fixture()
    def immainpage(self):
        immainpage = IMMaindPage(self.browser)
        return immainpage

    def test_im_login(self, immainpage):
        url = self.config['IM']['URL']
        username = self.config['IM']['username']
        password = self.config['IM']['password']
        immainpage.open(url)
        immainpage.login(username, password)

    def test_im_logout(self, immainpage):
        immainpage.logout()

