#! /usr/bin/python3
# _*_ coding:utf-8 _*_


from pages.impages import IMPages as IMMaindPage
import pytest
from hamcrest import *
from base.util import Logging


class TestIMMainPageTest(Logging):

    IM_mainpage_text = "Percolata Integration Manager"
    login_text = "login"

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
        assert_that(immainpage.immainpage_icon_text(), equal_to(self.IM_mainpage_text))

    def test_im_logout(self, immainpage):
        immainpage.logout()
        assert_that(immainpage.current_url_str(), contains_string(self.login_text))

