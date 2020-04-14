# 1. 创建测试套件
import time
import unittest

from script.cart_case import TestCart
from script.login_case import TestLogin
from tools.HTMLTestRunner import HTMLTestRunner
from utils import DriverUtil

suite = unittest.TestSuite()
# 2. 给套件添加测试用例
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestCart))

# 关闭 自动退出驱动开关
DriverUtil.kaiguan = False

# 3. 实例化一个运行器对象(HTMLTestRunner)
#    1. 报告文件流 -- 报告文件名字 -- 加入时间字符串
report_name = "./report/report{}.html".format(time.strftime("%Y%m%d%H%M%S"))

#    2. 报告标题
report_title = "TPshop自动化测试报告"
#    3. 报告描述
report_description = "操作系统:win10"

with open(report_name, "wb") as f:
    runner = HTMLTestRunner(stream=f, title=report_title, description=report_description)
    # 4. 运行器执行套件
    runner.run(suite)

# 打开自动退出驱动开关  退出驱动
DriverUtil.kaiguan = True
DriverUtil.quit_driver()
