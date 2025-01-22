import os
import time

import requests
import hashlib
import base64
import json


def string_to_md5(input_string):
    """
    将字符串转换为MD5哈希值

    :param input_string: 输入字符串
    :return: MD5哈希值
    """
    md5_hash = hashlib.md5()  # 创建一个md5哈希对象
    md5_hash.update(input_string.encode('utf-8'))  # 更新哈希对象，使用输入字符串的UTF-8编码
    return md5_hash.hexdigest()  # 返回16进制表示的哈希值


def load_config(config_path='config.json'):
    """
    读取并解析配置文件

    :param config_path: 配置文件的路径，默认为 'config.json'
    :return: 解析后的配置数据
    """
    if not os.path.exists(config_path):  # 检查配置文件是否存在
        raise FileNotFoundError(f"配置文件 {config_path} 未找到")  # 如果不存在则抛出异常

    with open(config_path, 'r', encoding='utf-8') as file:  # 打开配置文件
        config_data = json.load(file)  # 使用json模块解析文件内容

    return config_data  # 返回解析后的配置数据


def hyper3d_process_image_to_3d(image_url, api_key):
    """
    处理图像转换为3D模型并下载生成的GLB文件

    :param image_url: 图像的 URL 或 base64 编码数据 URI
    :param api_key: API 密钥
    :return: 下载的文件路径
    """
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    if image_url.startswith("data:image/"):  # 判断是否为base64编码的图像
        # 处理 base64 编码的图像
        image_data = image_url.split(",")[1]  # 获取base64编码部分
        image_data = base64.b64decode(image_data)  # 解码base64编码的数据
        file_extension = image_url.split(";")[0].split("/")[-1]  # 获取文件扩展名
        file_name = f"image.{file_extension}"  # 构建文件名
    else:
        # 处理图像 URL
        response = requests.get(image_url)  # 发送GET请求获取图像
        response.raise_for_status()  # 检查请求是否成功
        image_data = response.content  # 获取响应内容（图像数据）
        file_name = os.path.basename(image_url)  # 获取URL中的文件名

    files  = [
        ('images', image_data)
    ]

    response = requests.post(
        "https://hyperhuman.deemos.com/api/v2/rodin",
        headers=headers,
        files=files
    )
    response.raise_for_status()
    # 解析JSON响应
    response_data = response.json()
    print("hyper3d", response_data)

    task_id = response_data["uuid"]

    # 获取任务结果
    while True:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        response = requests.post(
            "https://hyperhuman.deemos.com/api/v2/download",
            headers=headers,
            json={"task_uuid": task_id}
        )
        response.raise_for_status()
        task_result = response.json()
        print("hyper3d", task_result)
        if len(task_result['list']) == 2:
            break
        time.sleep(3)

    # 假设响应中包含3D模型文件的URL
    output_url = task_result['list'][0]['url']

    # 下载文件
    local_filename = f"downloads/hyper3d_{string_to_md5(output_url)}.glb"  # 构建本地文件路径
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)  # 创建必要的目录

    with requests.get(output_url, stream=True) as r:  # 发送GET请求下载文件
        r.raise_for_status()  # 检查请求是否成功
        with open(local_filename, 'wb') as f:  # 打开本地文件以二进制模式写入
            for chunk in r.iter_content(chunk_size=8192):  # 分块读取文件内容
                f.write(chunk)  # 写入文件

    print(f"文件已下载到: {local_filename}")  # 打印下载完成信息
    return local_filename  # 返回下载的文件路径


if __name__ == "__main__":
    config = load_config()  # 加载配置文件
    imageUrl = "https://hao-wa-ai.obs.cn-south-1.myhuaweicloud.com/a04e2035e5eae852ce8b2e7d443eabde.png"  # 图像URL

    apiKey = config['app']['hyper3d']['key']  # 获取API密钥
    # 创建任务
    downloaded_file_path = hyper3d_process_image_to_3d(imageUrl, apiKey)  # 调用函数处理图像并下载3D模型
