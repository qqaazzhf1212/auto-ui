import settings
from page_objects.home_page import HomePage
from .base_case import BaseCase
from page_objects.login_page import LoginPage

import pytest
from test_datas.login_data import success_cases, fail_cases


class TestLogin(BaseCase):
    name = '登录功能'

    @pytest.mark.fail
    @pytest.mark.parametrize('case', fail_cases)
    def test_login_fail(self, driver, case):

        '''测试登录失败'''
        # 1、打开登录页面
        driver.get(settings.PROJECT_HOST + settings.INTESTFACE['login'])
        lp = LoginPage(driver)
        # 2、登陆

        lp.login(**case['request_data'])
        # 3、错误信息
        assert case['error_tip'] == lp.login_error_tip()

    @pytest.mark.smoke
    @pytest.mark.parametrize('case', success_cases)
    def test_login_success(self, driver, case):
        self.logger.info('=========={}开始测试============'.format(case['title']))
        self.logger.info('=========={}开始测试============'.format(case['request_data']))
        '''测试登录成功'''
        # 1、打开登录页面
        driver.get(settings.PROJECT_HOST + settings.INTESTFACE['login'])
        lp = LoginPage(driver)
        # 2、登陆
        lp.login(**case['request_data'])
        # 3、断言是否登录成功
        hp = HomePage(driver)
        # 断言
        assert hp.home_info()
