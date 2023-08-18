""" markdown 生成函数 """
import inspect
import re

from bin.base import fnBug

md_head_tpl = """---
title: {title}
pubDate: {pubDate}
description: {description}
heroImage: {heroImage}
---\n"""

md_body_tpl = """
### {title_link}\n
{desc}\n
`{tags}` / {source_link}\n
"""


# 修复错误的 … 符号为 ……
def fix_ellipsis(text):
    """修复错误的 … 符号为 ……"""
    text = text.replace("……", "…")
    return text.replace("…", "……")


# 拼接 md 语法的链接
def md_link(title, url, text_type=""):
    """拼接 md 语法的链接"""
    if text_type == "url":
        return f'[{url}]({url} "{title}")'
    return f'[{title}]({url} "{title}")'


# ubb 语法的链接转换
def ubb_link(text):
    """ubb 语法的链接转换"""
    # [url=https://www.wdssmq.com]沉冰浮水的博客[/url]
    # 正则解析上面的语法
    regex = r"\[url=(.+?)\](.+?)\[/url\]"
    match = re.search(regex, text)
    if match:
        return md_link(match.group(2), match.group(1))


# 保存为 md 文件
def save_md(data, md_path, debug=False):
    """保存为 md 文件"""
    file_name = data["issues_title"].replace(" ", "_") + ".md"
    file_path = md_path + file_name
    # meta data
    meta_data = {
        "title": data["issues_title"],
        "pubDate": data["issues_title"],
        "description": "description",
        "heroImage": "/placeholder-hero.jpg",
    }
    # markdown content
    md_content = md_head_tpl.format(**meta_data) + "\n"

    # issues_url
    md_content += md_link(data["issues_title"], data["issues_url"]) + "\n"

    for note in data["note_data"]:
        note["Desc"] = fix_ellipsis(note["Desc"])
        md_content += md_body_tpl.format(
            desc=note["Desc"],
            tags=note["Tags"],
            title_link=md_link(note["Title"], note["Url"]),
            source_link=ubb_link(note["Source"]),
        )
        md_content += "----\n"

    # 保存到文件
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(md_content)
    fnBug(f"保存文件：{file_path}", inspect.currentframe().f_lineno, debug)
