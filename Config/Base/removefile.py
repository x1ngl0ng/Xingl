import os
import json
import yaml

class BaseDispos:
    def read_yaml(self, file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            # 没指定格式：UnicodeDecodeError: 'gbk' codec can't decode byte 0xaa in position 31: illegal multibyte sequence
            yaml_data = yaml.safe_load(file)
            yaml_datas = json.dumps(yaml_data)#Python 对象转换为 JSON 格式的字符串,序列化
        return yaml_datas

'''
当作为字典或二元组列表传递时，将成功编码参数。
如果数据是两个元组的列表，则保持顺序，但如果参数作为字典提供，则保持任意顺序。
# def remove file(self filepath, endlst):
# def删除文件(self filepath, endlst):

'''

    # def remove_file(self,filepath, endlst):
    #     """
    #     删除文件
    #     :param filepath: 路径
    #     :param endlst: 删除的后缀，例如：['json','txt','attach']
    #     :return:
    #     """
    #     try:
    #         if os.path.exists(filepath):
    #             # 获取该目录下所有文件名称
    #             dir_lst_files = os.listdir(filepath)
    #             for file_name in dir_lst_files:
    #                 fpath = filepath + '\\' + file_name
    #                 # endswith判断字符串是否以指定后缀结尾
    #                 if isinstance(endlst, list):
    #                     for ft in endlst:
    #                         if file_name.endswith(ft):
    #                             os.remove(fpath)
    #                 else:
    #                     raise TypeError('file Type error,must is list')
    #         else:
    #             os.makedirs(filepath)
    #     except Exception as e:
    #         logs.error(e)
    # def remove_directory(self,path):
    #     try:
    #         if os.path.exists(path):
    #             os.remove(path)
    #     except Exception as e:
    #         logs.error(e)
if __name__ == '__main__':
    base = BaseDispos()
    read_yaml=base.read_yaml(r'L:\PythonCode\接口框架\Testcase\Case1\login.yaml')
    print(read_yaml)

    # print(read_yaml['test_name'])

