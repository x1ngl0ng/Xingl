import time

import pytest
from selenium import webdriver
from Login_Operation import Login_Operation
from Login_Data import Login_data

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class Test_login(Login_Operation):
    """
    :param: scope :
                "function"：默认值。每个测试函数都会调用一次 fixture。
                "module"：在每个测试模块中，fixture 只会调用一次。
                "class"：在每个测试类的所有方法中，fixture 只会调用一次。
                "session"：在整个测试会话期间，fixture 只会调用一次。  命令执行的时候
    :param: params=[] 表示这个 fixture 会被调用len(params)次，每次使用一个不同的参数值
    :param : autouse=True 为自动调用 autouse=False 时得显示调用才能调用fixture  false也是夹具的默认状态

    """
    @pytest.fixture(scope='module', params=["chrome", "firefox"])
    def drivers(self, request):
        """
        实现双驱动方式，会按顺序执行
        :param request:是一个fixture的内置对象，request.param 返回当前测试用例的参数值
        :return:携带不同的驱动
        """
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
        self.review(result,expect)


















