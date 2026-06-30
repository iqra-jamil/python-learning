import pandas as pd
df=pd.read_csv("pandas/cleaning_data/my_data.csv")
print(df)

##dealing with rows containing empty cells
##drop/remove them 
## will return new dataFrame
new_df=df.dropna()
print(new_df)
# apply dropna on orignal df
df.dropna(inplace=True)
print(df.to_string())

## replace with a value
df.fillna("134",inplace=True) ##will not wrk on pandas-3.0
print(df.to_string())
df.fillna({"Calories":134},inplace=True)
print(df.to_string())


## or replace values with mean,mediun, mode
x=df["Calories"].mean()
df.fillna({"Calories":x},inplace=True)
# print(df)

# pd.to_datetime({"Date" :"2026/5/2" },inplace=True)
df.fillna({"Date" :"2026-5-2" },inplace=True)
# print(df)
df["Date"]=pd.to_datetime(df["Date"],format="mixed")
# print(df.to_string)

# Fixing Wrong Data
df.loc[7,"Duration"]=45
print(df)

# loop for large data
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.drop(i, inplace = True)

print(df)
# # drop a row based on condition
for i in df.index:
    if df.loc[i,"Duration"]>120:
        df.loc[i, "Duration"]=120

print(df)

# discover & remove duplicates 
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df.to_string())
print(df.corr())
