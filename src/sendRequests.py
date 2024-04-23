import requests
import json


def send(request_json):
    dict_json = json.loads(request_json)
    if 'params' in dict_json:
        response = requests.request(method=dict_json["http_method"], url=dict_json["url"], params=dict_json["params"])
    elif 'form_data' in dict_json:
        response = requests.request(method=dict_json["http_method"], url=dict_json["url"], data=dict_json["form_data"])
    elif 'json_data' in dict_json:
        response = requests.request(method=dict_json["http_method"], url=dict_json["url"], data=dict_json["json_data"])
    else:
        response = requests.request(method=dict_json["http_method"], url=dict_json["url"])
    return str(response.content,encoding='utf-8')