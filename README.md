# Z-Blog-We

折腾 Z-Blog 的我们……


## 项目介绍

收集展示 Z-Blog、Z-BlogPHP 博客站点，如果你有自己开发主题或者插件，也可以提交到这里。


## 基本要求

最近修改日期：2023-10-18

1. 强制启用 https；
2. RSS 全文输出；
3. 符合「人写博客」的基本理念；

你可以写篇文章宣传一下本项目，当然目前这不是必须的；


## 如何提交

请按模板提交 ISSUE；

https://github.com/wdssmq/test-actions/issues


```markdown

    ```yml
    # 前后的 源码块标记也要带上
    name: 昵称标识
    id: GitHub ID
    site:
        site_name: 站点名称
        site_url: 站点地址
        site_rss: 站点 RSS 地址
        site_desc: 站点描述
    app:
        - app_name: 应用名称
          app_desc: 应用描述
          app_type: [plugin|theme] # 插件或者主题
          app_url: Git 仓库地址
        # 可以有多个 app

    ```

```
