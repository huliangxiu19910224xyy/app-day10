from Base.Base import Base
import Page

class Sign_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    
    def click_exist_btn(self):
        self.click_element(Page.exits_account_id)