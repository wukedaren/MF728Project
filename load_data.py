'''
MF728 Project : Bond Risk Premia
Spring 2021
Code : Load data
'''


import pandas as pd
import numpy as np 

prices = pd.read_excel('Bond prices.xlsx', index_col = 0)
prices.columns = ['1Y Bond', '2Y Bond', '3Y Bond', '5Y Bond', '7Y Bond']
log_prices = np.log(prices)
yields = prices.copy()
for i in range(len(prices.columns)):
    mat = int(prices.columns[i][0])
    yields[yields.columns[i]] = - log_prices[prices.columns[i]] / mat

forward = yields.copy()
forward['2Y Bond'] = log_prices['1Y Bond'] - log_prices['2Y Bond']
forward['3Y Bond'] = log_prices['2Y Bond'] - log_prices['3Y Bond']
forward['5Y Bond'] = (log_prices['3Y Bond'] - log_prices['5Y Bond']) / 2
forward['7Y Bond'] = (log_prices['5Y Bond'] - log_prices['7Y Bond']) / 2

yields.columns = ['r1', 'r2', 'r3', 'r5', 'r7']
forward.columns = ['f1', 'f2', 'f3', 'f5', 'f7']
log_prices.to_csv('Log_prices.csv')
yields.to_csv('Bond yields.csv')
forward.to_csv('forward rates.csv')