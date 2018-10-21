from Page.page import Page
from Base.get_driver import get_driver

page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

page_obj.get_home_page_obj().click_my_btn()
page_obj.get_sign_page_obj().click_exist_btn()
page_obj.get_login_page_obj().login("111","123")

page_obj.get_login_page_obj().get_toast('此用户')

page_obj.driver.quit()