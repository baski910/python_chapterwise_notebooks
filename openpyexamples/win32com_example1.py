import win32com.client as win32

# Create an Excel application instance
excel = win32.gencache.EnsureDispatch('Excel.Application')

# Make Excel visible (optional)
excel.Visible = True

# Add a new workbook
workbook = excel.Workbooks.Add()

# Get the active worksheet
worksheet = workbook.ActiveSheet

# Write data to cells
worksheet.Cells(1, 1).Value = "Hello"
worksheet.Cells(2, 1).Value = "World"

# Save the workbook
workbook.SaveAs("example.xlsx")

# Close the workbook
workbook.Close()

# Quit Excel
excel.Application.Quit()
