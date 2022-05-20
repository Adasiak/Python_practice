from importlib.machinery import FrozenImporter
from multiprocessing.context import _default_context
import pandas as pd
from openpyxl.workbook import Workbook



print("error check 0")
df_excel = pd.read_excel('Excel.xlsx') 
print("error check 1")
df_txt = pd.read_csv('Text.txt', delimiter='\t')
print("error check 2")

df_excel.columns = ["First","Last","Adress","City"]
print("error check 3")
df_excel.to_excel("modified0.xlsx")
print("error check 4")

print(df_excel)
print()
print(df_txt)
print()
print(df_excel[["Last","Adress"]])
print()
print(df_excel["First"][0:3])
print()
print(df_excel.iloc[1,1])
print()
wanted_values = df_excel[["First","Last",'City']]
wanted_values.to_excel("last_mod.xlsx", index=None)
print()
print(wanted_values)
print() 