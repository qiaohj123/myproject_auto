# -*- coding:utf-8 -*-
import unittest
import os
import HTMLTestRunner

# 指定测试用例路径
case_path = os.path.join(os.getcwd(), 'D:\PycharmProjects\\untitled\\rbemp_po\Testcase')
# 指定测试报告生成后的路径
report_path = os.path.join(os.getcwd(), 'D:\PycharmProjects\\untitled\\rbemp_po\Report\\result.html')

# 加载测试用例到套件中
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern='_0SameS*TestCase.py',
                                                   top_level_dir=None)
    return discover

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    with open(report_path, 'wb') as fp:
        runner_rp = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                                  title=u'测试结果报告',
                                                  description=u'测试用例执行情况')
        runner_rp.run(all_case())

