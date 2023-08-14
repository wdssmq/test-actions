""" HTTP 请求 """
import sys
import inspect
import requests

from bin.base import fnErr


def http(req_arg=None, data_arg=None, headers_arg=None):
    """HTTP 请求"""
    if data_arg is None:
        data_arg = {}
    if headers_arg is None:
        headers_arg = {}
    # ----------------------------------------
    url = req_arg["url"]

    try:
        if req_arg["method"] == "get":
            res_info = requests.get(
                url, params=data_arg, headers=headers_arg, timeout=10
            )
        else:
            res_info = requests.post(
                url, data=data_arg, headers=headers_arg, timeout=10
            )
    except KeyError:
        fnErr("网络错误", inspect.currentframe().f_lineno)
        sys.exit(0)

    return res_info


def http_git_headers(token=""):
    """GitHub 请求头"""
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token " + token,
    }
    return headers


def http_git_issues(labels="pick", repo="", token=""):
    """获取 issues 列表"""
    url = f"https://api.github.com/repos/{repo}/issues?labels={labels}"
    headers = http_git_headers(token)
    res_data = http({"url": url, "method": "get"}, headers_arg=headers)
    # fnLog(res_data.json(), inspect.currentframe().f_lineno)
    return res_data.json()
