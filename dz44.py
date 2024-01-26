# Задача 44:
# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?

import pandas as f 
import numpy as np 
import random
 
res_ls = ['robot'] * 10
res_ls += ['human'] * 10
random.shuffle(res_ls)
data = f.DataFrame({'whoAmI': res_ls})
print(data)
 
print('')

data['tmp'] = 1
data.set_index([data.index, 'whoAmI'], inplace=True)
data = data.unstack(level=-1, fill_value = 0).astype(int)
data.columns = data.columns.droplevel()
data.columns.name = None
print(data)