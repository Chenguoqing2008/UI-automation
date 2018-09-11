#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from selenium.webdriver.common.by import By


class SALocators:

    # login
    name = "username"
    password = "password"
    login = (By.CSS_SELECTOR, ".form-group button")

    # logout
    moreicon = (By.CSS_SELECTOR, ".tabbar a:nth-child(4)")
    logout = (By.CSS_SELECTOR, ".more-page  div:nth-child(5) >div")


