#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from base.base_page import BasePage
from locators.smlocators import SMLocators


class SMPages(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SMLocators

    # login signout page
    def login(self, username, password):
        self.browser.fill(self.locators.name, username)
        self.browser.fill(self.locators.password, password)
        login_button = self.browser.find_by_css(self.locators.login)
        login_button.click()

    def logout(self):
        pass

    def menu_icon(self):
        return self.browser.find_by_css(self.locator.menu).first

    def signout_button(self):
        return self.browser.find_by_css(self.locator.signout).first


