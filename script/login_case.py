# 创建测试类
import json
import logging
import time
import unittest

from config import BASE_DIR
from page.index_page import IndexProxy
from page.login_page import LoginProxy
from utils import DriverUtil
from parameterized import parameterized


# 读取构造数据
def get_data():
    # 1.准备测试数据结果列表
    result = []
    # 2.读取json文件 构造测试数据[[0,0,0],[1,3,4],[6,5,11]]
    # a.打开json文件 -- 读取数据
    with open(BASE_DIR + "/data/login.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
        # b.构造成 [[],[],[],[]]  [(),(),()]
        for d in data:
            username = d.get("username")
            password = d.get("password")
            verify_code = d.get("verify_code")
            expect = d.get("expect")
            result.append((username, password, verify_code, expect))

    # 3.返回测试数据列表
    logging.info("读取到的参数化数据{}".format(result))
    return result


# 测试类
class TestLogin(unittest.TestCase):

    # fixture
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtil.get_driver()
        # 首页业务层对象
        cls.index_proxy = IndexProxy()
        # 登录页业务层对象
        cls.login_proxy = LoginProxy()

    def setUp(self):
        # 打开首页
        self.driver.get("http://localhost")

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    # 测试方法,断言
    # 1. 测试数据用参数表示, 参数写在参数列表中
    # 2. 给测试用例添加参数化方法
    # 3. 把测试数据传递参数化方法[(),(),()]
    # @parameterized.expand([("13012345678", "123456", "8888", "我的账户")])
    @parameterized.expand(get_data)
    def test01_login(self, username, password, verify_code, expect):
        # print("useranme:{},password:{},verify_code:{},expect:{}".format(username, password, verify_code, expect))
        logging.info("参数化结果: useranme:{},password:{},verify_code:{},expect:{}".format(username, password, verify_code, expect))
        # 首页进入登录页  首页的业务层对象
        self.index_proxy.to_login_page()
        # 实现登录操作   登录页业务层对象
        self.login_proxy.login(username, password, verify_code)

        # 断言 页面标题中是否包含 "我的账户"  需要等几秒
        time.sleep(5)
        msg = self.driver.title
        print(msg)
        self.assertIn(expect, msg)

# 参数化,数据驱动
