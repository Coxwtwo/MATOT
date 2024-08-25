<!-- markdownlint-disable MD033 MD041 -->

## MATOT

基于MAA全新架构的未定助手。图像技术 + 模拟控制，解放双手！
由[MaaFramework](https://github.com/MaaXYZ/MaaFramework)强力驱动！


## 可能会有的功能

- [x] 启动游戏
  - [x] 官服
  - [x] B 服
- [x] 领取奖励
  - [x] 邮件
  - [x] 友谊徽章
  - [x] 每日每周任务
  - [x] 绮思经验
- [x] 基地
  - [x] 资源申请
  - [x] 案件解析
  - [x] 每日每周酬谢
- [ ] 辩论
  - [x] 复盘进修副本
  - [x] 复盘异常关卡刷技能材料
  - [x] 复盘异常关卡刷印象
  - [ ] 复盘异常关卡刷思绪残影（残影卡太多了没写完）
  - [x] 外勤委托：需要提前配好卡组，战力不足时会直接退出。
  - [x] 旧版刷思绪残影：只能复盘第一个关卡3次，要求刷取的残影至少有一个且可复盘次数为3。
- [x] 其他
  - [x] 专属甜心制作：目前会自动制作背包中第一件未完成物品。
  - [x] 逸梦系统收集花露
  - [x] 好感度：目前只支持触摸获取好感度，只能指定单个男主获取好感至每日上限。


## 图形化界面

本项目目前无GUI，但社区中有[overflow65537](https://github.com/overflow65537)贡献的[MAAFW-GUI](https://github.com/overflow65537/Tkinter_MAA-GUI)项目

## 如何使用

以windows用户为例：
1. 下载对应平台的压缩包并解压。
2. 修改模拟器分辨率，最低 `1280 * 720`。
3. 双击打开 `MaaPiCli.exe`
4. 首次使用需要按提示设置连接设备和游戏服务器。
5. 设置需要执行的任务然后执行。

## 开发相关

1. 完整克隆本项目及子项目。

    ```bash 
    git clone --recursive https://github.com/Coxwtwo/MATOT.git
    ```

    **请注意，一定要完整克隆子项目，不要漏了 `--recursive`，也不要下载 zip 包！**

2. 下载 MaaFramework 的 [Release 包](https://github.com/MaaXYZ/MaaFramework/releases)，解压到 `deps` 文件夹中。

3. 配置资源文件。

    ```bash
    python ./configure.py
    ```

4. 按需求修改 `assets` 中的资源文件并测试。

   请参考 [MaaFramework](https://github.com/MaaXYZ/MaaFramework/blob/main/docs/zh_cn/1.1-%E5%BF%AB%E9%80%9F%E5%BC%80%E5%A7%8B.md) 相关文档。

    **本项目完全依赖 Json 低代码编程（Pipeline Json），请注意查看[Pipeline 协议](https://github.com/MaaAssistantArknights/MaaFramework/blob/main/docs/zh_cn/3.1-%E4%BB%BB%E5%8A%A1%E6%B5%81%E6%B0%B4%E7%BA%BF%E5%8D%8F%E8%AE%AE.md)。**

    - 可使用 [MaaDebugger](https://github.com/MaaXYZ/MaaDebugger) 进行调试；
    - 也可以在本地安装后测试：

        1. 执行安装脚本

            ```bash
            python ./install.py
            ```

        2. 运行 `install/MaaPiCli.exe`

5. 完成开发工作后，上传代码。

    ```bash
    # 配置 git 信息（仅第一次需要，后续不用再配置）
    git config user.name "您的 GitHub 昵称"
    git config user.email "您的 GitHub 邮箱"
    
    # 提交修改
    git add .
    git commit -m "XX 新功能"
    git push origin HEAD -u
    ```

6. 发布版本

    ```bash
    # CI 检测到 tag 会自动进行发版
    git tag v1.0.0
    git push origin v1.0.0
    ```


## 鸣谢

本项目由 **[MaaFramework](https://github.com/MaaXYZ/MaaFramework)** 强力驱动！

感谢MaaFW开发者的贡献。

