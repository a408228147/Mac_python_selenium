from framework.base_page import BasePage


class HomePage(BasePage):
    #HomePage 继承了BasePage的driver
    input_box = "id=>kw"
    search_submit_btn = "xpath=>//input[@id='su']"
    #百度新闻入口
    news_link = "link_text=>新闻"

    def a_click_news(self):
        self.a_click_element(self.news_link)
        self.time_sleep(2)

    def type_search(self, text):
        self.type_input(self.input_box, text)

    def send_submit_btn(self):
        self.click_element(self.search_submit_btn)

    def get_windows_img(self):
        self.get_window_img()

    def time_sleeps(self,seconds):
        self.time_sleep(seconds)

