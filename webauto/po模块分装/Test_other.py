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

    """
    !!!前提是工作目录要进入到包含测试.py的目录，.py以test开头!!!
    
    命令行执行模式：
    一、执行某个类里的所有测试方法：
    pytest path/to/test_file.py::TestClassName
    （pytest + 路径::类名）
    
    二、执行某个类里的1个测试方法：
    pytest path/to/test_file.py::TestClassName::test_method
    pytest -vv path/to/test_file.py::TestClassName::test_method
    （pytest + 路径::指定某测试类名::某测试方法）
    （-v 输出详细信息eg：每个测试函数的结果（通过、失败等）所有状态都会被列出）
    （-vv 相对“-v”更加详细）
    
    三、只运行上次失败的case：
    pytest --lf

    四、运行全部case：
    假如你所有的用例的.py文件放在一个以TestCase的文件夹下，
    pytest.main('-v','./TestCase') 主函数
    pytest -v ./TestCase 命令行
    
    五、并行
    pip install pytest-xdist
    pytest -n 4  -v ./po模块分装
    tp：
    分配策略：
		每个进程会处理多个测试方法平均分配，具体的可能会收到测试框架和系统资源有所不同，
	    进程和线程：线程是并发，进程则是独立的执行环境
	    每个进程执行完成后，pytest 会将各个进程的测试结果汇总显示
	    
    进程：独立、每个进程都有自己独立的内存空间和运行环境
        通信：需要操作系统提供的机制，如管道、共享内存、消息队列
        并发：多个进程互相不干扰，但是进程切换开销比较打
	线程：
		共享、它们可以直接访问同一进程中的所有资源
		通信：相对简单、通过共享内存实现
		并发：多线程可以在同一进程内并发执行，相互切换开销比较小
	总结：
	    一个进程可以包含多个线程，即多个线程共享相同的进程资源。

    

    """



