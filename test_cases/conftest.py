import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import settings
from page_objects.login_page import LoginPage

chrome_options = Options()
chrome_options.add_argument("--headless")


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='browser name ，chrome，firefox')  # 坑 参数都是--小写


# 初始化driver
@pytest.fixture(scope='class')
def driver(pytestconfig):
    browser = pytestconfig.getoption('--browser')
    # options = chrome_options
    options = None

    if browser == 'firefox':
        browser_path = settings.BROWSER_DRIVER['firefox']
        with webdriver.Firefox(options=options, service=Service(browser_path)) as wd:
            # 最大化浏览器
            wd.maximize_window()
            yield wd

    elif browser == 'chrome':
        browser_path = settings.BROWSER_DRIVER['chrome']
        with webdriver.Chrome(options=options, service=Service(browser_path)) as wd:
            # 最大化浏览器
            wd.maximize_window()
            yield wd

    elif browser == 'edge':
        browser_path = settings.BROWSER_DRIVER['edge']
        with webdriver.Edge(options=options, service=Service(browser_path)) as wd:
            # 最大化浏览器
            wd.maximize_window()
            yield wd


# 登录
@pytest.fixture(scope='class')
def login_driver(driver):
    # 初始化话driver
    lp = LoginPage(driver)
    # 打开页面
    driver.get(lp.settings.PROJECT_HOST + lp.settings.INTESTFACE['login'])
    # 登录
    lp.login(lp.settings.TEST_NORMAL_USERNAME, lp.settings.TEST_NORMAL_PASSWRRD)
    yield driver
