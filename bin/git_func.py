""" GitHub 数据处理 """
import inspect

from bin.base import fnBug
from bin.http_func import http_git_issues

# 全局变量
config_info = {}
debug_info = {"debug": False, "log": ""}

# pylint: disable=global-statement


def git_func_init(config, debug):
    """初始化"""
    global config_info, debug_info
    config_info = config
    debug_info = debug


# 选出需要的字段
def filter_issues(pick_keys=None):
    """选出需要的字段"""
    issues = http_git_issues(
        config_info["PICK_LABEL"], config_info["GIT_REPO"], config_info["GITHUB_TOKEN"]
    )
    if pick_keys is None:
        return issues
    # 对于每个 issue，只保留需要的字段
    list_result = []
    for issue in issues:
        dict_issue = {}
        for key in pick_keys:
            dict_issue[key] = issue[key]
        list_result.append(dict_issue)
    fnBug(list_result, inspect.currentframe().f_lineno, debug_info["debug"])
    return list_result

def git_func_main():
    """主入口函数"""
    filter_issues(pick_keys=["url", "title", "body", "labels"])
