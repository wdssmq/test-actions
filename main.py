""" 主入口函数 """
import os
import sys
import json
import time
import inspect

# 从 bin/base.py 中导入通用函数
from bin.base import fnBug, fnErr, fnLog

# 全局变量
config_info = {}
debug_info = {
    "debug": False,
    "log": ""
}


def init():
    ''' 初始化 '''
    global config_info
    fnLog("## init")

    try:
        if os.environ["GIT_REPO"]:
            config_info["GIT_REPO"] = os.environ["GIT_REPO"]

    except KeyError:
        fnLog("无法获 github 的 secrets 配置信息，开始使用本地变量")
        fnLog("config 内拥有以下值: %s" % str(config_info.keys()),
              inspect.currentframe().f_lineno)

    # 读取配置文件
    if os.path.exists("dev_config.json") is True:
        with open("dev_config.json", 'rb') as config_file:
            config_info = json.loads(config_file.read())

    # 读取 debug 配置
    if "DEBUG" in config_info.keys() and config_info["DEBUG"]:
        debug_info["debug"] = True
        fnBug("debug 已开启: %s" % debug_info["debug"],
              inspect.currentframe().f_lineno, debug_info["debug"])
# 初始化函数


# 初始化调用
init()