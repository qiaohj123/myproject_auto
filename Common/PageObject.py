# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import time
import datetime
from rbemp_po.Common.logger import Log
from rbemp_po.Common.rconf import screen_shot
from selenium import webdriver
import os
import random


locator_map = {'css': 'By.CSS_SELECTOR',
                'id': 'By.ID',
                'name': 'By.NAME',
                'xpath': 'By.XPATH',
                'link_text': 'By.LINK_TEXT',
                'partial_link_text': 'By.PARTIAL_LINK_TEXT',
                'tag_name': 'By.TAG_NAME',
                'class_name': 'By.CLASS_NAME',
                }

class PageObject(object):
    # 初始化
    def __init__(self,driver,page_url=None):
        self.log = Log()
        self.dr = driver
        self.dr.maximize_window()
        self.url = page_url
        if self.url != None:
            self.dr.get(self.url)
    def Find_element(self,way,elements,wait_times=30,):
        if way == "name":
            locator = (By.NAME,elements)
        if way == "id":
            locator = (By.ID, elements)
        if way == "xpth":
            locator = (By.XPATH, elements)
        if way == "css":
            locator = (By.CSS_SELECTOR, elements)
        t1 = time.time()
        try:
            WebDriverWait(self.dr,wait_times,1).until(EC.visibility_of_element_located(locator))
            # 元素等待结束时间
            # t2 = time.time()
            # self.log.info("元素等待结束。等待开始时间为：{0}，等待结束时间为：{1}，等到耗费时长为：{2}".format(int(round(1000*t1)),int(round(1000*t2)),int(round(1000*(t2-t1)))))
            if way == "name":
                return self.dr.find_element_by_name(elements)
            elif way == "id":
                return self.dr.find_element_by_id(elements)
            elif way == "xpth":
                return self.dr.find_element_by_xpath(elements)
            elif way == "css":
                return self.dr.find_element_by_css_selector(elements)
        except TimeoutException as e:
            self.log.warning(">>> 等待元素超时，无法获取到元素，截图当前页面")
            screen_shot(self.dr, "无法获取元素.png")
            raise e

    # 元素存在性判断
    def Wait_Elepresence(self,way,elements,wait_times=30):
        # 元素等待开始时间
        # t1 =time.time()
        if way == "name":
            locator = (By.NAME,elements)
        if way == "id":
            locator = (By.ID, elements)
        if way == "xpth":
            locator = (By.XPATH, elements)
        if way == "css":
            locator = (By.CSS_SELECTOR, elements)
        try:
            ele = WebDriverWait(self.dr,wait_times,0.5).until(EC.presence_of_element_located(locator))
            return ele
            # 元素等待结束时间
            # t2 = time.time()
            # self.log.info("元素等待结束。等待开始时间为：{0}，等待结束时间为：{1}，等到耗费时长为：{2}".format(t1,t2,t2-t1))
        except TimeoutException as e:
            self.log.warning(">>> 等待元素超时，当前页面不存在此元素")
            return None

 # 元素可见性判断
    def Wait_Elevisibel(self,way,elements,wait_times=30):
        # 元素等待开始时间
        # t1 =time.time()
        if way == "name":
            locator = (By.NAME,elements)
        if way == "id":
            locator = (By.ID, elements)
        if way == "xpth":
            locator = (By.XPATH, elements)
        if way == "css":
            locator = (By.CSS_SELECTOR, elements)
        try:
            ele = WebDriverWait(self.dr,wait_times,1).until(EC.visibility_of_element_located(locator))
            return ele
            # 元素等待结束时间
            # t2 = time.time()
            # self.log.info("元素等待结束。等待开始时间为：{0}，等待结束时间为：{1}，等到耗费时长为：{2}".format(t1,t2,t2-t1))
        except TimeoutException as e:
            self.log.warning(">>> 等待元素超时，当前页面不存在此元素")
            return None



class Elements_located(object):
    # 初始化
    def __init__(self,driver):
        self.dr = driver

    # 元素定位查找
    def by_element(self,**kwargs):
        K, V = next(iter(kwargs.items()))
        by, locator = (locator_map[K], V)
        return self.dr.find_element(by,locator)
    # # 元素定位点击事件
    # def by_element_c(self):
    #     return self.dr.find_element(self.locator).click()
    # # 元素定位输入事件
    # def by_element_s(self,content):
    #     return self.dr.find_element(self.locator).send_keys(content)
    # # 元素定位文本事件
    # def by_elementt(self):
    #     return self.dr.find_element(self.locator).text()







    #
    # # id定位查找
    # def by_id(self,locator):
    #     return self.dr.find_element(By.ID,locator)
    # # id定位点击事件
    # def by_id_c(self,locator):
    #     return self.dr.find_element(By.ID,locator).click()
    # # id定位输入事件
    # def by_id_s(self,locator,content):
    #     return self.dr.find_element(By.ID,locator).send_keys(content)
    #
    # # name定位查找
    # def by_name(self,locator):
    #     return self.dr.find_element(By.NAME,locator)
    # # name定位点击事件
    # def by_name_c(self,locator):
    #     return self.dr.find_element(By.NAME,locator).click()
    # # name定位输入事件
    # def by_name_s(self,locator,content):
    #     return self.dr.find_element(By.NAME,locator).send_leys(content)
    #
    # # css定位查找
    # def by_css(self,locator):
    #     return self.dr.find_element(By.CSS_SELECTOR,locator)
    # # css定位点击事件
    # def by_css_c(self,locator):
    #     return self.dr.find_element(By.CSS_SELECTOR,locator).click()
    # # css定位输入事件
    # def by_css_s(self,locator,content):
    #     return self.dr.find_element(By.CSS_SELECTOR,locator).send_keys(content)
    #
    # # tag_name 定位查找
    # def by_tagname(self,locator):
    #     return self.dr.find_element(By.TAG_NAME,locator)
    # # tag_name定位点击事件
    # def by_tagname_c(self,locator):
    #     return self.dr.find_element(By.TAG_NAME,locator).click()