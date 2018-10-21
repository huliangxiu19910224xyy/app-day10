import sys,os

from selenium.common.exceptions import TimeoutException

sys.path.append(os.getcwd())

from Base.get_driver import get_driver
from Page.page import Page
import pytest
from Base.get_data import Get_Data

def get_login_data():
    login_list = []
    data = Get_Data().get_yaml_data("login.yml")
    for i in data.keys():
        login_list.append((i, data.get(i).get("phone"),
                              data.get(i).get("passwd"),
                              data.get(i).get("tag"),
                              data.get(i).get("tag_message"),
                              data.get(i).get("expect_result")))
    return login_list

class Test_Login():
    def setup_class(self):
        self.page_obj = Page(get_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity"))

    def teardown_class(self):
        self.page_obj.driver.quit()

    @pytest.mark.parametrize("test_num,phone,passwd,tag,tag_mess,expect_result",get_login_data())
    def test_login(self,test_num,phone,passwd,tag,tag_mess,expect_result):
        """
        :param test_num:
        :param phone:
        :param passwd:
        :param tag:
        :param tag_mess:
        :param expect_result:
        :return:
        """
        # 点击我的
        self.page_obj.get_home_page_obj().click_my_btn()
        # 点击已有账号，去登陆
        self.page_obj.get_sign_page_obj().click_exist_btn()
        # 登录操作
        self.page_obj.get_login_page_obj().login(phone,passwd)
        # 判断成功失败用例
        if tag:  # 预期成功的用例
            try:  #断言我的优惠券在不在个人中心页面，如果内容改变也不影响后面退出操作
                # 优惠券
                coupons = self.page_obj.get_person_page_obj().get_con_text()
                try:
                    # 断言
                    assert coupons == expect_result
                except AssertionError as e:
                    print(e.__str__())
                # 执行退出操作
                # 点击设置
                self.page_obj.get_person_page_obj().click_setting_btn()
                self.page_obj.get_setting_page_obj().click_logou_btn()

            except TimeoutException as e:  # 如果预期成功的用例没有登录成功，关闭登录页面
                # 关闭登录页面
                self.page_obj.get_login_page_obj().close_login_page()
                assert False

        # else:
        #     # 预期失败的用例
        #     try:
        #         # 获取toast消息
        #         toast_mess = self.page_obj.get_login_page_obj().get_toast(tag_mess)
        #         if_login = self.page_obj.get_login_page_obj().if_login_btn_exists()
        #         # 断言
        #         assert if_login and toast_mess == expect_result
        #
        #     except AssertionError as e:
        #         assert False
        #
        #     finally:
        #         # 关闭登录页面
        #         self.page_obj.get_login_page_obj().close_login_page()





