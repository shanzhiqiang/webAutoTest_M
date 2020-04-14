import time
import unittest

from config import BASE_DIR
from script.cart_case import TestCart
from script.login_case import TestLogin

# 测试套件
from script.order_case import TestOrder
from tools.HTMLTestRunner import HTMLTestRunner
from utils import DriverUtil

suite = unittest.TestSuite()

# 添加用例 -- 参数化后的 添加时使用类添加
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestCart))
suite.addTest(unittest.makeSuite(TestOrder))


# 执行前关闭退出不自动退出
DriverUtil.auto_quit = False

# 创建运行器 -- TextTestRunner(调试)   HTMLTestRunner(执行)
# runner = HTMLTestRunner(报告文件流, 报告标题, 报告描述)


# 执行后开启退出,手动退出驱动
DriverUtil.auto_quit = True
DriverUtil.quit_driver()
