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
        self.click_webelement(*self.locators.login)

    def home_text(self):
        return self.get_text(*self.locators.home)

    def signout(self):
        self.click_webelement(*self.locators.moreicon)
        self.click_webelement(*self.locators.logout)

