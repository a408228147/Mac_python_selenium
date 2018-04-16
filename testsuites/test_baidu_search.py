
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage


class BaiduSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''
        测试开始前的准备工作，用于加载浏览器URL以及驱动
        :return:
        '''
        cls.browse = BrowserEngine()
        cls.driver = cls.browse.open_browser()

    @classmethod
    def tearDownClass(cls):
        '''
        测试结束后的操作，基本上都是关闭浏览器
        '''
        cls.browse.quit_browser(cls.driver)
    def test_baidu_search(self):
        '''
        unittest 测试方法必须test开头
        :return:
        '''
        homepage = HomePage(self.driver)
        homepage.type_search('selenium')  # 调用页面对象中的方法
        homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
        homepage.time_sleeps(2)
        homepage.get_windows_img()  # 调用基类截图方法
        try:
            assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
           # self.assertIn("selenium" in homepage.get_page_title())
            print('Test Pass.')
        except Exception as e:
            print('Test Fail.', format(e))

    def test_baidu_search(self):
                '''
                unittest 测试方法必须test开头
                :return:
                '''
                homepage = HomePage(self.driver)
                homepage.type_search('selenium')  # 调用页面对象中的方法
                homepage.send_submit_btn()  # 调用页面对象类中的点击搜索按钮方法
                homepage.time_sleeps(2)
                homepage.get_windows_img()  # 调用基类截图方法
                try:
                    assert 'selenium' in homepage.get_page_title()  # 调用页面对象继承基类中的获取页面标题方法
                    # self.assertIn("selenium" in homepage.get_page_title())
                    print('Test Pass.')
                except Exception as e:
                    print('Test Fail.', format(e))


if __name__ == '__main__':
        unittest.main()
