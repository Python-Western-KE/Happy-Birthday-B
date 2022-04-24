# Python program to read an excel file

# import openpyxl module

import openpyxl
from openpyxl import Workbook

# Create new new blank workbook
workbook = Workbook()
# data
sheet = workbook.active
c1 = sheet.cell(row=1, column=1)

# write values
c1.value = "Hello"
# Save changes
workbook.save(filename="contacts.xlsx")
