import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle


# 对象库层
class OrderSubmitPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        super().__init__()

        # 业务元素定位信息
        # 超链接--提交订单
        self.submit_order = (By.LINK_TEXT, '提交订单')

        # 文本内容 -- 提交结果
        self.submit_result = (By.CSS_SELECTOR, '.erhuh>h3')

    # 定位提交订单超链接
    def find_submit_order(self):
        return self.base_find_element(self.submit_order)

    # 定位提交结果文本内容
    def find_submit_result(self):
        return self.base_find_element(self.submit_result)


# 操作层
class OrderSubmitHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.order_page = OrderSubmitPage()

    # 点击提交订单超链接
    def click_submit_order(self):
        self.order_page.find_submit_order().click()

    # 获取提交结果文本
    def get_submit_result_text(self):
        return self.order_page.find_submit_result().text


# 业务层
class OrderSubmitProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.order_handle = OrderSubmitHandle()

    # 提交订单
    def submit_order(self):
        # 点击提交订单超
        self.order_handle.click_submit_order()

    # 提交结果
    def get_submit_result(self):
        return self.order_handle.get_submit_result_text()
