import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle

# 对象库层
from utils import DriverUtil


class GoodsDetailPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        super().__init__()
        # 业务元素定位信息
        self.join_cart = (By.ID, "join_cart")
        self.join_result = (By.CSS_SELECTOR, ".conect-title>span")

    # 定位加入购物车超链接
    def find_join_cart(self):
        return self.base_find_element(self.join_cart)

    # 定位加入结果提示信息
    def find_join_result(self):
        return self.base_find_element(self.join_result)


# 操作层
class GoodsDetailHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.good_detail_page = GoodsDetailPage()

    # 点击加入购物车超链接
    def click_join_cart(self):
        self.good_detail_page.find_join_cart().click()

    # 获取加入结果提示信息文本--返回文本信息
    def get_join_result(self):
        return self.good_detail_page.find_join_result().text


# 业务层
class GoodsDetailProxy:
    # init方法
    def __init__(self):
        # 获取操作层对象
        self.goods_detail_handle = GoodsDetailHandle()

    # 添加商品到购物车
    def join_goods_to_cart(self):
        self.goods_detail_handle.click_join_cart()

    # 获取返回提示信息
    def get_join_result(self):
        return self.goods_detail_handle.get_join_result()


if __name__ == '__main__':
    driver = DriverUtil.get_driver()

    driver.get("http://localhost/Home/Goods/goodsInfo/id/104.html")
    gdp = GoodsDetailProxy()

    gdp.join_goods_to_cart()
    time.sleep(5)
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    print(gdp.get_join_result())
