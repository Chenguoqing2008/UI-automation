#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from base.base_page import BasePage
from locators.dmlocators import DMLocators


class DMPages(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = DMLocators

    # login signout page
    def login(self, username, password):
        self.fill_from(self.locators.name, username)
        self.fill_from(self.locators.password, password)
        self.click_webelement(*self.locators.login)

    def dashboard_text(self):
        return self.get_text(*self.locators.dashboard)

    def signout(self):
        self.click_webelement(*self.locators.menu)
        self.mouse_over_click(*self.locators.signout)
        self.wait()

