import requests
from yandex_token import token
import json
from pprint import pprint
import re


API_YA_URL = 'https://cloud-api.yandex.net/'
headers = {
            'accept': 'application/json',
            'Authorization': f'OAuth {token}',
            'path': 'disk:/sample'
        }

def check_connect():
        res = requests.get(API_YA_URL + f'v1/disk', headers=headers)
        return res.status_code

def create_path(path_name):
        res = requests.put(API_YA_URL + f'v1/disk/resources?path={path_name}', headers=headers)
        return res.status_code

def check_path(path_name):
    res = requests.get(API_YA_URL + f'v1/disk/resources?path={path_name}', headers=headers)
    return res.status_code


