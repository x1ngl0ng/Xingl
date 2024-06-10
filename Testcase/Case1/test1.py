import json

import requests
import requests

from Config.common.YamlDispos import YamlDispos

url = "http://192.168.202.131:8080/pimpeople/427a626493cb0d09c30b145333db757b"
# put_data = {
#   "updatedate": "2024-06-03 18:05:39",
#   "pimpersonid": "427a626493cb0d09c30b145333db757b",
#   "pimpersonname": "xinglong333",
#   "orgid": None,
#   "orgsectorid": None,
#   "ygbh": "0001",
#   "zjlx": "10",
#   "csrq": None,
#   "xb": None,
#   "zjhm": "140302199601160430",
#   "nj": None,
#   "xx": None,
#   # "zp": [{"name": "c1a8d893b9bc9b193129409cbc750df7.jpeg", "id": "d4de13b037d3b8087b72eca2bcdf3ab5"}],
#   "lxdh": "17501090037",
#   "dzyx": None,
#   "hyzk": None,
#   "mz": None,
#   "hklx": None,
#   "jg": None,
#   "hjszd": None,
#   "hjdz": None,
#   "csd": None,
#   "postaladdress": None,
#   "sfdszn": None,
#   "ahtc": None,
#   "jkzk": None,
#   "jlczz": None,
#   "zzmm": None,
#   "rtsj": None,
#   "rdsj": None,
#   "ygzt": "30",
#   "workstate": None,
#   "rzqd": None,
#   "yglx": None,
#   "ormorgid": None,
#   "ormorgname": None,
#   "ormorgsectorid": None,
#   "ormorgsectorname": None,
#   "zw": None,
#   "gw": None,
#   "cjgzsj": None,
#   "dbdwsj": None,
#   "sgyy": None,
#   "hmd": None,
#   "blacklistreasons": None,
#   "pimpersonabilities": [],
#   "pimpapers": [],
#   "pimdistirbutions": [],
#   "pimtitles": [],
#   "pimvocationals": [],
#   "pimarmycadres": [],
#   "pimcorrectionapplies": [],
#   "pimvacations": [],
#   "trmtrainpeople": [],
#   "pimcontracts": [],
#   "pimeducations": [],
#   "pimpersonchanges": [],
#   "pimachievements": [],
#   "pimresearchfindings": [],
#   "pimexitandentries": [],
#   "pimrewardpunishments": [],
#   "pimpatents": [],
#   "pimlanguageabilities": [],
#   "pimarchives": [],
#   "pimfaminfos": [],
#   "attendancemreportmxes": [],
#   "pimworkhistories": []
# }
# pp=json.dumps(put_data)
file_paths = r'L:\PythonCode\接口框架\Testcase\Case1\put.yaml'
put_data = YamlDispos.read_yaml(file_path=file_paths)['data']
data = json.dumps(put_data)
print(type(data))

payload = "{\"updatedate\":\"2024-06-03 18:05:39\",\"pimpersonid\":\"427a626493cb0d09c30b145333db757b\",\"pimpersonname\":\"xinglong333\",\"orgid\":null,\"orgsectorid\":null,\"ygbh\":\"0001\",\"zjlx\":\"10\",\"csrq\":null,\"xb\":null,\"zjhm\":\"140302199601160430\",\"nj\":null,\"xx\":null,\"zp\":\"[{\\\"name\\\":\\\"c1a8d893b9bc9b193129409cbc750df7.jpeg\\\",\\\"id\\\":\\\"d4de13b037d3b8087b72eca2bcdf3ab5\\\"}]\",\"lxdh\":\"17501090037\",\"dzyx\":null,\"hyzk\":null,\"mz\":null,\"hklx\":null,\"jg\":null,\"hjszd\":null,\"hjdz\":null,\"csd\":null,\"postaladdress\":null,\"sfdszn\":null,\"ahtc\":null,\"jkzk\":null,\"jlczz\":null,\"zzmm\":null,\"rtsj\":null,\"rdsj\":null,\"ygzt\":\"30\",\"workstate\":null,\"rzqd\":null,\"yglx\":null,\"ormorgid\":null,\"ormorgname\":null,\"ormorgsectorid\":null,\"ormorgsectorname\":null,\"zw\":null,\"gw\":null,\"cjgzsj\":null,\"dbdwsj\":null,\"sgyy\":null,\"hmd\":null,\"blacklistreasons\":null,\"pimpersonabilities\":[],\"pimpapers\":[],\"pimdistirbutions\":[],\"pimtitles\":[],\"pimvocationals\":[],\"pimarmycadres\":[],\"pimcorrectionapplies\":[],\"pimvacations\":[],\"trmtrainpeople\":[],\"pimcontracts\":[],\"pimeducations\":[],\"pimpersonchanges\":[],\"pimachievements\":[],\"pimresearchfindings\":[],\"pimexitandentries\":[],\"pimrewardpunishments\":[],\"pimpatents\":[],\"pimlanguageabilities\":[],\"pimarchives\":[],\"pimfaminfos\":[],\"attendancemreportmxes\":[],\"pimworkhistories\":[]}"
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'zh-CN',
  'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJndWVzdCIsImV4cCI6MTcxNzU3MjcyMCwiaWF0IjoxNzE3NTY1NTIwfQ.aKebRkhskvK_cstcdzh7bpIykFruYQuyhMuurW3kH89E9H7x0qYcIltiR4z0j3ePJYv5-hQAK2fWlw1VJ9RrSQ',
  'Connection': 'keep-alive',
  'Content-Type': 'application/json;charset=UTF-8',
  'Origin': 'http://192.168.202.129:8080',
  'Referer': 'http://192.168.202.129:8080/',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
  'srforgsectorid': 'null'
}

response = requests.request("PUT", url, headers=headers, data=data)
print(response.status_code)

# print(type(pp))
# escaped_str = json.dumps(payloads, ensure_ascii=False)
# print(escaped_str)
# print(type(escaped_str))

# ac=json.loads(payload)
# print(ac)