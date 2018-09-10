#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from selenium.webdriver.common.by import By


class SMLocators:

    # login
    name = (By.NAME, "name")
    password = (By.NAME, "password")
    login = (By.NAME, "login")

    # logout
    menu = "md-toolbar.main-toolbar button"
    signout = "md-toolbar > div > button"


