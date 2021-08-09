import requests
import json
from pprint import pprint
import time

# Создание json файла
def vk_json(data):
    with open('photo_vk.json', 'w') as file:
        json.dump(data, file, indent=3, ensure_ascii=False)

# Загрузка полученных данных на яндекс диск + создание логов загрузки
def upload(dict):
    for likes, url in dict.items():
        req = requests.post(API_YA_URL + 'v1/disk/resources/upload',
              headers=headers, params={'path': f'VK/{likes}', 'url': url})
        if req.status_code == 202:
            text = f'Фотография {url} загружена'
            with open('log.txt', 'a') as log:
                log.write(text + '\n')
                print(f'Фотография {likes} загружена')
        else:
            text = f'Ошибка при загрузке фотографии {url}' + '\n'
            with open('log.txt', 'a') as log:
                log.write(text + '\n')
                print(f'Ошибка при загрузке фотографии {likes}')

# Функция помощник, для сортировки фотографий
def get_largest(size_dict):
    if size_dict['width'] >= size_dict['height']:
        return size_dict['width']
    else:
        return size_dict['height']

def main():
    r = requests.get(API_VK_URL + 'photos.get', params=PARAMS_VK)
    vk_json(r.json())
    count_list = []
    url_photo = []
    photo_vk = json.load(open('photo_vk.json'))['response']
    for item in photo_vk['items']:
        sizes = item['sizes']
        max_size = max(sizes, key=get_largest)
        url_photo.append(max_size['url'])
        time_ = str(time.strftime("%D", time.localtime(int(item['date'])))).split('/')
        time_to_name = '_'.join(time_)
        if str(item['likes']['count']) not in count_list:
            count_list.append(str(item['likes']['count']))
        else:
            time.strftime("%D", time.localtime(int(item['date'])))
            count_list.append(str(item['likes']['count']) + f'({time_to_name})')
    vk_dict = dict(zip(count_list, url_photo))
    upload(vk_dict)

if __name__ == '__main__':
    TOKEN_VK = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
    V = '5.131'
    API_YA_URL = 'https://cloud-api.yandex.net/'
    API_VK_URL = 'https://api.vk.com/method/'
    PARAMS_VK = {
        'owner_id': 552934290, #ID человека, с которого надо скачать фотографии
        'album_id': 'profile',
        'extended': True,
        'access_token': TOKEN_VK,
        'v': V
    }
    TOKEN_YA = ''  # В скобках должен быть ваш токен с яндекс диска
    headers = {
        'accept': 'application/json',
        'Authorization': f'OAuth {TOKEN_YA}'
    }
    main()
