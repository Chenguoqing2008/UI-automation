#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from base.basepage import BasePage


class LogIn(BasePage):

    def __init__(self, url, browser):
        self.url = url
        super(LogIn, self).__init__(browser)
