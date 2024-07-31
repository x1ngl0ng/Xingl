import time

import pytest
from selenium import webdriver
from Login_Operation import Login_Operation
from Login_CASE import Login_data

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementNotInteractableException,TimeoutException,InvalidSelectorException,NoSuchElementException
from selenium.common.exceptions import *


class Test_case(Login_Operation):

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

    def test_createcard(self,driver):
        driver.get("http://127.0.0.1:90/user/personal/toBankCard.html")
        #修改最后1个数据，因为是新添加的
        lastdata = driver.find_elements(By.XPATH,'//div[@class="col-sm-12"]').pop(-1)
        #在上1条的基础上获得银行卡类别（借记卡 or 信用卡）
        types = lastdata.find_element(By.CSS_SELECTOR,'div.card-header.bg-primary > div').text
        bankcradtype = types.replace("(", "").replace(")", "").split()
        driver.find_element(By.XPATH,'//button[@id="bankCard_add_modal_btn"]').click()
        time.sleep(2)

        driver.find_element(By.XPATH,'//input[@type="text" and @id="cardBank_add_input"]').send_keys('银行卡所属银行')
        try:#看看这段有没有错
            if bankcradtype[1] == "借记卡":
                el = driver.find_elements(By.CLASS_NAME, "lyear-radio")
                el[1].click()
            elif bankcradtype[1] == "信用卡":
                el = driver.find_elements(By.CLASS_NAME, "lyear-radi")
                el[0].click()

        #如果try报错了 看看有没有以下的错
        except TimeoutException as e:
            print("元素等待超时，常为显示等待披露的错误；解决：增加等待时间，调整等待条件")
            raise "我自定义1个异常，并且重新引发except的错，再把我自定义的异常添加到捕获到的异常之后" from e

        except InvalidSelectorException as e:

            print("源元素定位语法有问题；解决：修改元素定位脚本")
            raise #重新引发这次异常

        except NoSuchWindowException as e:#这个要导入错误
            print("不对不存在的窗口或标签进行操作；解决：切换到当前页面")

        except ElementClickInterceptedException as e:
            print("元素不可以点击或被覆盖了，常见于依赖1个前置操作；解决：确保该元素在页面上没有遮挡")

        except WebDriverException as e:
            print("所有关于浏览器驱动的错误；解决：会披露具体内容eg：版本不匹配，未找到")

        except IndexError as e:
            print(f"索引越界: {e}解决：确保列表有足够元素")

        except NoSuchElementException as e:
            print(f"元素未找到: {e}")

        except StaleElementReferenceException as e:
            print(f"对过期或已被移除元素引用: {e}解决：常见于弹窗，曾经出现过引用的时候已经是关闭状态")

        except ElementNotInteractableException as e:
            print(f"元素不可操作: {e}解决：确保元素可见")

        except Exception as e:
            print(f"发生其他错误: {e}")

        else:#如果上面 except没错 就执行
            driver.find_element(By.ID, 'cardNum_add_input').send_keys('12345678945213123')
            time.sleep(2)

        finally:#不管错没错都执行
            print("finally下的不管错没错都执行")






















