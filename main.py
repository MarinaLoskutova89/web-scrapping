import requests
from bs4 import BeautifulSoup
from bs4 import NavigableString
from pprint import pprint

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

HOST = 'https://habr.com/ru/all/'

URL = 'https://habr.com'

response = requests.get(HOST)
response.raise_for_status()

soup = BeautifulSoup(response.text, features='html.parser')
article = soup.find('article')
articles = soup.find_all('article')

articles_list =[]

for article in articles:
    text = article.find('div', class_='article-formatted-body')

    text_list = [texts.text.strip() for texts in text if not isinstance(texts, NavigableString)]

    for string in text_list:
        string = string.lower()
        if any(i in string for i in KEYWORDS):
            publish_date = article.find('time').text
            title = article.find('h2')
            link = title.find('a').attrs.get('href')
            article_set = {'publish_date': publish_date,
                                  'title': title.text,
                                  'link': URL + link
                            }
            if article_set not in articles_list:
                articles_list.append(article_set)
pprint(articles_list)

