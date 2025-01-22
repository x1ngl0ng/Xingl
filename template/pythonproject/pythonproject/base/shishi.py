import json

from Config.common.YamlValue import DiYAml
from Config.common.YamlDispos import YamlDispos

class YamlHandler:
    def __init__(self):
        # 假设你有一些方法定义
        pass

    def get_extract_data(self, ):
        a =1
        b =2
        c = a+b

        return f"Value of {c}"

    def replace_load(self, data):
        """yaml数据替换解析"""
        str_data = data
        if not isinstance(data, str):
            str_data = json.dumps(data, ensure_ascii=False)

        # 循环查找${}模式并替换
        while '${' in str_data and '}' in str_data:
            start_index = str_data.index('${')  # 查找${的位置
            end_index = str_data.index('}', start_index)  # 查找}的位置

            # 获取 ${} 中的内容
            ref_all_params = str_data[start_index:end_index + 1]

            # 提取函数名和参数
            func_name = ref_all_params[2:ref_all_params.index("(")]  # 函数名
            func_params = ref_all_params[ref_all_params.index("(") + 1:ref_all_params.index(")")]  # 参数

            # 调试打印
            print(f"Function name: {func_name}")
            print(f"Function parameters: {func_params}")

            # 动态获取函数并传入参数
            # 假设你已经知道哪些函数存在，可以通过self.get_yaml_data等
            func = getattr(self, func_name, None)  # 获取当前类中的方法
            if func:
                # 处理函数的参数，如果有多个参数，用逗号分隔
                params = func_params.split(',') if func_params else []
                # 调用函数并获取返回值
                extract_data = func(*params)

                # 如果返回的是列表类型，转为逗号分隔的字符串
                if isinstance(extract_data, list):
                    extract_data = ','.join(extract_data)

                # 替换原字符串中的${}部分
                str_data = str_data.replace(ref_all_params, str(extract_data))
            else:
                print(f"Function '{func_name}' not found.")

        # 还原数据格式
        if isinstance(data, dict):
            data = json.loads(str_data)
        else:
            data = str_data
        return data

if __name__ == '__main__':

    # 测试代码



    yd=YamlDispos
    ss=yd.read_yaml(r"L:\PythonCode\Interfaceframework\Config\common\ddd.yaml",'params')
    yh = YamlHandler()
    print(yh.get_extract_data())
    result = yh.replace_load(ss)
    print(result)
