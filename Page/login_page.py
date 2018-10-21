from Base.Base import Base
import Page

class Login_Page(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

    def login(self,num,pwd):
        self.send_element(Page.login_account_id,num)
        self.send_element(Page.login_passwd_id,pwd)
        self.click_element(Page.login_btn_id)

    def if_login_btn_exists(self):
        try:
            self.search_element(Page.login_btn_id)

        except Exception as e:
            return False

    def close_login_page(self):
        self.click_element(Page.login_close_btn_id)