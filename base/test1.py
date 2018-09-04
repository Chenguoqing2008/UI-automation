import pytest


# @pytest.fixture
# def admin_browser(browser_instance_getter):
#     return browser_instance_getter(admin_browser)
#
#
# def test_with_several_browsers(browser, admin_browser):
#     # browser.visit('http://www.google.com')
#     admin_browser.visit('http://www.google.com')
#     assert admin_browser.url == "http://www.google.com"

from splinter import Browser

executable_path = {'executable_path': "C:\\Users\\18504\Desktop\\staffum-ui-automation\\utilities\\chromedriver.exe"}
admin_browser = Browser('chrome', **executable_path)


# @pytest.fixture
# def browser(request, browser_instance_getter):
#     """Browser fixture."""
#     return browser_instance_getter(request, browser)


# @pytest.fixture
# def admin_browser(request, browser_instance_getter):
#     executable_path2 = {'executable_path':
#                         "C:\\Users\\18504\Desktop\\staffum-ui-automation\\utilities\\chromedriver.exe"}
#     admin_browser = Browser('chrome', **executable_path2)
#     return browser_instance_getter(request, admin_browser)


def test_browser():
    admin_browser.visit('http://www.baidu.com')
    assert admin_browser.url == 'http://www.baidu.com'

# def test_with_several_browsers(browser, admin_browser):
#     browser.visit('http://www.google.com')
#     admin_browser.visit('http://www.baidu.com')
    # assert browser.url == 'http://example.com'

# executable_path = {'executable_path': "C:\\Users\\18504\Desktop\\staffum-ui-automation\\utilities\\chromedriver.exe"}
#
# browser = Browser('firefox', **executable_path)
# url = "http://www.google.com"
# browser.visit(url)
#
# with Browser() as browser:
#     # Visit URL
#     url = "http://www.google.com"
#     browser.visit(url)
#     browser.fill('q', 'splinter - python acceptance testing for web applications')
#     # Find and click the 'search' button
#     button = browser.find_by_name('btnG')
#     # Interact with elements
#     button.click()
#     if browser.is_text_present('splinter.readthedocs.io'):
#         print("Yes, the official website was found!")
#     else:
#         print("No, it wasn't found... We need to improve our SEO techniques")
