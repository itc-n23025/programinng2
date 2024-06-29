import openpyxl
import os


new_wb = openpyxl.Workbook()
new_sheet = new_wb.active

n = 0
for filename in sorted(os.listdir('.')):

    if not filename.lower().endswith('.txt'):
        continue

    n += 1
    text_file = open(filename, 'r', encoding='utf-8')

    for m,line in enumerate(text_file):
        new_sheet.cell(column=n, row=m + 1).value = line.strip()
    text_file.close()


new_wb.save('texts.xlsx')
