#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from base.base_page import BasePage
from locators.imlocators import IMLocators


class IMPages(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = IMLocators

    # login logout page
    def login(self, username, password):
        self.fill_from(self.locators.name, username)
        self.fill_from(self.locators.password, password)
        self.click_webelement(*self.locators.login)

    def immainpage_icon_text(self):
        return self.get_text(*self.locators.im_icon)

    def logout(self):
        self.click_webelement(*self.locators.account_icon)
        self.mouse_over_click(*self.locators.logout)
        self.wait()


