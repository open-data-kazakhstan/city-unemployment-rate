import openpyxl
import csv
from datapackage import Package

def data_package():
    package = Package()
    package.infer(r'data/unemploymentRate-final.csv')
    package.commit()
    package.save(r"datapackage.json")

workbook = openpyxl.load_workbook('archive/unemploymentRate.xlsx')
worksheet = workbook.active
desired_columns = [1, 111]
new_values = ["region","rate","year"]
with open('archive/unemploymentRate.csv', 'w', newline='', encoding='utf-8') as csvfile:
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

def rename_first_column_cells(input_file, output_file, new_names):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        # Modify the first cell of each row with new names
        for new_name, row in zip(new_names, reader):
            if row:  # Check if row is not empty
                row[0] = new_name
                writer.writerow(row)
input_file = 'archive/unemploymentRate.csv'
output_file = 'data/unemploymentRate-final.csv'
new_names = ["Region", "Abai Region", "Akmola Region","Aktobe Region","Almaty Region","Atyrau Region","West Kazakhstan Region","Jambyl Region","Jetisu Region","Karaganda Region","Kostanay Region","Kyzylorda Region","Mangystau Region","Pavlodar Region","North Kazakhstan Region","Turkistan Region","Ulytau Region","East Kazakhstan Region","Astana city","Almaty city","Shymkent city"]
rename_first_column_cells(input_file, output_file, new_names)


data_package()