#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from selenium.webdriver.common.by import By


class SMLocators:

    # login
    name = "username"
    password = "password"
    login = (By.ID, "login")
    dashboard = (By.CSS_SELECTOR, "md-toolbar > div > h2")

    # logout
    menu = (By.CSS_SELECTOR, "md-toolbar.main-toolbar button")
    signout = (By.CSS_SELECTOR, "md-toolbar > div > button")


