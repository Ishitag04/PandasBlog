import pandas as pd

df_customers = pd.DataFrame({
    "CustomerId" : [1,2,3],
    "Name" : ["Ramesh" , "Suresh", "Kalpesh"]
})

df_orders = pd.DataFrame({
    'CustomerId' : [1,2,4],
    "Order Amount" : [250, 450, 500]
})

# df_merged = pd.merge(df_customers, df_orders, on="CustomerId", how="inner")
# print(df_merged)
#inner - intersection

# df_merged = pd.merge(df_customers, df_orders, on="CustomerId", how="outer")
# print(df_merged)
# outer - Union (not present will be filled by NaN)

# df_merged = pd.merge(df_customers, df_orders, on="CustomerId", how="left")
# print(df_merged)
#left - left will be there matching with the right dataframe

# df_merged = pd.merge(df_customers, df_orders, on="CustomerId", how="right")
# print(df_merged)
#right - right will be putted and matched with the left values

df_merged = pd.merge(df_customers, df_orders, left_index=True, right_index=True)
print(df_merged)
#combine both the df column wise - index join