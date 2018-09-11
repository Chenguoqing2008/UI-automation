#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from base.base_page import BasePage
from locators.imlocators import IMLocators


class DMPages(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.locators = IMLocators

    # login logout page
    def login(self, username, password):
        self.fill_from(self.locators.name, username)
        self.fill_from(self.locators.password, password)
        login_button = self.get_web_element(*self.locators.login)
        login_button.click()

    def logout(self):
        menu_icon = self.get_web_element(*self.locators.logouticon)
        menu_icon.click()
        signout_button = self.get_web_element(*self.locators.logout)
        signout_button.click()
