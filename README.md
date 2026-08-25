# 英汉词典
包含高中3500词、英语四级词汇的词典，支持多种查找模式，也可以用 Termux 或安装其他 Python 环境在手机上运行。

## 程序说明
主程序：`dictionary.py`，依赖词典文件：`dictionary.json`，二者均放在主文件夹 `dictionary` 中。

## 功能介绍
### 查询模式
- `-e`：英文精确查询中文（默认模式）
- `-i`：英文模糊匹配，检索包含关键词的单词，忽略大小写
- `-c`：中文反向查询英文

### 指令输入格式
支持两种输入格式：
- 单词 空格-参数，示例：`love -e`
- 单词,参数，示例：`love,-i`

> 不添加参数时，默认使用 `-e` 模式。输入 `quit` 退出程序。

## 运行环境
- 电脑：本地 Python 环境直接运行
- 手机：Termux，配置 Python 环境即可运行

  > [Termux 官网](https://termux.dev)

  Termux 配置命令（将文件夹 `dictionary` 放在手机的 `Download` 目录下）：
  ```bash
  pkg update -y && pkg upgrade -y
  pkg install -y termux-tools
  # 可交互式切换国内镜像源
  termux-change-repo
  pkg update -y
  pkg install python -y
  termux-setup-storage
  echo 'alias dic="cd ~/storage/downloads/dictionary && python dictionary.py"' >> ~/.bashrc && source ~/.bashrc
  ```

    > 逐行复制执行，配置完成后输入 `dic` 即可启动字典程序
