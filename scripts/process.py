import openpyxl
import csv
from datapackage import Package

def data_package():
    package = Package()
    package.infer(r'data/unemploymentRate.csv')
    package.commit()
    package.save(r"datapackage.json")

workbook = openpyxl.load_workbook('archive/unemploymentRate.xlsx')
worksheet = workbook.active
desired_columns = [1, 111]
new_values = ["region","rate","year"]
with open('data/unemploymentRate.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(new_values)
    for row in worksheet.iter_rows(min_row=7, max_row=27):
        if row[0].row != 19:
            values = [cell.value for cell in row if cell.column in desired_columns]
            if row[0].row > 6:
                values.append("2022")
            if row[0].row in [14, 22, 27]:
                values[0] = values[0].rstrip(")3 ")
            writer.writerow(values)

data_package()