import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

class  Login_Operation:

    #  登陆的页面逻辑操作,驱动保持3个模块中都得1样
    def  login(self,driver,name,pwd):
        # 输入用户名
        ele = driver.find_element(By.XPATH, "//input[@id='username']")
        ele.send_keys(name)

        # 输入密码
        ele2 = driver.find_element(By.XPATH, "//input[@id='password']")
        ele2.send_keys(pwd)

        #  点击登录
        ele3 = driver.find_element(By.XPATH, "//button[@id='login_btn']")
        ele3.click()
        time.sleep(2)

    def managemoney(self,driver):
        """
        基金理财:点击投资>输入>确认>结果为”买入失败“
        :param login1:登录的夹具
        :param driver:浏览器
        :return:None
        """

        #基金理财
        driver.get('http://127.0.0.1:90/user/finance/toFundProduct.html')

        #点击投资按钮   注意观察 区别，这是页面的两条信息
        # driver.find_element(By.XPATH,"//button[@class='btn btn-primary btn-sm buy_btn' and @buybtnid='1' and @buybtnname='支付宝期限理财']").click()
        el = WebDriverWait(driver,6,poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH,'//button[@class="btn btn-primary btn-sm buy_btn" and @buybtnid="3" and @buybtnname="广发多元新兴股票"]')))
        el.click()

        #点击投资按钮后的弹窗
        time.sleep(1)
        driver.find_element(By.XPATH,'//div[@class="layui-layer-content"]//input[@id="password"]').send_keys('1111')
        wait=WebDriverWait(driver,6,poll_frequency=2)

        #点击小窗口的确认 三种种方法都可以
        confirm_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".layui-layer-btn0")))
        # confirm_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "确定")))
        # confirm_button = WebDriverWait(driver,6,poll_frequency=2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='layui-layer-btn layui-layer-btn-']/a[contains(text(),'确定')]")))
        confirm_button.click()

        #获得买入失败的标题
        fail_info = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".jconfirm-content > div"))).text

        return fail_info

    def safelendmoney(self,driver):

        driver.get("http://127.0.0.1:90/user/tools/toApplyLoan.html")
        # 输入贷款金额
        el = WebDriverWait(driver, 6).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.form-control[type="text"][name="amount"]')))
        el.send_keys('1000')

        # 输入天数
        el1 = WebDriverWait(driver, 6).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.form-control[type="text"][name="term"]')))
        el1.send_keys('3')

        # 点击申请按钮
        # <button class="btn btn-primary" id="submit" type="button"> 这是确认按钮的源元素，特征class的值的空格部分是html语言的类定义规则表示类嵌套
        driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary#submit').click()

        # 这个地方的空格
        time.sleep(1)
        driver.find_element(By.CSS_SELECTOR, 'div.jconfirm-buttons button.btn.btn-default').click()

        # 已取消的弹窗   动态变化的id，所以得忽略id
        # eg: cancel_text = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.jconfirm-content#jconfirm-box77017 div'))).text
        el3 = WebDriverWait(driver, 6).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.jconfirm-content div'))).text

        return el3



    def  getSuccessResult(self,driver):

        time.sleep(1)
        return driver.title
        # return  driver.find_element(By.XPATH, "/html/head/title").text



    def review(self,result,expect,driver):

        if  result == expect:
            print('success')

        else:

            os.mkdir('demo')
            driver.save_screenshot('demo/erro.jpg')

        assert  result == expect
