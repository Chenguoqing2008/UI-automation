#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from selenium.webdriver.common.by import By


class DMLocators:

    # login
    name = "username"
    password = "password"
    login = (By.ID, "login")

    # logout
    menu = (By.CSS_SELECTOR, "md-toolbar.main-toolbar button")
    signout = (By.CSS_SELECTOR, "md-toolbar > div > button")

