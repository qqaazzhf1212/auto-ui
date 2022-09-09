from page_locators.login_page_locs import HomePageLocators as loc
from page_objects.base_page import BasePage


class HomePage(BasePage):
    name = 'Home页面'

    # 定位信息被放在雷属性中
    def home_info(self):
        return self.wait_element_is_visible(locator=loc.Home_info_locator, action='首页信息', timeout=60)
