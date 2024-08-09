import pandas as pd
import numpy as np

data = pd.read_csv('sq_data.csv')
grey_sq = data[data['Primary Fur Color'] == 'Gray']
grey_sq_len = len(data[data['Primary Fur Color'] == 'Gray'])
cinn_sq_len = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_sq_len = len(data[data['Primary Fur Color'] == 'Black'])
print(black_sq_len)
print(cinn_sq_len)