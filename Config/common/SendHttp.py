'''
请求和响应
'''
import requests
url='http//127.0.0.1:8787//dar/user/login'

header={'Content-Type':'application/x-www-formurlencoded;charset=UTF-8'}

data={"user_name":"test01","passwd":"admin1234"}

res=requests.post(url=url,data=data)
ress=requests.get(url=url,data=data)

print(res.text)
print(res.content)#文本类型
print(res.json())
#总体调用，不需要写明post或get，接口信息在yaml
see=requests.session()
see.request(method='get',url=url,params=data,headers=header)