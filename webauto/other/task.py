import pytest
#一、——————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
夹具可以 传参，参考下这个案例 把双驱动的事情做下，firefox或者ie；没用夹具的可以使用 [pytest -n 2] 实现。
"""
@pytest.fixture(params=[(1, 2), (3, 4), [5, 6]])
# 使用request方法传入夹具参数
def input_data(request):
    # 使用request.param调用夹具参数
    # 同parametrize 会输出(1, 2)、(3, 4)、[5, 6]
    print(request.param)
    return request.param


def add(a, b):

    return a + b


def test_add(input_data):

    a, b = input_data
    result = add(a, b)
    assert result == a + b



#二 、————————————————————————————————————————————————————————————————————————————————————————————————————————————
# 模拟用户账户密码
@pytest.fixture
def user(request):

    user_type = request.param
    if user_type == "admin":
        return {"username": "admin", "password": "admin123"}
    elif user_type == "guest":
        return {"username": "guest", "password": "guest123"}
    elif user_type == "user":
        return {"username": "user", "password": "user123"}
    else:
        raise EnvironmentError("invalid enumerate type: " + user_type)



@pytest.fixture()
def dev(request):
    # 模拟环境设置逻辑
    env_type = request.param
    #模拟测试环境地址
    if env_type == "test":
        return {"url": "https://test.request.cn"}
    #模拟预发地址环境
    elif env_type == "pre":
        return {"url": "https://pre.request.cn"}
    #模拟线上真实环境地址
    elif env_type == "online":
        return {"url": "https://online.request.cn"}
    else:
        raise EnvironmentError("invalid enumerate type: " + env_type)




@pytest.mark.parametrize("user", ["admin", "guest", "user"],ids=["TestDev",'PreDev','OnlineDev'], indirect=True)
@pytest.mark.parametrize("dev", ["test", "pre", "online"], ids = ['AdminUser', 'GuestUser', 'UserUser'],indirect=True)
"""
利用笛卡尔积数规则，达到在不同环境测试执行测试方法；
indirect=True 默认为False，如果为true 为间接调用；就是会传递给相同名称的的fixture进行参数的预处理，然后再传递给测试函数
ids：可以是一个列表或生成器函数，提供1个友好的测试标识 用于为每个参数集生成一个标识符（ID）
"""
def test_user_login(user, dev):
    # 模拟登录逻辑
    url = dev["url"]
    username = user["username"]
    password = user["password"]
    print(f"Logging {url} as {username} with password {password}")
