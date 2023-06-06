# Задача 44: Ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. 
# Сможете ли Вы это сделать без get_dummies?

import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
df = pd.DataFrame({'whoAmI':lst})

# Перевод в one hot вид без использования get_dummies
df.loc[df['whoAmI'] == 'robot', 'robot'] = 1
df.loc[df['whoAmI'] != 'robot', 'robot'] = 0
df.loc[df['whoAmI'] == 'human', 'human'] = 1
df.loc[df['whoAmI'] != 'human', 'human'] = 0
print(df.drop(columns='whoAmI'))