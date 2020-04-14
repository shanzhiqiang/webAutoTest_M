from utils import DriverUtil


# 对象库层基类
class BasePage:
    # 在初始化方法中获取到浏览器驱动对象保存到driver
    def __init__(self):
        self.driver = DriverUtil.get_driver()

    # 封装元素定位方法,参数-(定位方法,定位依据)
    # 需要浏览器驱动对象 -- 元素定位信息
    def base_find_element(self, locaction):
        # find_element定位元素-- 传入两个参数-定位方法-定位依据
        return self.driver.find_element(locaction[0], locaction[1])


# 操作层基类
class BaseHandle:
    # 封装元素输入文本操作 参数-输入元素和输入文本
    # 元素  输入  文本
    def base_input_text(self, element, text):
        element.clear()
        element.send_keys(text)
