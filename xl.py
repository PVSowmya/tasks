import xlrd

book = xlrd.open_workbook("data.xlsx")
l=list()
sheet = book.sheet_by_index(0)
print(sheet.cell_value(0, 0))
for i in range(1,6):
    print(sheet.row_values(i))