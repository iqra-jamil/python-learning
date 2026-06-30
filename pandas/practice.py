import pandas as pd

a = [1, 7, 2]

res= pd.Series(a)
print(res)

a = [1, 7, 2]

res= pd.Series(a[2])
print(res)

a = [1, 7, 2]

res= pd.Series(a ,index=["i","j","k"])
print(res)

calories = {"day1": 420, "day2": 380, "day3": 390}

print(pd.Series(calories))
print(calories["day1"])

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

# #load dict/data into a DataFrame object:
res=pd.DataFrame(data)
print(res)

#loading CSV file
df=pd.read_csv("data.csv")
print(df.to_string())
print(pd.options.display.max_rows)
df=pd.read_json("data.json")
print(df.to_string())
print(df.head(10))
print(df.tail())