import yaml
import json

data = {"deviceName": "2bcaca49", "name": "John Doe", "color": "blue"}



class YamlDispos:
    def __init__(self,config_path:str):
        self.config_path = config_path
        # self.params = self.__write_yaml(config_path,data)

    # @staticmethod#写数据返回路径
    # def __write_yaml( file_path, datas):
    #     with open(file_path, "w") as file:
    #         yaml.dump(datas, file)
    #     return file_path

    @staticmethod
    def read_yaml(file_path):
        # file_path=None
        with open(file_path, "r",encoding='utf-8') as file:
            yaml_data = yaml.safe_load(file)
            return yaml_data#本来字典，转成json


if __name__ == '__main__':
    yy=YamlDispos(r"L:\PythonCode\接口框架\Config\common\ddd.yaml")
    ss=yy.read_yaml(r"L:\PythonCode\接口框架\Config\common\ddd.yaml")
    print(ss['header'])
    print(type(ss))
    # print(ss['headers'])
