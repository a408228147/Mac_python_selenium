import unittest
from tools import HTMLTestRunner
import os
import time

'''
#实例化一个TestSuite对象
#suite=unittest.TestSuite()
#将test_forget_password模块下的forgetPassword类的测试用例test_forget_password加入到测试套件里
#suite.addTest(test_forget_password.forgetPassword("test_forget_password"))

'''
# 设置报告文件保存路径
report_path = '../test_reports/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
suit = unittest.defaultTestLoader.discover("testsuites", "test_*.py", )
# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    with open(HtmlFile, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(f)
        runner.run(suit)
    # 开始执行测试套件