import pandas as pd
import numpy as np

myindex = ['USA','Canada','Mexico']
mydata = [1776,1896,1261]
myseries = pd.Series(data=mydata,index=myindex)

ages = {'Sam' : 5 , 'Test 1' : 3 ,'Best' : 'x123'}

salesq1 = {'Indo' : 1 , 'Brazil' : 4, 'Afrika Selatan' : 5 , 'Singapore' :2 , 'Japan' : 5}
salesq2 = {'Indo' : 4 , 'Brazil' : 3, 'Afrika Selatan' : 2.5 , 'Singapore' :9}

sales_q1 = pd.Series(salesq1)
sales_q2 = pd.Series(salesq2)
print(np.array([1,2]) * 3)
print(sales_q1 + sales_q2)