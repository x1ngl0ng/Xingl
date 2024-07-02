import time

import pytest
from selenium import webdriver
from Login_Operation import Login_Operation
from Login_Data import Login_data

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class Test_login(Login_Operation):

    @pytest.mark.parametrize('name,pwd,expect', Login_data.Login_data)
    def test_login_1(self,driver, name,login1, pwd, expect):
        """

        :param driver: ……
        :param name: 参数化的账号
        :param login1: 登录 测试登录就用父类封装好的登录页面逻辑，使用登录就使用夹具里的登录，理解这个思想，可以想下还有哪些场景可以利用这个思想
        :param pwd: ……
        :param expect: ……
        :return:
        """
        print( Login_data.Login_data)
        self.login(driver, name, pwd)
        result=self.getSuccessResult(driver)
        self.review(result,expect,driver)


    def test_moneymange(self,login1,driver):
        """
        :param login1:登录
        :param driver:页面
        :return:
        """
        result = self.managemoney(driver)
        print(result)
        expect = "买入失败!"
        self.review(driver,result,expect)

    def test_safelendmoney(self,driver,login1):

        result = self.safelendmoney(driver)
        expect = "已取消!"
        self.review(result,expect,driver)


















