import pandas as pd

data = {
    "Name" : ["Arun", "Varun", "Tarun","Narun","Karun"],
    "Age" : [28,34,22,34,28],
    "Salary" : [50000, 60000, 45000, 52000, 480000]
}

df = pd.DataFrame(data)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)