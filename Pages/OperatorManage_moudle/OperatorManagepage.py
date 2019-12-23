# -*- coding:utf-8 -*
from rbemp_po.Common.PageObject import PageObject
from rbemp_po.Common.CommonLib import *
from selenium.webdriver.common.keys import Keys

class OperatorManagepage(PageObject):

    # 新建操作员测试数据信息
    num = str(random.randint(1000,9999))
    # 登录账号
    login_account = 'cs'+num
    # 操作员名称
    operator_name = '自动化测试操作名称'+num
    # 手机号码
    phone_num = create_phone()


    # 新建操作员页面元素
    def page_ele_newcarate(self):
        # 员工基本信息
        # 登录账号
        login_account0 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[2]/div/div/input')
        # 操作员名称
        operator_name1 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[3]/div/div/input')
        # 操作员编码
        operator_code2 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[4]/div/div/input')
        # 所属机构
        organization3 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[5]/div/div/div/input')
        # 性别
        sex4 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[6]/div/div/div/input')
        # 生日
        birthday5 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[7]/div/div/input')
        # 手机
        phonenum6 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[8]/div/div/input')
        # 职位
        position7 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[9]/div/div/div/input')
        # 分配角色
        role8 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[10]/div/div/div[2]/input')
        # 账号状态
        account_status9 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[11]/div/div/div[1]/input')
        # 设置审核流程
        check_stream10 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[12]/div/div/div[1]/input')
        # 固定尾号
        end_num11 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[13]/div/label/span/span')
        # 接收审批提醒--短信
        sms12 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[14]/div/label[1]/span[1]/span')
        # 接收审核提醒--邮箱
        email13 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[14]/div/label[2]/span[1]/span')
        # 是否为客服人员
        customer14 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[15]/div/label/span/span')
        # 确定按钮
        commit15 = self.Find_element('xpth', '//div[@class="operator-box"]/form/div[31]/div/div/button')

        return login_account0,operator_name1,operator_code2,organization3,sex4,birthday5,phonenum6,position7,role8,account_status9,check_stream10,end_num11,sms12,email13,customer14,commit15

    # 进入到操作员管理页面
    def forward_page_operator(self):
        # 系统管理
        entsms = self.Find_element('xpth', '//span[text()="系统管理"]')
        entsms.click()
        samesend = self.Find_element('xpth', '//span[text()="操作员管理"]')
        samesend.click()
        # 操作员管理页面
        self.Find_element('xpth', '//*[@id="app"]/div/div[2]/div[1]/div/ul/div[13]/li/ul/div[3]/li/ul/div[2]/a/li/span').click()


    # 新建按钮封装
    def new_create(self):
        self.Find_element('xpth', '//div[@class="conten-top"]/button[1]').click()

    # 机构选择
    def organization(self):
        self.page_ele_newcarate()[3].click()
        self.Find_element('xpth', '//span[text()="梦网科技"]').click()

    # 性别选择
    def sex(self):
        self.page_ele_newcarate()[4].click()
        self.Find_element('xpth', '//span[text()="男"]').click()
    # 生日选择
    def birthday(self):
        self.page_ele_newcarate()[5].click()
        self.Find_element('xpth', '//div[@class="el-date-picker__header"]/button[1]').click()
    # 分配角色
    def roles(self):
        self.page_ele_newcarate()[8].click()
        self.Find_element('xpth', '//div[@x-placement="bottom-start"]/div[1]/div[1]/ul/li[5]/span').click()


    # 新增及断言
    def commit(self):
        self.page_ele_newcarate()[15].click()
        create_result = self.Wait_Elepresence('css', '.el-message__content').text
        if create_result == '新增成功':
            self.log.info('>>> 新建操作员成功')
        else:
            self.log.info('>>> 新建操作员失败')

