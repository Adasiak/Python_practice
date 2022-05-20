import openpyxl
from openpyxl.chart import PieChart, Reference, Series, PieChart3D
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()

wb =  openpyxl.Workbook()
ws = wb.active

data = [
    ["Flavor", 'Sold'],
    ["vanila",1500],
    ['Chockolate',1990], 
    ['Strawbery',888],
    ['PeunatButter', 999]
]

for row in data:
    ws.append(row)

chart = PieChart()

labels = Reference(ws, min_col=1, min_row=1, max_row=5)
data = Reference(ws, min_col=2, min_row =1, max_row = 5)

chart.add_data(data, titles_from_data=True)

chart.set_categories(labels)
chart.title =  "Ice Cream by Flavour"

ws.add_chart(chart, "C1")
wb.save("Pie.xlsx")

print("DONE")