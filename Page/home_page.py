from Base.Base import Base
import Page

class Home_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def click_my_btn(self):
        self.click_element(Page.my_btn_id)

