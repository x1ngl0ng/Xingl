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
    def read_yaml(file_path, target=None):
        if target is None:
            raise ValueError(f'当前target为{target}，检查yaml层级')

        with open(file_path, "r", encoding='utf-8') as file:
            yaml_data = list(yaml.safe_load_all(file))
            for index, value in enumerate(yaml_data):
                if index == target:
                    return value

            raise IndexError(f'目标索引 {target} 超出范围，共有 {len(yaml_data)} 个文档')



if __name__ == '__main__':
    yy=YamlDispos(r"L:\PythonCode\接口框架\Config\common\ddd.yaml")
    ss=yy.read_yaml(r"L:\PythonCode\接口框架\Config\common\ddd.yaml")
    print(ss['header'])
    print(type(ss))
    # print(ss['headers'])
