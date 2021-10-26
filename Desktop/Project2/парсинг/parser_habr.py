from bs4 import BeautifulSoup
import requests
import re

KEYWORDS = ['IPv6', 'API', 'web', 'python']


res = requests.get('https://habr.com/ru/all/')
res.raise_for_status()

soup = BeautifulSoup(res.text, features='lxml')


articles = soup.find_all('article')
for article in articles:
    time = article.find('time').attrs['title']
    title = article.find('h2').text
    href = article.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').find('a').attrs['href']
    link = 'https://habr.com' + href
    res_link = requests.get(link)
    soup_article = BeautifulSoup(res_link.text, features='lxml')
    link_article = soup_article.find('div', xmlns='http://www.w3.org/1999/xhtml').text.strip()
    list_link_article = link_article.split(' ')
    for word in KEYWORDS:
        if word in list_link_article:
            print(time, title, link)


