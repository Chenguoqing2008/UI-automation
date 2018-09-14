#! /usr/bin/python3
# _*_ coding:utf-8 _*_


from pages.sapages import SAPages as SAHomePage
import pytest


class TestSAHomePage:

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

    def test_sa_signout(self, sahomepage):
        sahomepage.signout()

