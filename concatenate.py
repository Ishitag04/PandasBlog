import pandas as pd

df_region1 = pd.DataFrame({
    "CustomerId" : [1,2],
    "Name" : ["Ramesh" , "Suresh"]
})

df_region2 = pd.DataFrame({
    'CustomerId' : [3,4],
    "Name" : ["Raju", "Babu"]
})

df_concatenate = pd.concat([df_region1,df_region2], axis = 0, ignore_index = True)
print(df_concatenate)

df_concatenate = pd.concat([df_region1,df_region2], axis = 1, ignore_index = True)
print(df_concatenate)