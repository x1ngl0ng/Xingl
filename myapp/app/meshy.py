import json
import os
import time
import requests
import hashlib
import base64

def string_to_md5(input_string):
    """
    将字符串转换为MD5哈希值

    :param input_string: 输入字符串
    :return: MD5哈希值
    """
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()


def load_config(config_path='config.json'):
    """
    读取并解析配置文件

    :param config_path: 配置文件的路径
    :return: 解析后的配置数据
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"配置文件 {config_path} 未找到")

    with open(config_path, 'r', encoding='utf-8') as file:
        config_data = json.load(file)

    return config_data


def meshy_process_image_to_3d(image_url, api_key):
    """
    处理图像转换为3D模型并下载生成的GLB文件

    :param image_url: 图像的 URL 或 base64 编码数据 URI
    :param api_key: API 密钥
    :return: 下载的文件路径
    """
    # 创建任务
    payload = {
        "image_url": image_url,
        "enable_pbr": True,
        "should_remesh": True,
        "should_texture": True
    }
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(
        "https://api.meshy.ai/openapi/v1/image-to-3d",
        headers=headers,
        json=payload,
    )
    response.raise_for_status()
    result = response.json()
    print("meshy", result)
    task_id = result['result']

    # 获取任务结果
    while True:
        try:
            response = requests.get(
                f"https://api.meshy.ai/openapi/v1/image-to-3d/{task_id}",
                headers=headers,
            )
            response.raise_for_status()
            task_result = response.json()
            print("meshy", task_result)
            if task_result['status'] == 'SUCCEEDED':
                break
            time.sleep(3)
        except requests.exceptions.RequestException as e:
            print("meshy", f"请求失败: {e}")
            time.sleep(3)

    output_url = task_result['model_urls']['glb']

    # 下载文件
    local_filename = f"downloads/meshy_{string_to_md5(output_url)}.glb"
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)

    with requests.get(output_url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print("meshy", f"文件已下载到: {local_filename}")
    return local_filename


if __name__ == "__main__":
    config = load_config()
    imageUrl = "https://hao-wa-ai.obs.cn-south-1.myhuaweicloud.com/a04e2035e5eae852ce8b2e7d443eabde.png"

    apiKey = config['app']['meshy']['key']
    # 创建任务
    downloaded_file_path = meshy_process_image_to_3d(imageUrl, apiKey)
