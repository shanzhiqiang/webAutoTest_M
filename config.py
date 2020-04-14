import logging
import os

# 获取项目根目录
# 获取到当前文件(config.py)的绝对路径
# C:\Users\iambtree\Desktop\代码模板_day10\webAutoTest_M\config.py
# print(os.path.abspath(__file__))
# 只截取 目录部分  --> 项目路径
# print(os.path.dirname(os.path.abspath(__file__)))
# 项目路径保存给一个变量 -- 外面使用的使用导包使用
from logging.handlers import TimedRotatingFileHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# print(BASE_DIR)

# 初始化日志配置
def init_log_config():
    # 日志器 默认日志器 root
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 处理器  控制台 -- StreamHandler 时分文件  --TimedRatatingFileHandler
    shl = logging.StreamHandler()
    trfhl = TimedRotatingFileHandler(BASE_DIR + "/log/mylog.log", when="h", interval=1, backupCount=0, encoding="utf-8")

    # 格式化器  "%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s"
    fmter = logging.Formatter(
        fmt="%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s")

    # 处理器设置格式器
    shl.setFormatter(fmter)
    trfhl.setFormatter(fmter)

    # 日志器添加处理器
    logger.addHandler(shl)
    logger.addHandler(trfhl)
