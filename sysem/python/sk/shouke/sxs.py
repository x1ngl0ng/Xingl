import random

import requests
import json
import time
em=random.Random()
# 请求的URL和头部信息
url = "https://api-staging.tripo3d.ai/v2/web/account/email/send"
payload = json.dumps({
    "email": f"xinglongggggs@vastai{em}.com",
    "type": "signup"
})
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'cookie': '_ga=GA1.1.web; ph_phc_avMshN0l7NiHSfgKBAjLke3il4P2sGBzOvj2LFGyTV9_posthog=%7B%22distinct_id%22%3A%22019444fe-ec56-7c8c-a00b-8380a251fd2d%22%2C%22%24sesid%22%3A%5B1736324363404%2C%22019444ff-132f-7467-98ba-8ef605973f45%22%2C1736324354863%5D%2C%22%24initial_person_info%22%3A%7B%22r%22%3A%22%24direct%22%2C%22u%22%3A%22https%3A%2F%2Fweb-testing.tripo3d.ai%2Fapp%2Fhome%22%7D%7D; _ga_65RE1SFD1W=GS1.1.1736321619.16.1.1736324364.0.0.0; _gcl_au=1.1.201194971.1736236282.941402313.1736324376.1736324375',
    'origin': 'https://web-testing.tripo3d.ai',
    'priority': 'u=1, i',
    'referer': 'https://web-testing.tripo3d.ai/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'use-language': 'zh',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'x-client-id': 'web'
}

call_count = 0
max_calls = 21
interval = 1

start_time = time.time()

while call_count < max_calls:
    response = requests.post(url, headers=headers, data=payload)

    print(f"Response {call_count + 1}: {response.json()}")

    call_count += 1

    if call_count < max_calls:
        time.sleep(interval)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"耗时: {elapsed_time / 60:.2f}s")
