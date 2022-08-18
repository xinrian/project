import openpyxl_studay

test = openpyxl.load_workbook('test.xlsx')
print(test.sheetnames)