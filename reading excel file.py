import xlrd

workbook = xlrd.open_workbook('first_file.xlsx')

worksheet = workbook.sheet_by_index(0)

rows = worksheet.nrows

for row in range(rows):
    firstcol, secondcol = worksheet.row_values(row)

    print(firstcol,'   ',secondcol)