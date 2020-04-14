# 创建测试类
import json
import time
import unittest

from config import BASE_DIR
from page.cart_page import CartProxy
from page.index_page import IndexProxy
from page.my_order_list_page import MyOrderProxy
from page.order_pay_page import OrderPayProxy
from page.order_submit_page import OrderSubmitProxy
from utils import DriverUtil

from parameterized import parameterized


def get_order_submit_data():
    # 保存测试数据的列表
    result = []
    # 读取json数据 构造数据格式 [[],[],[]]  [(),(),()]
    with open(BASE_DIR + "/data/order.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
        #  test_order_submit  索引 为 0
        d = data[0]
        expect = d.get("expect")
        result.append((expect,))
    # 返回测试数据
    print("test_order_submit:", result)
    return result

def get_order_pay_data():
    # 保存测试数据的列表
    result = []
    # 读取json数据 构造数据格式 [[],[],[]]  [(),(),()]
    with open(BASE_DIR + "/data/order.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
        #  test_order_pay  索引 为 1
        d = data[1]
        expect = d.get("expect")
        result.append((expect,))
    # 返回测试数据
    print("test_order_pay:", result)
    return result


# 测试类
class TestOrder(unittest.TestCase):

    # fixture
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtil.get_driver()
        # 页面对象 -- 业务层 首页 购物车 提交订单页
        cls.index_proxy = IndexProxy()
        cls.cart_proxy = CartProxy()
        cls.order_submit_proxy = OrderSubmitProxy()

        cls.my_order_proxy = MyOrderProxy()
        cls.order_pay_proxy = OrderPayProxy()

    def setUp(self):
        # 打开首页
        self.driver.get("http://localhost")

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    # 测试方法,断言
    @parameterized.expand(get_order_submit_data)
    def test01_order_submit(self, expect):
        # 1.进入购物车页面
        self.index_proxy.to_cart_page()
        # 2.点击"全选"选中所有商品
        # 3.点击"去结算"按钮
        self.cart_proxy.go_balance()
        # 4.进入填写核对订单页面
        # 5.点击"提交订单"按钮
        time.sleep(5)
        self.order_submit_proxy.submit_order()

        # 判断提交结果
        time.sleep(5)
        msg = self.order_submit_proxy.get_submit_result()
        self.assertIn(expect, msg)



    @parameterized.expand(get_order_pay_data)
    def test02_order_pay(self,expect):
        # 1.点击"我的订单"
        self.index_proxy.to_my_order_page()
        # 2.进入后台订单管理页面
        # 3.点击"待付款"
        # 4.点击"立即支付"
        # 切换到新窗口中+++++++++++++
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.my_order_proxy.go_pay()

        # 5.进入订单支付页面
        # 6.选择"货到付款"
        # 7.点击"确认支付方式"
        # 切换到新窗口中+++++++++++++
        time.sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.order_pay_proxy.confirm_pay_way()

        # 获取支付的结果 判断是否符合预期
        time.sleep(5)
        msg = self.order_pay_proxy.get_submit_result()
        self.assertIn(expect, msg)

# 参数化,数据驱动
