import requests
import json
from pprint import pprint
import time

# Создаем класс для скачивания с контакта и закачивания на яндекс диск
class Yanupload():
    API_YA_URL = 'https://cloud-api.yandex.net/'
    API_VK_URL = 'https://api.vk.com/method/'

    def __init__(self, token_vk:str, token_ya:str):
        self.params = {
            'access_token': token_vk,
            'v': '5.131'
        }
        self.headers = {
            'accept': 'application/json',
            'Authorization': f'OAuth {token_ya}'
        }

# Создаем json файл для записи данных с метода API VK
    def vk_json(self, data):
        with open('photo_vk.json', 'w') as file:
            json.dump(data, file, indent=3, ensure_ascii=False)

# Загрузка полученных данных на яндекс диск + создание логов загрузки
    def upload(self, dict):
        for likes, url in dict.items():
            req = requests.post(self.API_YA_URL + 'v1/disk/resources/upload',
                  headers=self.headers, params={'path': f'VK/{likes}.jpg', 'url': url})
            if req.status_code == 202:
                text = f'Фотография {likes}.jpg загружена'
                with open('log.txt', 'a') as log:
                    log.write(text + '\n')
                    print(f'Фотография {likes}.jpg загружена')
            else:
                text = f'Ошибка при загрузке фотографии {likes}.jpg' + '\n'
                with open('log.txt', 'a') as log:
                    log.write(text + '\n')
                    print(f'Ошибка при загрузке фотографии {likes}.jpg')

# Метод помощник, для сортировки фотографий
    def get_largest(self, size_dict):
        if size_dict['width'] >= size_dict['height']:
            return size_dict['width']
        else:
            return size_dict['height']

# Метод для скачивания фотографий с профиля в ВК, нужно ввести id пользователя и id альбома, по умолчанию альбом profile
    def vk_download_profile(self, owner_id, album_id = 'profile'):
        params_vk = {
            'owner_id': owner_id,
            'album_id': album_id,
            'extended': True,
        }
        r = requests.get(self.API_VK_URL + 'photos.get', params=params_vk|self.params)
        self.vk_json(r.json())
        count_list = []
        url_photo = []
        size_json = []
        dict_info = {}
        photo_vk = json.load(open('photo_vk.json'))['response']
        for item in photo_vk['items']:
            sizes = item['sizes']
            max_size = max(sizes, key=self.get_largest)
            url_photo.append(max_size['url'])
            time_ = str(time.strftime("%D", time.localtime(int(item['date'])))).split('/')
            time_to_name = '_'.join(time_)
            if str(item['likes']['count']) not in count_list:
                count_list.append(str(item['likes']['count']))
                dict_info['file_name'] = str(item['likes']['count']) + '.jpg'
                dict_info['size'] = str(max_size['type'])
                size_json.append(dict_info)
            else:
                time.strftime("%D", time.localtime(int(item['date'])))
                count_list.append(str(item['likes']['count']) + f'({time_to_name})')
                dict_info['file_name'] = str(item['likes']['count']) + f'({time_to_name})' + '.jpg'
                dict_info['size'] = str(max_size['type'])
                size_json.append(dict_info)
        with open('info.json', 'w') as f:
            json.dump(size_json, f, indent=1)
        vk_dict = dict(zip(count_list, url_photo))
        self.upload(vk_dict)


#достаем токен вк из файла:
with open('vk_token.txt', 'r', encoding='utf-8') as file_reader:
    token_vk = file_reader.read().strip()
with open('yandex_token.txt', 'r', encoding='utf-8') as file_reader:
    token_ya = file_reader.read().strip()
abc = Yanupload(token_vk, token_ya)
# Вводим id пользователя и id альбома, если не введете id альбома, по умолчанию загрузятся фотографии с профиля.
abc.vk_download_profile('8168323', '164606769')

