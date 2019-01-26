from xlsxwriter import Workbook

workbook = Workbook('first_file.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write(0, 0, 10)
worksheet.write(1, 0, 20)
worksheet.write(0, 1, 30)
worksheet.write(1, 1, 40)

workbook.close()