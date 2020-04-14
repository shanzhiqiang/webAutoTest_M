# 参数化,数据驱动
# 创建测试类
import json
import time
import unittest

from config import BASE_DIR
from page.goods_detail_page import GoodsDetailProxy
from page.goods_search_page import GoodsSearchProxy
from page.index_page import IndexProxy
from utils import DriverUtil
from parameterized import parameterized


# 读取json文件, 构造测试数据 [(),(),()]
def get_data():
    # 创建结果列表
    result = []
    # 读取JSON文件 构造测试数据
    # a.打开json文件 -- 读取到数据
    with open(BASE_DIR + "/data/cart.json", 'r', encoding="utf-8") as f:
        data = json.load(f)
        # b.取出数据构造测试数据结构[(),(),()]
        for d in data:
            goods_name = d.get("goods_name")
            expect = d.get("expect")
            result.append((goods_name, expect))

    # 返回结果列表
    print(result)
    return result


class TestCart(unittest.TestCase):

    # fixture
    @classmethod
    def setUpClass(cls):
        # 获取浏览器驱动对象
        cls.driver = DriverUtil.get_driver()
        # 首页的业务层对象
        cls.index_proxy = IndexProxy()
        # 商品列表的业务层对象
        cls.goods_search_proxy = GoodsSearchProxy()
        # 商品详情页的业务层对象
        cls.goods_detail_proxy = GoodsDetailProxy()

    def setUp(self):
        # 打开首页
        self.driver.get("http://localhost")

    def tearDown(self):
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        DriverUtil.quit_driver()

    # 创建测试方法,断言
    # 1. 测试数据用参数表示, 参数写在参数列表中
    # 2. 给测试用例添加参数化方法
    # 3. 把测试数据传递参数化方法
    @parameterized.expand(get_data)
    def test01_cart(self, keys, expect):
        # keys = "小米"
        # 首页的业务层对象
        self.index_proxy.search_goods(keys)
        # 商品列表的业务层对象
        self.goods_search_proxy.to_goods_detail_page(keys)
        # 商品详情页的业务层对象
        self.goods_detail_proxy.join_goods_to_cart()

        # 获取加入购物车的结果  对结果断言
        time.sleep(5)
        # 子页中
        # 主页 --> 子页 dirver.switch_to.frame(iframe_id_name_element)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        msg = self.goods_detail_proxy.get_join_result()
        self.assertIn(expect, msg)

# 参数化,数据驱动
