import os
import win32com.client as win32

xlApp = win32.Dispatch('Excel.Application')
xlApp.Visible = True

wb = xlApp.Workbooks.Add()
wb.SaveAs(os.path.join(os.getcwd(),'test.xlsx'))

ws_sheet1 = wb.Worksheets('sheet1')
ws_sheet1.name
ws_sheet1.name = 'data_test'

ws_sheet1.Cells(5, "B").Value = "samsung"