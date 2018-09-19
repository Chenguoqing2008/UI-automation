#! /usr/bin/python3
# _*_ coding:utf-8 _*_

from selenium.webdriver.common.by import By


class IMLocators:

    # login
    name = "email"
    password = "password"
    login = (By.CSS_SELECTOR, ".input-field button")
    im_icon = (By.CSS_SELECTOR, ".brand-logo")

    # logout
    account_icon = (By.CSS_SELECTOR, "#nav-mobile > li:nth-child(4)  span")
    logout = (By.ID, "logout")


