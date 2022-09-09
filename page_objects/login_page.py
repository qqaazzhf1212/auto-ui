from page_locators.login_page_locs import LoginPageLocator as loc
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    '''
    把一个页面抽象成一个类，所有的这个页面上的功能封装成方法
    '''
    name = '登录功能'  # 页面名称

    # 定位信息被放在雷属性中
    def login(self, username, password, error_tip=None):
        # 1、输入用户名
        self.wait_element_is_visible(locator=loc.username_intut_locator, action='输入用户名').input_text(username)

        # 2.输入密码
        self.wait_element_is_visible(locator=loc.password_intut_locator, action='输入密码').input_text(password)

        # 3.点击登录
        self.wait_element_is_visible(locator=loc.login_btn_locator, action='点击登录按钮').click_element()

    # 提示错误信息
    def login_error_tip(self):
        return self.wait_element_is_visible(locator=loc.login_password_tips, action='登录错误信息提示').get_elenmet_text()
