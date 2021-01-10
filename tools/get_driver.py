import appium.webdriver
from selenium import webdriver

import page


class GetDriver:
    # 1. 声明变量
    __web_driver = None

    # 声明app中driver变量
    __app_driver = None

    # 2. 获取driver方法
    @classmethod
    def get_web_driver(cls, url):
        # 判断driver为空
        if cls.__web_driver is None:
            # 获取浏览器
            cls.__web_driver = webdriver.Chrome()
            # 最大化浏览器
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回driver
        return cls.__web_driver

    # 3. 退出driver方法
    @classmethod
    def quit_web_driver(cls):
        # 判断driver不为空
        if cls.__web_driver:
            # 退出操作
            cls.__web_driver.quit()
            # 置空操作 重点
            cls.__web_driver = None

    # 4. 获取app_driver
    @classmethod
    def get_app_driver(cls):
        # 1. 判断app_driver为空
        if cls.__app_driver is None:
            # 设置启动参数
            desired_caps = dict()
            # 必填—且正确
            desired_caps['platformName'] = 'Android'
            # 必填—且正确
            desired_caps['platformVersion'] = '5.1'
            # 必填
            desired_caps['deviceName'] = '1'
            # app报名
            desired_caps['appPackage'] = page.appPackage
            # app启动名
            desired_caps['appActivity'] = page.appActivity
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        # 返回cls.__app_driver
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        # 判断不为空
        if cls.__app_driver:
            # 退出操作
            cls.__app_driver.quit()
            # 置空操作
            cls.__app_driver = None


