#df.sort_values(by="ColumnName", True/False, inplace = True)
#True - Ascending

import pandas as pd

data = {
    "Name" : ["Arun", "Varun", "Tarun"],
    "Age" : [10,20,1],
    "Salary" : [10000,2000,30000]
}

df = pd.DataFrame(data)
print(df)

# df.sort_values(by="Name", ascending=False, inplace=True)
# print(df)


df.sort_values(by=["Salary", "Age"], ascending=False, inplace=True)
print(df)