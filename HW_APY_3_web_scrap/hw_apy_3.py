import time
from functions.funcs import find_habr_articles, find_habr_articles2

if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    num_pages = 3
    # Вариант 1
    print('\nПоиск по preview-информации статьи\n')
    start = time.perf_counter()

    res = find_habr_articles(KEYWORDS, num_pages)
    if res:
        print(*find_habr_articles(KEYWORDS, num_pages), sep='\n')
        print(f'Всего результатов {len(res)}')

    end = time.perf_counter()
    print(f'Время поиска: {round(end-start,1)} сек')

    # Вариант 2
    print('\nПоиск по всему тексту статьи\n')
    start = time.perf_counter()

    res2 = find_habr_articles2(KEYWORDS, num_pages)
    if res2:
        print(*find_habr_articles2(KEYWORDS, num_pages), sep='\n')
        print(f'Всего результатов {len(res2)}')
    end = time.perf_counter()

    print(f'Время поиска: {round(end-start,1)} сек')
