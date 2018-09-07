#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from locators.imlocators import IMLocators
from utilities import util
from base.precondition import PreEnv
import time


class IMMainPage(PreEnv):
    config = util.getConfig()

    def test_im_login(self):
        qa_url = __class__.config['QA']['IM']['URL']
        username = self.config['QA']['IM']['username']
        password = self.config['QA']['IM']['password']
        self.browser.visit(qa_url)
        self.browser.fill(IMLocators.name, username)
        self.browser.fill(IMLocators.password, password)
        self.browser.find_by_css(IMLocators.login).first.click()
        time.sleep(5)

    def test_im_logout(self):
        self.browser.find_by_css(IMLocators.logouticon).first.click()
        self.browser.find_by_id(IMLocators.logout).first.click()

