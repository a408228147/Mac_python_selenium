import time

from selenium.common.exceptions import NoSuchAttributeException, NoSuchElementException
import  os.path
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from framework.logger import Logger
logger = Logger(logger="BasePage").getlog()

class BasePage(object):
    '''
    定义一个页面基类，让所有页面都继承与此页面，对selenium进行二次封装
    '''

    def __init__(self, dirver):
        self.driver = dirver
    #关闭当前页面
    def close_current_window(self):
        self.driver.close()
        logger.info("close_current_window")
    #前进
    def browser_forward(self):
        self.driver.forward()
        logger.info("Click forward on current page.")
    #后退
    def browser_back(self):
        self.driver.back()
        logger.info("Click back on current page.")
    #隐式等待
    def implicitly_Wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("wait for %d seconds."%seconds)
    #关闭浏览器
    def quit_browser(self):
        try:
            self.driver.quit()
            logger.info(" quit current window")
        except NameError as e:
            logger.info("Fail to close with %s"%e)
    #截图
    def get_window_img(self):
        file_path=os.path.dirname(os.path.abspath('.'))+'/screenshots/'
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name = file_path+rq+'.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had  take screenshot and save to folder :/screenshots")
        except NameError as e:
            logger.info("Failed to take screenshot! %s" % e)
            self.get_window_img()
    #寻找元素
    def find_element(self,selector):
        '''
        格式：id=>su
        :param selector:对象
        :return: element
        '''
        element=""
        if "=>" not in selector:
            return self.driver.find_element_by_id(selector)

        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by =="id" or selector_by=="i":
            try:
                element = self.driver.find_element_by_id(selector_value)
                logger.info("Had find the element  %s  successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("not find by id to element")
                logger.error("NoSuchElementException: %s" %e)
                self.get_windows_img()  # 失败了就截图

        elif selector_by == "n" or selector_by == 'name':
            try:
                element = self.driver.find_element_by_name(selector_value)
                logger.info("Had find the element %s  successful "
                        "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("not find by name to element")
                logger.error("NoSuchElementException: %s" %e)
                self.get_windows_img()  # 失败了就截图

        elif selector_by == "c" or selector_by == 'class_name':
            try:
                element = self.driver.find_element_by_class_name(selector_value)
                logger.info("Had find the element %s  successful "
                        "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("not find by class_name to element")
                logger.error("NoSuchElementException: %s" %e)
                self.get_windows_img()  # 失败了就截图

        elif selector_by == "l" or selector_by == 'link_text':
            try:
                element = self.driver.find_element_by_link_text(selector_value)
                logger.info("Had find the element  %s  successful "
                        "by %s via value: %s " % (element.text, selector_by, selector_value))
            except Exception as e:
                logger.info("not find by link_text to element")
                logger.error("NoSuchElementException: %s" %e)
                self.get_windows_img()  # 失败了就截图

        elif selector_by == "p" or selector_by == 'partial_link_text':
            try:
                element = self.driver.find_element_by_partial_link_text(selector_value)
                logger.info("Had find the element  %s  successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("not find by partial_link_text to element")
                logger.error("NoSuchElementException: %s" %e)
                self.get_windows_img()  # 失败了就截图

        elif selector_by == "t" or selector_by == 'tag_name':
            try:
                element = self.driver.find_element_by_tag_name(selector_value)
                logger.info("Had find the element  %s successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("not find by tag_name to element")
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # 失败了就截图

        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logger.info("Had find the element  %s successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("not find by xpath to element")
                logger.error("NoSuchElementException: %s" % e)
                self.get_windows_img()  # 失败了就截图

        elif selector_by == "s" or selector_by == 'selector_selector':
            try:
                element = self.driver.find_element_by_selector_selector(selector_value)
                logger.info("Had find the element  %s  successful "
                            "by %s via value: %s " % (element.text, selector_by, selector_value))
            except NoSuchElementException as e:
                logger.info("not find by selector_selector to element")
                logger.error("NoSuchElementException: %s" %e)
                self.get_windows_img()  # 失败了就截图

        else:
            raise NameError("Please enter a valid type of targeting elements.")


        return element
    #输入
    def type_input(self,selector,text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logger.info("Had type \' %s \' in inputBox" %text)
        except NameError as e:
            logger.error("Failed to type in input box with %s" %e)
            self.get_windows_img()
    #清除文本框
    def clear(self, selector):
        el = self.find_element(selector)
        try:
            el.clear()
            logger.info("Clear text in input box before typing.")
        except NameError as e:
            logger.error("Failed to clear in input box with %s" %e)
            self.get_windows_img()
    #链接点击
    def a_click_element(self,selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The page is change ")
        except NameError as e:
            logger.info(" a click fail")
            logger.error("Failed to click the element with %s" %e)
    #按钮点击元素
    def click_element(self,selector):
        el = self.find_element(selector)
        try:
            el.click()
            logger.info("The element %s  was clicked." %el.text)
        except NameError as e:
            logger.info("click fail")
            logger.error("Failed to click the element with %s" %e)
    #网页标题
    def get_page_title(self):
        logger.info("Current page title is %s " %self.driver.title)
        return self.driver.title
    #设置页面大小
    def set_window_Size(self,width,height):
        self.driver.set_window_size(width,height)
        logger.info("set window size width: %s height:%s " %(width,height))
    # 鼠标右击
    def mouse_right_click(self,selector):
        el = self.find_element(selector)
        ActionChains(self.driver).context_click(el).perform()
        logger.info("mouse right click")
    #鼠标悬停
    def mouse_move_to_element(self,selector):
        el = self.find_element(selector)
        ActionChains(self.driver).move_to_element(el).perform()
        logger.info("mouse move to element ")
    #页面抓取
    def mouse_drag_drop(self,source,target):
        source = self.find_element(source)
        target = self.find_element(target)
        ActionChains(self.driver).drag_and_drop(source,target)
    #表单提交
    def form_submit(self,selector):
        el = self.find_element(selector)
        el.submit()
        logger.info("submit")
    #刷新
    def F5(self):
        self.driver.refresh()
        logger.info("refresh")
    #js
    def js(self,script):
        self.driver.execute_script(script)
        logger.info("use  the js")
    #获取元素信息
    def element_get_attribute(self,selector,attribute):
        el = self.find_element(selector)
        return el.get_attribute(attribute)
        logger.info("get the element's attribute")
    #text
    def get_text(self,selector):
        el = self.find_element(selector)
        return el.text
        logger.info("get element's text")
    #元素是否显示
    def get_display(self,selector):
        el = self.find_element(selector)
        return el.is_displayed()
        logger.info("use  display")
    #页面标题
    def get_window_title(self):
        return self.driver.title
        logger.info("get window title")
    #接收弹出框
    def accept_alert(self):
        self.driver.switch_to.alert.accept()
        logger.info("agree alert")
    #不接受弹出框
    def dismiss_alert(self):
        self.driver.switch_to.alert.dismiss()
        logger.info("don't agree alert")
    #切换表单
    def switch_to_frame(self,selector):
        iframe_el = self.get_element(selector)
        self.driver._switch_to.frame(iframe_el)
        logger.info("switch the frame")
    #返回上一级表单
    def switch_to_frame_out(self):
        self.driver.switch_to.default_content()
        logger.info("go back")
    #获得当前页面句柄
    def get_current_window_handle(self):
        return self.driver.current_window_handle
        logger.info("get current handle")
    #获取所有页面句柄
    def get_window_handles(self):
        return self.driver.window_handles
        logger.info("get all handle")
    #切换句柄
    def switch_to_other_window(self,handle):
        self.driver.switch_to.window(handle)
        logger.info("switch handle")
    #获取cookie信息
    def get_cookie(self):
        return self.driver.get_cookies()
        logger.info("get cookies")
    #清除cookie
    def del_cookie(self):
        self.driver.delete_all_cookies()
        logger.info("delete all cookies")
    #键盘操作
    def ctrl_a(self,selector,word):
        el=self.driver.find_element(selector)
        el.send_keys(Keys.CONTROL,word)
        logger.info("ctrl + %s" %word)
    #免验证码登入
    def get_add_login_cookies(self,domain,account_name,account_value, passwd_name,passwd_value):
        cookie_account_name ={
            'domain': domain, 'name': account_name,'value': account_value
        } #百度的name
        cookie_password_name ={
            'domain': domain, 'name': passwd_name,'value': passwd_value
        }
        self.driver.add_cookie(cookie_account_name)  # 添加cookie ，通过Cookie登陆
        self.driver.add_cookie(cookie_password_name)
        logger.info("login finish")
    #sleep等待
    @staticmethod
    def time_sleep(seconds):
        time.sleep(seconds)
        logger.info("Sleep for %d seconds" %seconds)