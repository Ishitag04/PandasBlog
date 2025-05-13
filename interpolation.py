"""
10
20
NaN -> 30(estimated value)
40
50

linear
polynomial
time


only with numbers
"""

import pandas as pd

# data = {
#     "Name" : ['Ram','Shayam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
#     "Age" : [28,None,22,30,29,40,25,32],
#     "Salary" : [50000,None,45000,52000,49000,70000,48000,58000],
#     "Performance Score" : [85, None, 78, 92, 88, 95, 80, 89]
# }

# df = pd.DataFrame(data)
# print(df)

# df["Age"].interpolate(method="linear", inplace=True)
# print(df)


data = {
    "Time" : [1,2,3,4,5],
    "Value": [10,None,30,None,50]
}

df = pd.DataFrame(data)
print(df)

df["Value"].interpolate(method="linear", inplace=True)
print(df)