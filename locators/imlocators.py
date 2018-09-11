#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from selenium.webdriver.common.by import By


class IMLocators:

    # login
    name = "email"
    password = "password"
    login = (By.CSS_SELECTOR, ".input-field button")

    # logout
    logouticon = (By.CSS_SELECTOR, ".dropdown-button")
    logout = (By.ID, "logout")


