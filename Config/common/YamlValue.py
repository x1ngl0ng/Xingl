#热加载

import yaml
import json
import re
import random
import yaml
import json
import re
import random

class DiYAml:
    """

    """

    def get_extract_yaml(self, a, b=None):
        """
        params:yaml的层级，a为第一层，b为第二层，要读取的yaml数据层级
        return： <class 'list'>
        """
        file_path = 'L:\PythonCode\Interfaceframework\Config\common\data.yaml'
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
                if b is None:
                    return data[a]
                else:
                    return data.get(a, [])[int(b)] if isinstance(data.get(a, []), list) else data.get(a, {}).get(b)

        except yaml.YAMLError as e:
            print(f"读取yaml文件失败，请检查格式{file_path},{e}")
        except Exception as e:
            print(f'未知异常{e}')

    def get_extratc_data(self, a, b=None):
        """
        params：
            b: 调用 self.seq_read(data, b) 获取指定索引的数据。
            0: 从 data 中随机选择一个元素。
            -1: 将 data 中的所有元素连接成一个字符串，元素之间用逗号分隔。
            -2: 将 data 中的所有元素连接成一个字符串后再分割成列表。
        return：
            如果 b 是整数且满足条件，则返回 data_value 字典中对应 b 的值。
            如果 b 不符合整数条件，则返回 get_extract_yaml(a, b) 的结果。
        """
        data = self.get_extract_yaml(a)
        if b is not None and bool(re.compile(r'^[+-]?\d+$').match(str(b))):
            b = int(b)
            data_value = {
                b: self.seq_read(data, b),
                0: random.choice(data),
                -1: ','.join(data),  # join只能对字符串操作
                -2: ','.join(data).split(',')
            }
            data = data_value[b]
        else:
            data = self.get_extract_yaml(a, b)
        return data

    def seq_read(self, data, randoms):
        if randoms not in [0, -1, -2]:
            return data[randoms - 1]
        else:
            return None

        #todo:这个方法现存在bug，只能接受二级层级输出，索引处理不了
    def parse_and_replace_variables(self, yaml_data):
        """
        正则表达式，提取yaml文件中的“${get_extract_yaml(goddsid,-1)}”部分，并且解析出来执行函数和参数并执行，为了解决上下游接口传参的问题
        params：读取1个yaml文件
        return：完整yaml
        """
        yaml_str = yaml_data if isinstance(yaml_data, str) else json.dumps((yaml_data))

        for _ in range(yaml_str.count('${')):
            if '${' in yaml_str and '}' in yaml_str:
                startindex = yaml_str.index('$')
                endindex = yaml_str.index('}', startindex)
                ys = yaml_str[startindex:endindex + 1]
                match = re.match(r'\$\{(\w+)\((.*?)\)\}', ys)
                if match:
                    func_name, func_params = match.groups()
                    func_params = func_params.split(',') if func_params else []
                    extract_data = getattr(DiYAml(), func_name)(*func_params)
                    yaml_str = re.sub(re.escape(ys), str(extract_data), yaml_str)
        try:
            data = json.loads(yaml_str)
        except json.JSONDecodeError:
            data = yaml_str

        return data

    def get_id(self):
        return 333


if __name__ == '__main__':
    dy=DiYAml()
    file_path = 'L:\PythonCode\learn\基础\data.yaml'
    resa=dy.get_extract_yaml('goddsid')
    print('shishi',type(resa))
    # res=get_extract_yaml('data')
    # print(res)
    res=dy.get_extratc_data('data')
    print(res)
    parv=dy.parse_and_replace_variables(res)
    print('dsd',parv)
