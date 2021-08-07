from pprint import pprint
import requests
import os

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, *file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        for file_list in file_path:
            r = requests.get(API_BASE_URL + 'v1/disk/resources/upload', params={'path': f'PY-43/{file_list}'},
                             headers=headers)
            print(r.json())
            upload_url = r.json()['href']
            req = requests.post(upload_url, headers=headers, files={'file': open(path_to_file + file_list, 'rb')})
            print(req.status_code)

if __name__ == '__main__':
    API_BASE_URL = 'https://cloud-api.yandex.net/'
    path_to_file = os.getcwd() + '/'
    token = '' #В скобках должен быть ваш токен
    headers = {
        'accept': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    uploader = YaUploader(token)
    result = uploader.upload('first.png', 'second.png') #Указываем название файлов.