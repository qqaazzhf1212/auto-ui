import os
import time

import pytest
from common.tools import get_opts
import settings

if __name__ == '__main__':
    args = ['-s', '-v', '--alluredir=results/reports', settings.TEST_CASE_DIR]
    arg_mark = get_opts('-m')
    default_arg_mark = 'smoke'

    # 手动运行标记的用例
    if arg_mark:
        args.insert(0, '-m {}'.format(arg_mark))
    else:
        args.insert(0, '-m {}'.format(default_arg_mark))

    # 手动运行执行用例的浏览器
    arg_driver = get_opts('--browser')
    if arg_driver:
        args.insert(0, '--browser={}'.format(arg_driver))

    print(args)
    pytest.main(args)

    time.sleep(3)
    os.system("allure generate reports/report_web -o results/reports/allures-web --clean")