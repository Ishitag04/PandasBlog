# head() tail()
#head(n)
#tail(n)

import pandas as pd
df = pd.read_json("sample_Data.json")

print("Display first 7 rows : ")
print(df.head(7))

print("Display last 7 rows : ")
print(df.tail(7))