import os
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import sql

title = "something..."
os.system(f"title {title}")

url = 'https://ru.investing.com/currencies/usd-rub'

green = [173, 255, 47]
red = [255, 0, 0]


def rgb(rgb_color, text='test'):
    color_text = f"\u001b[38;2;{rgb_color[0]};{rgb_color[1]};{rgb_color[2]}m{text}"
    return color_text


def save_file(name_file='file\\dollar_exchange_rate.txt', text="Пример текста"):
    date = str(datetime.now().date())
    time_now = str(datetime.now().time())[:8]
    with open(name_file, 'a+') as file:
        file.write(f'{date} {time_now} - {text} RUB\n')


def get_result(url):
    return requests.get(url).text


old_price = 0.0

while True:
    try:
        soup = BeautifulSoup(get_result(url), "lxml")
        price = soup.find_all(class_="text-2xl")[2]
        price_float = float(format(float(price.text.replace(",", ".")), '.2f'))
        if old_price < price_float:
            text_result_green = rgb(rgb_color=green, text=str(price_float))
            save_file(text=str(price_float))
            sql.insert_into_dollars(price_float, difference="↑")
            print(text_result_green)
        if old_price > price_float:
            text_result_red = rgb(rgb_color=red, text=str(price_float))
            save_file(text=str(price_float))
            sql.insert_into_dollars(price_float, difference="↓")
            print(text_result_red)
        old_price = price_float
        time.sleep(2)
    except:
        print(rgb(rgb_color=red, text=str('Ошибка')))
        time.sleep(2)
