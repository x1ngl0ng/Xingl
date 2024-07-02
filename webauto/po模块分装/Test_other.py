import pytest
from Login_Operation import Login_Operation
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class TestOther(Login_Operation):


    def test_update(self,driver,login1):


        driver.get('http://127.0.0.1:90/user/finance/toBank.html')
        #点击右上角lisi图标
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-toggle='dropdown']"))).click()

        #点击右上角个人信息
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), '个人信息')]"))).click()
        WebDriverWait(driver, 4).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/user/personal/toProfile.html')]"))).click()
        #点击保存按钮
        WebDriverWait(driver,4).until(EC.element_to_be_clickable((By.XPATH,'//button[@id="updateUserBtn" and @type="button"]'))).click()






if __name__ == '__main__':
    pytest.main(['-v','./po模块分装'])
