#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from base.base_page import BasePage
from locators.salocators import SALocators


class SAPages(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = SALocators

    # login signout page
    def login(self, username, password):
        self.fill_from(self.locators.name, username)
        self.fill_from(self.locators.password, password)
        login_button = self.get_web_element(*self.locators.login)
        login_button.click()

    def signout(self):
        more_icon = self.get_web_element(*self.locators.moreicon)
        more_icon.click()
        logout_button = self.get_web_element(*self.locators.logout)
        logout_button.click()
