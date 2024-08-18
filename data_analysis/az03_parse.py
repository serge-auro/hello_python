import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL страницы с диванами
url = 'https://divan.ru/category/divany-i-kresla'

# Выполняем GET-запрос на сайт
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим все элементы с диванами (нужно обновить селекторы на основе актуального HTML сайта)
    divans = soup.select('div._Ud0k')  # Обновите селектор в соответствии с текущим HTML-кодом

    # Список для хранения данных
    data = []

    for divan in divans:
        name = divan.select_one('div.lsooF span').get_text(strip=True)
        price_text = divan.select_one('div.pY3d2 span').get_text(strip=True)
        price = int(price_text.replace('руб.', '').replace(' ', ''))
        url = divan.select_one('a')['href']

        # Добавляем данные в список
        data.append({
            'name': name,
            'price': price,
            'url': f'https://divan.ru{url}'  # формируем полный URL
        })

    # Преобразуем список данных в DataFrame
    df = pd.DataFrame(data)

    # Сохраняем DataFrame в CSV файл
    df.to_csv('sofa_prices.csv', index=False)

    # Вычисляем среднюю цену
    mean_price = df['price'].mean()
    print(f"Средняя цена на диваны: {mean_price} ₽")

    # Построение гистограммы цен
    plt.figure(figsize=(10, 6))
    plt.hist(df['price'], bins=30, color='blue', edgecolor='black')
    plt.title('Histogram of Sofa Prices')
    plt.xlabel('Price (₽)')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
