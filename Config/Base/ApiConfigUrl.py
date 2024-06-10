class APIConfig:
    BASE_URL = "http://192.168.202.132:8080"
    MysqlUrl = BASE_URL.split("//",1)[-1]
    Token =BASE_URL + "/v7/login"
    Create_Identity = BASE_URL + "/pimpeople"#新建用户
    Serch_info = BASE_URL + "/pimpeople/fetchygxxgly"#查询用户
    Save_Identity = BASE_URL + "/pimpeople"+"/427a626493cb0d09c30b145333db757b"
    USER_INFO_URL = BASE_URL + "/user/info"

    usr="{}"





    # 下面是接口名称：_________________________________________________________________________________________

