#! /usr/bin/python3
# _*_ coding:utf-8 _*_


from pages.sapages import SAPages as SAHomePage


class TestSAHomePage:

    def test_sa_login(self):
        url = self.config['SA']['URL']
        username = self.config['SA']['username']
        password = self.config['SA']['password']
        self.sahomepage = SAHomePage(self.browser)
        self.sahomepage.open(url)
        self.sahomepage.login(username, password)

    def test_sa_signout(self):
        self.sahomepage = SAHomePage(self.browser)
        self.sahomepage.signout()

