#! /usr/bin/python3
# _*_ coding:utf-8 _*_


from pages.impages import IMPages as IMMaindPage


class TestIMMainPageTest:

    def test_im_login(self):
        url = self.config['IM']['URL']
        username = self.config['IM']['username']
        password = self.config['IM']['password']
        self.immainpage = IMMaindPage(self.browser)
        self.immainpage.open(url)
        self.immainpage.login(username, password)

    def test_im_logout(self):
        self.immainpage = IMMaindPage(self.browser)
        self.immainpage.logout()

