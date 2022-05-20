import pandas as pd

df = pd.read_excel("modified0.xlsx")

df.columns = ["First","Last","Adress","City",'Post Code','Number of Flat']
df["Number of Flat"][2]=2.5
# print(df)
df.to_excel("MM.xlsx",index=None)

print(df.loc[df["Adress"]=='Lotnicza'])

print()
dm =  pd.read_excel("MM.xlsx")
dm.columns = ["First","Last","Adress","City",'Post Code','Number of Flat']
print()
print(dm)
print(dm['Number of Flat'][2])

