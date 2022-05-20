import pandas as pd
import numpy as np
from openpyxl.workbook import workbook 

import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()


df = pd.read_csv("Names.csv",header=None)
df.columns=["First","Last","Adress",'City','State','Area Code','Income']

df.drop(columns="Adress", inplace=True) 

df = df.set_index('Area Code')



# print(df.loc[8074])
# this two print is the same
# print(df.iloc[0])

# print(df.loc[8074: , "First"])

# print(df.First.str.split(expand=True))

df.first = df.First.str.split(expand=True)

df = df.replace(np.nan , 'N/A', regex=True)

to_excel = df.to_excel("Modify.xlsx")

# to_excel = to_excel.save(to_excel, "Modify.xlsx")

dm = pd.read_excel("Modify.xlsx")

print(dm)

