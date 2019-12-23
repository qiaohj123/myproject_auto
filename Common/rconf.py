# -*- coding:utf-8 -*-
import time
import configparser
import os
from selenium import webdriver
from rbuildemp.public.common import elelocate
from selenium.webdriver.common.action_chains import ActionChains
from rbuildemp.public.common.logger import Log
from selenium import webdriver
import unittest
from rbuildemp.public.common import elelocate
from selenium.webdriver.common.action_chains import ActionChains
from rbuildemp.public.common.logger import Log


datapath = 'D:\PycharmProjects\\untitled\\rbulidemp\data'
id = elelocate.Id()
xp = elelocate.Xp()
css = elelocate.Css()
name = elelocate.Name()


# dr = webdriver.Chrome()
# 读取配置文件config.ini中item对应的value


def rconf(value):           # 读取配置文件
    cf = configparser.ConfigParser()
    os.chdir('D:\PycharmProjects\\untitled\\rbuildemp\config')
    cf.read('config.ini', encoding='utf-8')
    items = cf.options('logindata')
    for i in items:
        if i == value:
            result = cf.get('logindata', i)
            return result


def login(dr):                           # 登录系统
    log = Log()
    id = elelocate.Id()
    xp = elelocate.Xp()
    css = elelocate.Css()
    name = elelocate.Name()
    lg_url = rconf('login_url')
    lg_code = rconf('login_code')
    lg_usr = rconf('login_user')
    lg_pass = rconf('login_pass')
    dr.get(lg_url)
    time.sleep(3)
    name.by_name_s(dr, 'enpcode', lg_code)
    name.by_name_s(dr, 'username', lg_usr)
    name.by_name_s(dr, 'password', lg_pass)
    xp.by_xpath_c(dr,'//span[text()="登录"]')
    time.sleep(2)


def screen_shot(dr, filename):        # 测试截图
    rpath = rconf('path_shot')
    dtime = time.strftime('%Y%m%d')
    stime = time.strftime('%H%M%S')
    os.chdir(rpath)
    isexist = os.path.exists(dtime)
    if not isexist:
        os.makedirs(dtime)
        full_path = os.path.join(rpath, dtime)
        os.chdir(full_path)
        dr.get_screenshot_as_file(stime + filename)
    else:
        full_path = os.path.join(rpath, dtime)
        os.chdir(full_path)
        dr.get_screenshot_as_file(stime + filename)

def info_assert(dr,localname,infoname):    # 页面判断
    title = id.by_id_t(dr, 'top_main')
    log = Log()
    if title == localname:
        log.info('>>> 跳转进入到:%s 页面：成功' %(infoname))
    else:
        log.info('>>> 跳转进入到:%s 页面：失败' %(infoname))