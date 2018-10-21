from Base.Base import Base
import Page

class Person_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def get_con_text(self):
        return self.search_element(Page.person_coupons_id).text

    def click_setting_btn(self):
        self.click_element(Page.setting_btn_id)