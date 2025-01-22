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

def tripo3d_process_image_to_3d(image_url, api_key):
    """
    处理图像转换为3D模型并下载生成的GLB文件

    :param image_url: 图像的 URL 或 base64 编码数据 URI
    :param api_key: API 密钥
    :return: 下载的文件路径
    """
    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    if image_url.startswith("data:image/"):
        # 处理 base64 编码的图像
        image_data = image_url.split(",")[1]
        image_data = base64.b64decode(image_data)
        file_extension = image_url.split(";")[0].split("/")[-1]
        file_name = f"image.{file_extension}"
    else:
        # 处理图像 URL
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = response.content
        file_name = os.path.basename(image_url)

    files = {
        'file': (file_name, image_data, f'image/{file_name.split(".")[-1]}')
    }

    response = requests.post(
        "https://api.tripo3d.ai/v2/openapi/upload",
        headers=headers,
        files=files
    )
    response.raise_for_status()
    print("tripo3d", response.json())

    file_token = response.json()['data']['image_token']

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "type": "image_to_model",
        "file": {
            "type": "image",
            "file_token": file_token
        }
    }

    response = requests.post(
        "https://api.tripo3d.ai/v2/openapi/task",
        headers=headers,
        json=payload
    )
    response.raise_for_status()
    print("tripo3d", response.json())
    task_id = response.json()['data']['task_id']

    # 获取任务结果
    while True:
        url = f"https://api.tripo3d.ai/v2/openapi/task/{task_id}"

        headers = {
            "Authorization": f"Bearer {api_key}"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        task_result = response.json()['data']
        print("tripo3d", task_result)
        if task_result['status'] == 'success':
            break
        time.sleep(3)

    output_url = task_result['result']['model']['url']

    # 下载文件
    local_filename = f"downloads/tripo3d_{string_to_md5(output_url)}.glb"
    os.makedirs(os.path.dirname(local_filename), exist_ok=True)

    with requests.get(output_url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print("tripo3d", f"文件已下载到: {local_filename}")
    return local_filename

if __name__ == "__main__":
    config = load_config()
    imageUrl = "https://hao-wa-ai.obs.cn-south-1.myhuaweicloud.com/a04e2035e5eae852ce8b2e7d443eabde.png"

    apiKey = config['app']['tripo3d']['key']
    # 创建任务
    downloaded_file_path = tripo3d_process_image_to_3d(imageUrl, apiKey)
