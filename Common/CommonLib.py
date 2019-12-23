# -*- coding:utf-8 -*-

import time
import random
import configparser
import os
import datetime
from itertools import islice
from rbemp_po.Common.logger import Log
from rbemp_po.Common.PageObject import PageObject
from selenium.webdriver.common.by import By


    # 读取文件路径、环境信息等配置
def rconf(value):
    cf = configparser.ConfigParser()
    os.chdir('D:\PycharmProjects\\untitled\\rbuildemp\config')
    cf.read('config.ini', encoding='utf-8')
    items = cf.options('logindata')
    for i in items:
        if i == value:
            result = cf.get('logindata', i)
            return result


    # 登录系统
def login(dr):
    log = Log()
    PO = PageObject(dr,page_url='http://192.169.7.209:8000')
    name = PO.Find_element('name','username')
    name.send_keys('admin')
    pwd = PO.Find_element('name','password')
    pwd.send_keys('123qwe')
    button = PO.Find_element('xpth','//span[text()="登录"]')
    button.click()
    log.info('>>> 系统登录成功')

    # 上传各种类型的文件
def upload_file(dr,file_path):
    po = PageObject(dr)
    file_format = ['txt','zip','xls','xlsx','csv','et']
    for i in range(1,6):
        po.Find_element('css', '.el-icon-ali-upload')
        file_ele = dr.find_element(By.CSS_SELECTOR,".el-upload__input")
        file_ele.send_keys('%s.%s'%(file_path,file_format[i]))



    # 页面截图
def screen_shot(dr, filename):
    rpath = rconf('path_shot')
    os.chdir(rpath)
    isexist = os.path.exists(time.strftime('%Y%m%d'))

    if not isexist:
        os.makedirs(time.strftime('%Y%m%d'))
        full_path = os.path.join(rpath, time.strftime('%Y%m%d'))
        os.chdir(full_path)
        dr.get_screenshot_as_file(time.strftime('%H%M%S') + filename)
    else:
        full_path = os.path.join(rpath, time.strftime('%Y%m%d'))
        os.chdir(full_path)
        dr.get_screenshot_as_file(time.strftime('%H%M%S') + filename)

    # table表格数据——获取单元格数据
def getdata(dr, row_s, clu_s):
    try:
        table = dr.find_element(By.CSS_SELECTOR,'.el-table__body')
        # 获取列表表格的行数
        table_rows = table.find_elements_by_tag_name('tr')
        # 获取列表单元格数据
        data = table_rows[row_s].find_elements_by_tag_name('td')[clu_s].text
        return data
    except Exception as e:
        Log().warning("获取单元格数据失败%s"%(e))
        raise e
    # 获取表格行数
def getrows(dr):
    try:
        table = dr.find_element(By.CSS_SELECTOR,'.el-table__body')
        # 获取列表表格的行数
        table_rows = table.find_elements_by_tag_name('tr')
        return len(table_rows)
    except Exception as e:
        Log().warning("获取表格行数失败%s" % (e))


     # table表格数据——获取单元格元素定位信息
def getelement(dr, row_s, clu_s):
    try:
        table = dr.find_element(By.CSS_SELECTOR,'.el-table__body')
        # 获取列表表格的行数
        table_rows = table.find_elements_by_tag_name('tr')
        # 获取列表单元格元素信息
        element = table_rows[row_s].find_elements_by_tag_name('td')[clu_s]
        return element
    except Exception as e:
        Log().warning("获取表格单元格元素信息失败%s"%(e))
        raise e

    # 查询结构条件判断是否正确
def tablecheck(dr, clus, text, exname):
    table = dr.find_element(By.CSS_SELECTOR,'.el-table__body')
    # 获取列表表格的行数
    table_rows = table.find_elements_by_tag_name('tr')
    # 验证查询结果数据与条件查询数据是否一致
    try:
        for i in range(len(table_rows)):
            if i <= len(table_rows) - 1:
                txt = table_rows[i].find_elements_by_tag_name('td')[clus].text
                if txt == text:
                    pass
                elif txt == '':
                    Log().warning("查询结果数据为空，条件数据为{0}".format(text))
                else:
                    Log().warning("查询结果与条件数据存在不一致，条件数据为{0}，查询结果数据为{1}".format(text, txt))
            else:
                pass
    except Exception as e:
        Log().warning("查询结果验证失败%s"%(e))
        raise e

    # 生成手机号码
def create_phone():
    # 第二位数字
    second = [3, 5, 7, 8][random.randint(0, 3)]
    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    # 最后八位数字
    suffix = random.randint(9999999,100000000)
    # 拼接手机号
    phonenum = "1{}{}{}".format(second, third, suffix)
    return phonenum

#  定时发送时间控件时间选择
def timecontrl(dr):
    po = PageObject(dr)
    po.Find_element('xpth', '//span[text()="定时发送"]').click()
    po.Find_element('css', '.el-date-editor').click()
    po.Find_element('xpth', '//div[@x-placement="top-start"]/div[2]/button[1]').click()
    po.Find_element('css', '.el-date-editor').click()
    po.Find_element('xpth', '//div[@x-placement="top-start"]/div/div/div/span[2]/div/input').clear()
    now = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(hours=1), '%H:%M:%S')
    Log().info('>>> 定时发送时间为：%s'%(now))
    po.Find_element('xpth', '//div[@x-placement="top-start"]/div/div/div/span[2]/div/input').send_keys(now)
    po.Find_element('xpth', '//div[@x-placement="top-start"]/div[2]/button[2]').click()

# 获取表格数据总数
def toal_datas(dr):
    po = PageObject(dr)
    txt = po.Wait_Elevisibel('css', '.el-pagination__total').text
    total_nums = int(txt.split()[1])
    return total_nums


# 清空文件
def move_content(filename):
    with open('D:\PycharmProjects\\untitled\\rbemp_po\Common\%s'%(filename),'r+') as f:
        f.truncate()

# 写入文件
def write_get(filename,content):
    with open('D:\PycharmProjects\\untitled\\rbemp_po\Common\%s'%(filename),'a+') as f:
        f.writelines(content)

# 读取文件
def read_content(filename, i=0):
    with open('D:\PycharmProjects\\untitled\\rbemp_po\Common\%s'%(filename),'r+') as f:
        a = f.readlines()
        return a[i]

