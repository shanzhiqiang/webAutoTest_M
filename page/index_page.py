from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle

# 对象库层
from utils import DriverUtil


class IndexPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        super().__init__()
        # 页面元素定位信息
        self.denglu = (By.LINK_TEXT, "登录")
        self.search_input = (By.ID, "q")
        self.search_btn = (By.CLASS_NAME, "ecsc-search-button")

        # div-我的购物车
        self.my_cart = (By.ID, "hd-my-cart")
        # 超链接-我的订单
        self.my_order = (By.LINK_TEXT, "我的订单")

    # 定位登录超链接
    def find_login_link(self):
        return self.base_find_element(self.denglu)

    # 定位搜索输入框
    def find_search_input(self):
        return self.base_find_element(self.search_input)

    # 定位搜索按钮
    def find_search_btn(self):
        return self.base_find_element(self.search_btn)

    # 定位我的购物车
    def find_my_cart(self):
        return self.base_find_element(self.my_cart)

    # 定位我的订单超链接
    def find_my_order(self):
        return self.base_find_element(self.my_order)


# 操作层
class IndexHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.index_page = IndexPage()

    # 点击登录超链接
    def click_login_link(self):
        self.index_page.find_login_link().click()

    # 输入框搜索 -- 参数-搜索关键字
    def input_search_text(self, text):
        self.index_page.find_search_input().send_keys(text)

    # 点击搜索按钮
    def click_search_btn(self):
        self.index_page.find_search_btn().click()

    # 点击我的购物车
    def click_my_cart(self):
        self.index_page.find_my_cart().click()

    # 点击我的订单
    def click_my_order(self):
        self.index_page.find_my_order().click()


# 业务层
class IndexProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.index_handle = IndexHandle()

    # 点击登录前往登录页
    def to_login_page(self):
        # 点击登录超链接
        self.index_handle.click_login_link()

    # 搜索商品
    def search_goods(self, name):
        # 输入关键字
        self.index_handle.input_search_text(name)
        # 点击搜索按钮
        self.index_handle.click_search_btn()

    # 进入购物车页面
    def to_cart_page(self):
        # 点击我的购物车
        self.index_handle.click_my_cart()

    # 进入我的订单页面
    def to_my_order_page(self):
        # 点击我的订单
        self.index_handle.click_my_order()


if __name__ == '__main__':
    driver = DriverUtil.get_driver()

    driver.get("http://localhost/")
    lp = IndexProxy()

    lp.search_goods("小米")
