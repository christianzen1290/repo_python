import pandas as pd
import numpy as np

data_test = np.random.seed(101)
mydata1 = np.random.randint(0,151,(4,3))
# print(mydata1)

my_index = ['A1','B2','C3','D4' , ]
my_columns = ['Jan', 'Feb' , 'Mar' ]
df = pd.DataFrame(data=mydata1 , index = my_index)
#      0    1   2
# 0   95   11  81
# 1   70   63  87
# 2   75  137  40
# 3  132   63  60

df = pd.DataFrame(data=mydata1 , index = my_index)
#       0    1   2
# A1   95   11  81
# B2   70   63  87
# C3   75  137  40
# D4  132   63  60

df = pd.DataFrame(data=mydata1 , index = my_index , columns = my_columns)
#     Jan  Feb  Mar
# A1   95   11   81
# B2   70   63   87
# C3   75  137   40
# D4  132   63   60

import os

# Mendapatkan direktori kerja saat ini
current_directory = os.getcwd()
print("Current working directory:", current_directory)
