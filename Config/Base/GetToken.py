from Config.Base.ApiConfigUrl import APIConfig
from Config.common.YamlDispos import YamlDispos
import requests
from functools import wraps
from functools import wraps

class GetToken:
    @staticmethod
    def get_token():
        url = APIConfig.Token
        data = {"loginname": "guest", "password": "guest"}
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'zh-CN',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Cookie': 'loginname=guest',
            'Origin': 'http://192.168.3.179:8080',
            'Referer': 'http://192.168.3.179:8080/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
            'srforgsectorid': 'null'
        }

        response = requests.post(url, headers=headers, json=data)
        json_response = response.json()
        token = json_response.get('token')
        return token

def with_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = GetToken.get_token()
        headers = kwargs.get('headers', {})
        headers['Authorization'] = f'Bearer {token}'
        kwargs['headers'] = headers
        return func(*args, **kwargs)
    return wrapper




if __name__ == '__main__':
    token=GetToken()
    cc=token.get_token()
    print(cc)
    print(type(cc))

