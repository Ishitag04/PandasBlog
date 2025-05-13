import pandas as pd

data = {
    "Name" : ["Arun", "Varun", "Tarun"],
    "Age" : [28,34,22],
    "Salary" : [10000, 20000, 30000]
}

df = pd.DataFrame(data)

avg_sal = df["Salary"].mean()
print(avg_sal)
