import json
import hashlib


# задание 1------------------------------------------

class Countries:

    def __init__(self):
        self.country_list = []

    def country_json(self):
        with open('countries.json', 'r') as file:
            for countries in json.load(file):
                for items, values in countries.items():
                    self.country_list.append(values['common'])
                    break

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.country_list):
            raise StopIteration
        country = self.country_list[self.index]
        self.index += 1
        return country

if __name__ == '__main__':
    link = 'https://en.wikipedia.org/wiki/'
    a = Countries()
    a.country_json()
    for i in a:
         with open('country_link.txt', 'a') as file:
               file.write(f'{i} - {link}{i}\n')

# задание 2----------------------------------------------

def generator_md5(file):
    with open(file, 'r') as file:
        string = (i.strip() for i in file)
        for i in string:
            md5_hash = hashlib.md5(i.encode())
            yield md5_hash.hexdigest()

g = generator_md5('country_link.txt')
for i in g:
    print(i)

