from pprint import pprint
import requests
API_BASE_URL = 'https://superheroapi.com/api/2619421814940190'
superhero = ['Hulk', 'Captain America', 'Thanos']
dict_superhero = {}
search = '/search'
for name_heroes in superhero:
    r = requests.get(API_BASE_URL + search + f'/{name_heroes}')
    dict_superhero[name_heroes] = r.json()['results'][0]['powerstats']['intelligence']

for key, value in sorted(dict_superhero.items(), reverse=True):
    print(f'Самый умный супергерой это {key}, его интелект равен {value}')
    break
