import requests
import json


def send(request_json, configFilePath=None):
    dict_json = json.loads(request_json)
    url = dict_json["url"]
    if configFilePath is not None:
        configFile = open(configFilePath, 'r', encoding='utf-8')
        configData = configFile.read()
        configFile.close()
        config = yaml.load(configData, Loader=yaml.FullLoader)
    if 'params' in dict_json:
        response = requests.request(method=dict_json["http_method"], url=url, params=dict_json["params"])
    elif 'form_data' in dict_json:
        response = requests.request(method=dict_json["http_method"], url=url, data=dict_json["form_data"])
    elif 'json_data' in dict_json:
        response = requests.request(method=dict_json["http_method"], url=url, data=dict_json["json_data"])
    else:
        response = requests.request(method=dict_json["http_method"], url=url)
    return str(response.content,encoding='utf-8')