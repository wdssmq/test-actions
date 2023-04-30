# 测试各种东西的仓库

## act-note 分支

本地测试 GitHub Actions，使用的环境为 wsl2；

需要先安装好 Docker，然后安装 act；

### 克隆本仓库或者使用你自己的仓库

```bash
git clone git@github.com:wdssmq/test-actions.git
cd test-actions
git switch act-note
```

`.github/workflows/update-now.yml`为本仓库的 GitHub Actions 配置文件，可以参考。

### 安装 act

```bash
# 安装 act
# 方式一：脚本安装
curl -s https://raw.githubusercontent.com/nektos/act/master/install.sh | sudo bash

# 方式二：下载二进制文件
cd ~/tmp
wget https://github.com/nektos/act/releases/download/v0.2.44/act_Linux_x86_64.tar.gz
# wget https://ghproxy.com/https://github.com/nektos/act/releases/download/v0.2.44/act_Linux_x86_64.tar.gz

# 解压
tar -xzvf act_Linux_x86_64.tar.gz

# 移动到 /usr/local/bin
sudo mv act /usr/local/bin

```

### 使用 act

```bash
# 查看 Actions 列表
act -l

# Stage  Job ID  Job name  Workflow name      Workflow file   Events
# 0      update  update    Update update.txt  update-now.yml  push

# 执行 update 任务
act -j update

# 首次执行需要选择并拉取 Docker 镜像，三个选项大小不一样，文件越大支持的动作越多

```