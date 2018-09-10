#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from base.base_page import BasePage
from locators.smlocators import SMLocators


class SMPages(BasePage):

    # def __init__(self):
    #     self.browser = __class__.browser

    # login
    name = "username"
    password = "password"
    login = "login"

    # logout
    menu = "md-toolbar.main-toolbar button"
    signout = "md-toolbar > div > button"

    # login signout page
    def login_button(self):
        return self.browser.driver.find_element_by_css_selector(SMLocators.login).click()

    def menu_icon(self):
        return self.browser.find_by_css(SMLocators.menu).first

    def signout_button(self):
        return self.browser.find_by_css(SMLocators.signout).first


