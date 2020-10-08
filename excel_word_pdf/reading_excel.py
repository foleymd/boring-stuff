# reading excel spreadsheets

import os, openpyxl

os.chdir('/Users/mdf594/Desktop') # chdir to directory with excel document

# create workbook object
wb = openpyxl.load_workbook('video_filenames.xlsx') 
print('type: ' + str(type(wb))) #tells us the type of object

# get_sheet_names is deprecated and replaced by wb.sheetnames()
# print(workbook.get_sheet_names()) #list sheet names if you don't know them

#list sheet names if you don't know them
print('sheetnames: ' + str(wb.sheetnames)) 

# get_sheet_by_name is deprecated and replaced by wb[sheetname]
# sheet = workbook.get_sheet_by_name('video_filenames') #specifies the sheet in the workbook

# assign sheet object to variable; gets sheet object, not value
sheet = wb['video_filenames']
print('sheet: ' + str(sheet)) 

# assign cell object to variable; #gets cell object, not value
cell = sheet['A1'] 
print('cell: ' + str(cell))

# using member variable "value" to print value
print(cell.value) 

#specifying row and column instead

cell2 = sheet.cell(row=1, column=2) #row begins at 1, not at zero
print(cell2.value)

for i in range(1,8):
    print(i, sheet.cell(row=i, column=2).value)
