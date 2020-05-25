#! python3
#blankRowInserter
#takes two integers and inserts M rows starting with Nth row
import openpyxl

M = 2
N = 3
fileName = 'produceSales.xlsx'

wb = openpyxl.load_workbook('produceSales.xlsx')
ws = wb.active

for i in range(M):
    ws.insert_rows(N)
wb.save('insertedRows.xlsx')
wb.close()
