from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()


class AppBase(Base):
    # 1. 查找页面是否存在指定元素
    def app_base_is_exist(self, loc):
        try:
            # 1. 调用查找方法
            self.base_find(loc)
            log.info("在app页面中找到指定元素了")
            # 2. 输出信息
            print("找到元素：{}".format(loc))
            # 3. 返回True
            return True
        except:
            # 1. 输出信息
            log.error("没有在app中找到指定元素")
            print("未找到元素：{}".format(loc))
            # 2. 返回False
            return False

    # 2. 从右向左滑动屏幕
    def app_base_right_wipe_left(self, loc_area, click_text):
        log.info("正在调用从右向左滑动方法")
        # 1. 查找区域元素
        el = self.base_find(loc_area)
        # 2. 获取区域元素的位置y坐标
        y = el.location.get("y")
        # 3. 获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 4. 计算 start_x, start_y, end_x, end_y
        start_x = width*0.8
        start_y = y + height*0.5
        end_x = width*0.2
        end_y = y + height*0.5
        # 组合频道元素配置信息
        loc = By.XPATH, "//*[@bounds='[0,520][1440,2288]']/*[contains(@text,'{}')]".format(click_text)
        # 5. 循环操作
        while True:
            # 1. 获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2. 捕获异常
            try:
                # 1. 查找元素
                el = self.base_find(loc, timeout=3)
                # 2. 输出提示信息
                print("找到：{}元素".format(loc))
                # 3. 点击元素
                el.click()
                # 4. 跳出循环
                break
            # 3. 处理异常
            except:
                # 1. 输出提示信息
                print("未找到元素{}".format(loc))
                # 2. 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            # 4. 判断是否为最后一页
            if page_source == self.driver.page_source:
                # 1. 输出提示信息
                print("滑到最后一屏，未找到元素")
                # 2. 抛出未找到元素异常
                raise NoSuchElementException

    # 3. 从下向左上滑动屏幕
    def app_base_down_wipe_up(self, loc_area, click_text):
        log.info("正在调用从下向上滑动方法")
        # 1. 查找区域元素
        el = self.base_find(loc_area)
        # 2. 获取区域元素宽高
        width = el.size.get("width")
        height = el.size.get("height")
        # 3. 计算 start_x, start_y, end_x, end_y
        start_x = width*0.5
        start_y = height*0.8
        end_x = width*0.5
        end_y = height*0.2
        # 组合频道元素配置信息
        loc = By.XPATH, "//android.widget.HorizontalScrollView/*[contains(@text,'{}')]".format(click_text)
        # 5. 循环操作
        while True:
            # 1. 获取当前屏幕页面结构
            page_source = self.driver.page_source
            # 2. 捕获异常
            try:
                # 1. 查找元素
                sleep(2)
                el = self.base_find(loc, timeout=3)
                # 2. 输出提示信息
                print("找到：{}元素".format(loc))
                sleep(2)
                # 3. 点击元素
                el.click()
                # 4. 跳出循环
                break
            # 3. 处理异常
            except:
                # 1. 输出提示信息
                print("未找到元素{}".format(loc))
                # 2. 滑动屏幕
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            # 4. 判断是否为最后一页
            if page_source == self.driver.page_source:
                # 1. 输出提示信息
                print("滑到最后一屏，未找到元素")
                # 2. 抛出未找到元素异常
                raise NoSuchElementException
