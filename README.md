<div align="center">

<h1>Python 工具箱 - PyTools</h1>

![GitHub stars](https://img.shields.io/github/stars/hrpzcf/AwesomePyKit?style=flat)
![GitHub forks](https://img.shields.io/github/forks/hrpzcf/AwesomePyKit?style=flat)
![GitHub issues](https://img.shields.io/github/issues/hrpzcf/AwesomePyKit)
![GitHub license](https://img.shields.io/github/license/hrpzcf/AwesomePyKit)
![GitHub release](https://img.shields.io/github/v/release/hrpzcf/AwesomePyKit)
![PyPI Release](https://img.shields.io/pypi/v/Awespykit?label=PyPi)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Awespykit?label=Python)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/Awespykit?label=Wheel)

</div>

## 快速跳转

[程序简介](#程序简介) **·** [如何安装和运行](#如何安装和运行) **·** [程序截图](#程序截图) **·** [源码仓库](#源码仓库)

<br />

## 程序简介

这是一个关于 Python 的工具箱，有包管理器、程序打包工具、镜像源设置工具、模块安装包下载器可用。

`注：仅支持在 Windows 系统上使用`

<br />

## 如何安装和运行

> #### 安装包安装（推荐）

1. 下载安装包
3. 安装完成后，即可在开始菜单找到PyTools。

<br/>

> #### 下载源代码并从源代码运行：

1. 假设你的计算机已经安装了 Python 环境，且版本 >=3.7。
2. `git clone` 克隆源代码到你的计算机(需要计算机上已经安装了 git)或下载源代码包 Source code.zip 解压。
3. 在 Awespykit 目录内打开 PowerShell 或 Cmd。
4. 使用以下命令安装 Awespykit 的依赖，有多个 Python 环境的请自行选择环境：
   ```cmd
   pip install -r requirements.txt
   ```
5. 找到 runpykit.py 运行。如果不想显示控制台，可以将 runpykit.py 重命名为 runpykit.pyw。
6. *注意*：由于更改了项目目录结构，使用 Pycharm 的同学，Pycharm 打开 Awespykit 目录后，请右键 Awespykit
   -> src -> awespykit 目录，选择菜单末尾的 `将目录标记为->源代码根目录` 把 `awespykit`
   目录标记为源码根目录，否则影响编程体验。

<br />

> #### 使用 pip 命令从 GitHub 安装开发版

1. 假设你的计算机已经安装了 Python 环境，且版本 >=3.7（如果不符合要求则不能使用这个方法）。
2. 使用以下命令安装开发版（可能需要你的计算机上已经安装了 git）：
   ```cmd
   pip install git+https://github.com/HelloEasytong/PyTools.git@main
   ```
注意：开发版可能含有许多 BUG，无法保证程序一定能正常运行，也无法保证所有功能都正常。

<br />

## 程序截图

> ### 工具箱启动窗口

![启动窗口](img/MainEntrance.png)

<br/>

> ### 包管理器：封装了 pip 命令

- 提供多 Python 环境的包管理，免于用命令行管理的混乱
    + 支持常规 Python 环境
    + 支持 venv 虚拟环境
    + 支持 Anaconda 主环境、虚拟环境
- 支持批量安装模块、按版本号安装等
- 支持检查更新、批量卸载、批量升级(不了解各包的互相依赖则请慎用批量功能)

![包管理器](img/PackageManager.png)

<br/>

> ### 程序打包工具：封装了 Pyinstaller

- 封装了 Pyinstaller 的大部分常用命令
- 支持选择不同的环境进行打包操作
- 支持一键在项目下创建 venv 虚拟环境
- 支持项目所使用的 Python 环境的检查，检查出未安装的模块可一键安装

![程序打包工具](img/PyinstallerTool.png)

<br/>

> ### 镜像源设置工具：封装了 pip 命令

- 使用 pip 时网络不佳，用此工具一键切换 pip 所使用的镜像源
- 支持保存你自己常用的镜像源地址

![镜像源设置工具](img/IndexUrlTool.png)

<br/>

> ### 模块安装包下载器：封装了 pip 命令

- 用于特殊需求时下载各个包/库/模块的安装包
- 支持同时下载要下载的包/库/模块的依赖
- 支持从 requirement.txt 批量读取并一键下载

![模块安装包下载器](img/PackageDownloader.png)

<br/>


