import requests
from bs4 import BeautifulSoup

# URL веб-сайта для парсинга
url = "https://example.com"

# Получение данных с веб-сайта
response = requests.get(url)

# Проверка успешности запроса
if response.status_code == 200:
    print("Данные успешно получены!")

    # Парсинг HTML-кода с использованием BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Пример: извлечение заголовка страницы
    title = soup.title.string
    print(f"Заголовок страницы: {title}")

    # Пример: извлечение всех ссылок на странице
    links = soup.find_all('a')
    print("\nСсылки на странице:")
    for link in links:
        href = link.get('href')
        if href:
            print(href)
else:
    print(f"Ошибка при получении данных. Код статуса: {response.status_code}")
