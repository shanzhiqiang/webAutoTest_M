from selenium.webdriver.common.by import By

from base.base_page import BasePage, BaseHandle

# 对象库层
from utils import DriverUtil


class GoodsSearchPage(BasePage):
    # init方法
    def __init__(self):
        # 调用父类init方法,实例化浏览器驱动对象
        super().__init__()
        # 页面元素定位信息  //div[@class="shop_name2"]/a[contains(text(),"小米")]
        self.goods_item = (By.XPATH, '//div[@class="shop_name2"]/a[contains(text(),"{}")]')

    # 定位商品名超链接 -- 参数--商品名关键字
    def find_goods_item(self, keys):
        loc = (self.goods_item[0], self.goods_item[1].format(keys))
        return self.base_find_element(loc)


# 操作层
class GoodsSearchHandle(BaseHandle):
    # init方法
    def __init__(self):
        # 获取对象库层对象
        self.goods_search_page = GoodsSearchPage()

    # 点击商品名超链接--参数-商品名关键字
    def click_goods_name(self, keys):
        self.goods_search_page.find_goods_item(keys).click()


# 业务层
class GoodsSearchProxy:

    # init方法
    def __init__(self):
        # 获取操作层对象
        self.goods_search_handle = GoodsSearchHandle()

    # 进入指定商品详情页--参数-商品名关键字
    def to_goods_detail_page(self, keys):
        # 点击指定商品
        self.goods_search_handle.click_goods_name(keys)


if __name__ == '__main__':
    driver = DriverUtil.get_driver()

    driver.get("http://localhost/Home/Goods/search.html?q=%E5%B0%8F%E7%B1%B3")
    gsp = GoodsSearchProxy()

    gsp.to_goods_detail_page("小米")
