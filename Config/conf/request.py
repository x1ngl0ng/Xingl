#封装接口请求
import requests
from urllib.parse import urlencode
from Config.Base.GetToken import with_token
import json
import logging
from datetime import datetime
current_time = datetime.now()



logging.basicConfig(level=logging.DEBUG, handlers=[logging.StreamHandler()])


class SendRequests:
    @staticmethod
    def req(method, url, params=None, data=None,put_data=None, headers=None,files=None):
        logging.info(f"Run Current Time:{current_time},Method: {method}\nParams: {params}")

        if method.upper() == 'GET' and params is not None:#todo：加日志
            if isinstance(params, (dict, list, tuple)):
                try:
                    query_string = urlencode(params)
                    url = f"{url}?{query_string}"

                    logging.info(f"Get Request URL This: {url}")

                except TypeError as e:
                    logging.error(f"GET UnexPected param ERRO:{e}")
                    raise
            else:
                raise TypeError(f"GET param参数类型错误: params必须是字典或序列, 但传递的是 {type(params)}")


        elif method.upper() in ['POST', 'PUT'] and data is not None:
            if isinstance(data, str):
                pass
            elif files:
                pass
            elif isinstance(data, dict):
                data = json.dumps(data)
                logging.warning(f"THIS DicTionaries SWICH JSON……")
            elif isinstance(data, (list, tuple)):
                data = urlencode(data, doseq=True)
                logging.warning(f"THIS{type(data)}SWICH JSON ……")
            else:
                raise TypeError(
                    f"{method.upper()} data参数类型错误: data必须是字符串、字典、列表或元组, 但传递的是 {type(data)}")

        try:
            if files:
                res = requests.request(
                    method=method,
                    url=url,
                    data=data if method.upper() == ['POST','PUT'] else None,
                    params=None,
                    files=files,
                    headers=headers
                )
            else:
                logging.info(f"URsssL: {url}")
                res = requests.request(
                    method=method,
                    url=url,
                    params=params if method.upper() == 'GET' else None,
                    data=data if method.upper() in ['POST','PUT'] else None,
                    headers=headers
                )
            logging.info(f"Response status code: {res.status_code}")
            # print(f"response status code: {res.status_code}")
            # print(f"response body: {res.text}")
            res.raise_for_status()  # 如果发生HTTP错误则引发异常
            logging.info(f"Response body: {res.text}")
            print("_"*100,"complete","__"*100)
            return res.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"status code: {e}")
            raise


    @staticmethod
    @with_token
    def special(url, put_data=None, headers=None):
        if isinstance(put_data, str):
            data = put_data
        elif isinstance(put_data, dict):
            logging.warning(f"THIS dictionaries SWICH JSON ……")
            data = json.dumps(put_data)
        elif isinstance(put_data, (list, tuple)):
            logging.warning(f"THIS{type(put_data)}SWICH JSON ……")
            data = urlencode(put_data, doseq=True)

        else:
            raise TypeError(
                f"data参数类型错误: data必须是字符串、字典、列表或元组, 但传递的是 {type(put_data)}"
            )

        logging.info(type(data))
        response = requests.request('PUT', url, headers=headers, data=data)
        return response






        # 发送 HTTP 请求，#todo：post返回的是json

            # 在这里可以根据具体情况进行进一步处理，比如记录日志或采取其他措施



        #todo：post向服务器提交资源，需要反序列化，MismatchedInputException异常

        # return res.json()  # 返回响应的 json,这是字典

    # try:
    #     response_json = json.loads(res.text)
    #     print(type(response_json))
    #     print(response_json)
    #     # 在这里可以使用反序列化后的 response_json 对象进行后续处理
    # except json.JSONDecodeError as e:
    #     print(f"JSON 反序列化错误: {e}")

    @staticmethod
    @with_token
    def get(url, params=None, headers=None):
        logging.info(f"Headers: {headers}")
        return SendRequests.req('get', url, params=params, headers=headers)

    @staticmethod
    @with_token
    def post(url, data=None, headers=None,files=None):
        logging.info(f"Headers: {headers}")
        return SendRequests.req('post', url, data=data, headers=headers,files=files)

    @staticmethod
    @with_token
    def put(url, put_data=None, headers=None):
        logging.info(f"Headers: {headers}")
        return SendRequests.special('put',url,put_data=put_data, headers=headers)

    @staticmethod
    @with_token
    def delete(url, data=None, headers=None):
        logging.info(f"Headers: {headers}")

        return SendRequests.req('DELETE', url, data=data, headers=headers)


    #todo:什么时候传data什么时候传json，根据header
    @staticmethod
    def run_main(url, headers=None,put_data=None, **kwargs):
        if 'params' in kwargs:
            return SendRequests.get(url, params=kwargs.get('params'), headers=headers)
        elif 'data' in kwargs:
            return SendRequests.post(url, data=kwargs.get('data'), headers=headers)
        elif 'files' in kwargs:
            return SendRequests.post(url, data=kwargs.get('data'), headers=headers, files=kwargs.get('files'))
        elif 'put_data' in kwargs:
            return SendRequests.put(url, put_data=kwargs.get('put_data'), headers=headers)

        # elif 'data' in kwargs:
        #     return SendRequests.post(url, data=kwargs.get('data'), headers=headers)
        # elif 'files' in kwargs:
        #     return SendRequests.post(url, data=kwargs.get('data'), headers=headers, files=kwargs.get('files'))
        else:
            raise ValueError("关键字keyword Error")


# SendRequests.get = with_token(SendRequests.get)
# SendRequests.post = with_token(SendRequests.post)
# SendRequests.put = with_token(SendRequests.put)
# SendRequests.delete = with_token(SendRequests.delete)
#     def __init__(self):
#         pass
#     @staticmethod
#     def get(url, params=None, headers=None):
#         if params is not None:
#             query_string = urlencode(params)

#
#         return res
#     @staticmethod

#         if headers is None:
#             res=requests.post(url=url,data=data)
#         else:
#             res=requests.post(url=url,data=data,headers=headers)
#         return res
#
#     def put(self):
#         pass
#     def delete(self):




if __name__ == '__main__':
    send=SendRequests()
    url=''
    data={}
    method='post'
    header=None
    res=send.run_main(url,data)
    print(res)
    res.json()
    res.loads()#字典转
