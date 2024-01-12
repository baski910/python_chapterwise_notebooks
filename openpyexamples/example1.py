from openpyxl import Workbook
#from openpyxl.compat import range
#from openpyxl.utils import get_column_letter

wb = Workbook()

ws1 = wb.active

dest_filename = 'test.xlsx'
 
ws1.title = "range names"

for row in range(1, 40):
    ws1.append(range)

wb.save(filename = dest_filename)


        
