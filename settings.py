import os

# 根项目目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 测试用例路径
TEST_CASE_DIR = os.path.join(BASE_DIR, 'test_cases')

# 错误图片位置
SCREENSHOT_DIR = os.path.join(BASE_DIR, 'results/screenshot')

# 项目域名
PROJECT_HOST = 'XXX'

# 登录配置
INTESTFACE = {
    'login': 'login'
}

# 日志配置
LOG_CONFIG = {
    'name': 'pyui',
    'filename': os.path.join(BASE_DIR, 'results/logs/pyui.log'),
    'mode': 'a',
    'encoding': 'utf-8',
    'debug': True
}

# 账号信息
TEST_NORMAL_USERNAME = 'admin'
TEST_NORMAL_PASSWRRD = 123456

# 全局查找元素等等时间
DEFAULT_TIOMEOUT = 5

BROWSER_DRIVER = {
    'chrome': os.path.join(BASE_DIR, 'drivers', 'chromedriver_103.exe'),
    'firefox': os.path.join(BASE_DIR, 'drivers', 'geckodriver_102.exe'),
    'edge': os.path.join(BASE_DIR, 'drivers', 'msedgedriver_103.exe')
}
