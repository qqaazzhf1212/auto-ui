from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_cases.test_cases_api.base_case import BaseCase


class TestLogin(BaseCase):
    name = '登录功能'

    # xunit风格的前置
    @classmethod
    def setup_class(cls):
        cls.logger.info('============{}测试开始============='.format(cls.name))

    # xunit风格的后置
    @classmethod
    def teardown_class(cls):
        cls.logger.info('============{}测试结束============='.format(cls.name))

    def test_login_success(self, driver):
        # 1、访问登录页面
        driver.get(self.settings.PROJECT_HOST + self.settings.INTESTFACE['login'])
        # 2、输入用户名和密码
        # username=driver.find_element('xpath','//input[@type="text"]')
        # password=driver.find_element('xpath','//input[@type="password"]')
        # 2.1定位输入框
        wait = WebDriverWait(driver, timeout=3)
        username_intut = wait.until(
            EC.visibility_of_element_located(('xpath', '//input[@type="text"]'))
        )
        # 2.2输入用户名
        username_intut.send_keys(self.settings.TEST_NORMAL_USERNAME)
        # 2.3定位密码框
        wait = WebDriverWait(driver, timeout=3)
        password_intut = wait.until(
            EC.visibility_of_element_located(('xpath', '//input[@type="password"]'))
        )
        # 2.4输入密码
        password_intut.send_keys(self.settings.TEST_NORMAL_PASSWRRD)
        # 2.5定位登录按钮
        wait = WebDriverWait(driver, timeout=30)
        submit_intut = wait.until(
            EC.visibility_of_element_located(('xpath', '//span[text()="登 录"]'))
        )
        # 2.6点击登录按钮
        submit_intut.click()
        # 3断言是否登录成功
        assert wait.until(EC.visibility_of_element_located(('xpath', '//span[text()="首页"]')))
