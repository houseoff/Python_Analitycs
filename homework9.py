import pandas as pd

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
df = pd.read_csv('california_housing_train.csv')
print(df[df['population'].between(0, 500)][['population', 'median_house_value']])

# Задача 42: Узнать какая максимальная households в зоне минимального значения population
print(df[df['population'] == df['population'].min()]['households'].max())