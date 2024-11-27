import sys
import numpy as np

import pandas as pd
import time
from pathlib import Path
from functools import reduce
#import kagglehub

# Чтение входных данных из стандартного потока ввода
for line in sys.stdin:

    data = line.strip().split(',') # Разделение строки на столбцы
    if len(data) == 16:
        price = data[9] # Извлечение цены в качестве значения
        print("{0}t{1}".format("price", price)) # Вывод ключ-значение для передачи в reducer


# Инициализация переменных
total_count = 0
total_price = 0
total_price_squared = 0

for line in sys.stdin: # Чтение и обработка данных от mapper
    key, value = line.strip().split('t')
    if key == "price":
        price = float(value)
        total_count += 1
        total_price += price
        total_price_squared += price ** 2

dataset = pd.read_csv('/kaggle/input/ab-nyc-2019csv/AB_NYC_2019.csv')
dataset_path = Path('AB_NYC_2019.csv')
if not dataset_path.is_file():
    opendatasets.download('https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data/data')

# Вычисление среднего значения и дисперсии

mean_price = total_price / total_count

var_price = (total_price_squared / total_count) - (mean_price ** 2)

# Вывод результатов

print("Средняя цена: {:.2f}".format(mean_price))

print("Дисперсия: {:.2f}".format(var_price))
