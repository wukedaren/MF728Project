# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np 

data = pd.read_excel('Data forward.xlsx', index_col = 0)
data = data/100

forward = pd.DataFrame(index = data.index, 
                       columns = ['f1', 'f2', 'f3', 'f5', 'f7'])

forward['f1'] = data['H15T1Y Index']
forward['f2'] = (1 + data['H15T2Y Index']) ** 2 / (1 + data['H15T1Y Index']) - 1
forward['f3'] = (1 + data['H15T3Y Index']) ** 3 / (1 + data['H15T2Y Index']) ** 2  - 1
forward['f5'] = np.sqrt((1 + data['H15T5Y Index']) ** 5 / (1 + data['H15T3Y Index']) ** 3) - 1
forward['f7'] = np.sqrt((1 + data['H15T7Y Index']) ** 7 / (1 + data['H15T5Y Index']) ** 5) - 1

forward.to_csv('forward rates.csv')
