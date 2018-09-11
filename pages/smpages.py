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
        self.fill_from(self.locators.name, username)
        self.fill_from(self.locators.password, password)
        login_button = self.get_web_element(*self.locators.login)
        login_button.click()

    def signout(self):
        menu_icon = self.get_web_element(*self.locators.menu)
        menu_icon.click()
        signout_button = self.get_web_element(*self.locators.signout)
        signout_button.click()




