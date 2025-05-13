import pandas as pd

# df = pd.read_json("sample_Data.json")
# print("Displaying the info of the data set : ")
# print(df.info())

data  = {
    "Name" : ['Ram','Shyam', 'Ghanshyam'],
    "Age" : [10, 20, 30],
    "City" : ['Nagpur','Mumbai','Delhi']
}

df = pd.DataFrame(data)
print(df.info())