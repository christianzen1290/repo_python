import pandas as pd

df = pd.read_csv('tips.csv')

columns_tips = df.columns
df_index = df.index
df_head = df.head()# get first 5 rows
# Index(['total_bill', 'tip', 'sex', 'smoker', 'day', 'time', 'size',
#        'price_per_person', 'Payer Name', 'CC Number', 'Payment ID'],
#       dtype='object')
print(df_index)
# RangeIndex(start=0, stop=244, step=1)w

df_head = df.head(10) # first 10 rows
df_tail = df.tail(10) # last 10 rows
# print(df) # info
# print(df.describe()) #info statistic
# print(df.describe().transpose()) #info statistic
# print(df.head(10)['total_bill']) 

my_cols = ['total_bill' , 'tip']
# print(df[my_cols])

df['tip_percentage'] = df['tip'] / df['total_bill'] * 100 # operasi untuk array
xx = df.set_index('Payment ID') # set to index
# xx = xx.reset_index() #reset index

set_row = df.iloc[[1,5,3]]
xy = xx.drop('Sun2959' , axis= 0)
# set_row = df.iloc[0:5]
x = 7
dfx = df[(df['total_bill'] > (x + 2)) & (df['tip_percentage']> 25)]
dfy = df[df['day'].isin(['Sat','Sun'])]
print(dfy)