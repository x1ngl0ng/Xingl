# from Config.conf.request import SendRequests
from Config.common.YamlDispos import YamlDispos
from Config.conf.request import SendRequests
from Config.Base.ApiConfigUrl import APIConfig
import json
from Config.Base.removefile import BaseDispos
import requests

class Testbase(SendRequests):
    def tes_create(self):
        url = APIConfig.Create_Identity
        yaml_path=r'L:\PythonCode\接口框架\Testcase\Case1\login.yaml'
        headers = YamlDispos.read_yaml(file_path=yaml_path)['header']
        data = YamlDispos.read_yaml(file_path=yaml_path)['data']#传参得json，yaml得yaml格式
        response = super().run_main(url, data=data, headers=headers)
        return response



    def serchinfo(self):

        yaml_path=r'L:\PythonCode\Interfaceframework\Config\common\ddd.yaml'
        url=APIConfig.Serch_info
        params={'size':10,'query':'xinglong','page':0}  #todo:处理get的传参和URL
        headers = YamlDispos.read_yaml(file_path=yaml_path)['header']
        response = super().run_main(url, params=params,headers=headers)#, verify=False
        # response = requests.request("GET", url, headers=headers, data=payload)
        # print(response)


    def upload(self):

        url = "http://192.168.202.131:8080/ibizutil/upload"

        data = {}
        files = [
            ('file', (
            'image.jpg', open('L:\PythonCode\Interfaceframework\Config\Base\image.jpg', 'rb'),
            'image/png'))
        ]
        print(files)
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'Connection': 'keep-alive',
            'Origin': 'http://192.168.202.131:8080',
            'Referer': 'http://192.168.202.131:8080/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
            'srfappdata': '[object Object]'
        }
        response = super().run_main(url, files=files,headers=headers)
        print(response)

    def putt(self):

        url=APIConfig.Save_Identity
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'http://192.168.202.131:8080',
            'Referer': 'http://192.168.202.131:8080/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'srforgsectorid': 'null'
        }
        file_paths=r'L:\PythonCode\接口框架\Testcase\Case1\put.yaml'
        put_data=YamlDispos.read_yaml(file_path=file_paths)['data']
        print(put_data)
        response = super().special(url, put_data, headers=headers)
        print(response.status_code)




if __name__ == '__main__':
    TT=Testbase()
    # print(re)

    # cc=TT.tes_create()
    # TT.serchinfo()
    TT.putt()
    # TT.upload()
    # print(type(reget))
    # print(reget.json())
