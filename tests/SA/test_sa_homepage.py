#! /usr/bin/python3
# _*_ coding:utf-8 _*_


from pages.sapages import SAPages as SAHomePage
import pytest
from hamcrest import *
from base.util import Logging


class TestSAHomePage(Logging):

    sa_home_text = "HOME"
    login_text = "login"

    @pytest.fixture()
    def sahomepage(self):
        sahomepage = SAHomePage(self.browser)
        return sahomepage

    def test_sa_login(self, sahomepage):
        url = self.config['SA']['URL']
        username = self.config['SA']['username']
        password = self.config['SA']['password']
        sahomepage.open(url)
        sahomepage.login(username, password)
        assert_that(sahomepage.home_text(), equal_to(self.sa_home_text))

    def test_sa_signout(self, sahomepage):
        sahomepage.signout()
        assert_that(sahomepage.current_url_str(), contains_string(self.login_text))

