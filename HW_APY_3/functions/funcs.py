import requests
import bs4
from fake_headers import Headers
import re


def get_preview_text(article):
    header_ = article.find(class_='tm-article-snippet__title-link').find('span').text
    overview_text = article.find(class_='tm-article-body tm-article-snippet__lead').text
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = ', '.join([hub.find('span').text for hub in hubs])
    return f'{header_}\n {overview_text}\n{hubs}'.lower(), header_


def get_info(article, key_words, base_url='https://habr.com'):

    preview_text, header = get_preview_text(article)
    pattern = fr"({'|'.join(key_words)})"

    if re.search(pattern, preview_text, flags=re.I):
        href = article.find(class_='tm-article-snippet__title-link').attrs['href']
        link = base_url + href
        datetime = article.find('time').attrs['title']
        return f'{datetime} - {header} - {link}'


def find_habr_articles(key_words: list, number_of_pages=1):

    """Ищет ключевые слова в preview статьи на habr.com  и выводит информацию в виде
    <дата> - <заголовок> - <ссылка>.
    Также можно указать количество страниц для поиска, начиная с самой свежей."""

    if number_of_pages == 0:
        return print('Ошибка! Количество страниц должно быть больше 0')

    base_url = 'https://habr.com'
    headers = Headers(os='win', headers=True).generate()
    result = []

    for page in range(1, number_of_pages + 1):
        url = base_url + '/ru/all/page' + str(page)
        text = requests.get(url, headers=headers).text
        soup = bs4.BeautifulSoup(text, features='html.parser')
        articles = soup.find_all(class_='tm-articles-list__item')
        for article in articles:
            temp_res = get_info(article, key_words)
            if temp_res:
                result.append(temp_res)
    return result


def find_habr_articles2(key_words: list, number_of_pages=1):

    """Ищет ключевые слова в самой статье на habr.com и выводит информацию в виде
    <дата> - <заголовок> - <ссылка>
    Также можно указать количество страниц для поиска, начиная с самой свежей"""

    if number_of_pages == 0:
        return print('Ошибка! Количество страниц должно быть больше 0')

    base_url = 'https://habr.com'
    headers = Headers(os='win', headers=True).generate()
    pattern = fr"\s({'|'.join(key_words)})\s"
    result = []

    for page in range(1, number_of_pages + 1):
        url = base_url + '/ru/all/page' + str(page)
        text = requests.get(url, headers=headers).text
        soup = bs4.BeautifulSoup(text, features='html.parser')
        articles = soup.find_all(class_='tm-articles-list__item')
        for article in articles:
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = base_url + href
            resp = requests.get(link, headers=headers).text
            soup_a = bs4.BeautifulSoup(resp, features='html.parser')
            temp_res = soup_a.find(class_='tm-article-presenter__content tm-article-presenter__content_narrow')
            if re.search(pattern, temp_res.text, flags=re.I):
                datetime = article.find('time').attrs['title']
                header = article.find(class_='tm-article-snippet__title-link').find('span').text
                result.append(f'{datetime} - {header} - {link}')
    return result
