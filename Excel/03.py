import pandas as pd


df = pd.read_csv("Names.csv",header=None)

df.columns=["First","Last","Adress",'City','State','Area Code','Income']

# print(df.loc[(df['City']=='Riverside') & (df["First"] == 'John')])

df["Taxes %"] = df["Income"].apply(lambda x: .15 if 10_000 < x < 40_000 else .2 if 40_000 < x < 80_000 else .25)

# print(df)


df["Taxes Owned "] = df["Income"] * df["Taxes %"]

# print(df["Taxes Owned "])

To_Drop = ['Area Code','First','Adress']

df.drop(columns=To_Drop , inplace=True)

# print(df)

df["Test Column"] = False 

df.loc[df["Income"]< 60_000 , "Test Column"] = True
print(df)

print(df.groupby(["Test Column"]).mean().sort_values("Income"))

