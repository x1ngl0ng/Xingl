import time

import pytest
from selenium import webdriver
from Login_Operation import Login_Operation
from Login_Data import Login_data


class Test_login(Login_Operation):


    @pytest.fixture(scope='module', params=["chrome", "firefox"])

    def drivers(self, request):
        if request.param == "chrome":
            driver = webdriver.Chrome()
        elif request.param == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError("ValueError")

        driver.get('http://127.0.0.1:90/')
        driver.maximize_window()
        yield driver
        driver.quit()

    @pytest.fixture(scope='module')
    def driver(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:90/')
        driver.maximize_window()
        yield driver
        driver.quit()

    @pytest.fixture()
    def login1(self, driver):
        name='lisi'
        pwd='123456'
        self.login(driver, name, pwd)
        return driver

    @pytest.mark.parametrize('name,pwd,expect', Login_data.Login_data)
    def test_login_1(self,driver, name,login1, pwd, expect):
        print( Login_data.Login_data)
        self.login(driver, name, pwd)
        result=self.getSuccessResult(driver)
        self.review(result,expect,driver)

    def test_moneymange(self,login1,driver):
        """
        这个测试方法会断言失败，expect = '买入失败!', driver = '买入失败!' 但是会失败，还未破解
        :param login1:exit
        :param driver:
        :return:
        """
        result = self.managemoney(driver)
        print(result)
        expect = "买入失败!"
        self.review(driver,result,expect)







