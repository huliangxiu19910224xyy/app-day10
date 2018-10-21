import time

from Base.Base import Base
import Page

class Setting_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_logou_btn(self, tag=1):
        # 向上滑动
        time.sleep(2)
        self.screen_scroll(1)

        self.click_element(Page.logout_btn_id)
        if tag:
            # 点击确认退出
            self.click_element(Page.logout_acc_btn_id)

        else:
            # 点击取消退出
            self.click_element(Page.log_out_miss_btn_id)