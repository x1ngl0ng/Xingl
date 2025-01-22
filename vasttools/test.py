import requests

api_key = "tcli_0ec5d315adef4097b20cf83899139422"
url = "https://api.tripo3d.ai/v2/openapi/upload"

headers = {
    "Authorization": f"Bearer tcli_0ec5d315adef4097b20cf83899139422"
}

# file_path = r'file:///C:/Users/xl/Pictures/inages/41823.jpg'
file_path = r'C:/Users/xl/Pictures/inages/41823.jpg'
with open(file_path, 'rb') as f:
    files = {'file': (file_path, f, 'image/jpeg')}
    response = requests.post(url, headers=headers, files=files)

print(response.json())