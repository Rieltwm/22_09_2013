#Задача 42: Узнать какая максимальная households в зоне минимального значения population

import pandas as pd
df = pd.read_csv('california_housing_train.csv')
df
df[df['population'] == df['population'].min()]['households'].max()