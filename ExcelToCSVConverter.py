#! python3
# Excel-To-CSV Converter - takes excel files from folder and saves them as CSV files
#for multiple sheets creates one file per sheet "<filename>_<sheet name>.csv"

import os, openpyxl, csv, getPathFromUser
#get folder path
folderPath = r'C:\Users\Piotr Jaroszuk\Desktop\python_kurs\Automate Boring Stuff\AutomateWithPython\make those CSV'
#implement choose folder def
folderPath = getPathFromUser.askUserForPath()
outputFolder = os.path.join(folderPath , "CSV")
if not os.path.exists(outputFolder):
    os.mkdir(outputFolder)

os.chdir(folderPath)
for excelFile in os.listdir(folderPath):
    if '.xls' in excelFile:
        print('Converting ' + excelFile)
        try:
            wb = openpyxl.load_workbook(excelFile)
        except openpyxl.utils.exceptions.InvalidFileException:
            print("!!!!Can't support old file format " + excelFile + '\n')
            continue
        for sheetName in wb.sheetnames:
            csvFileName = excelFile.replace('.xlsx','') + '_' + sheetName
            csvFile = open(os.path.join(outputFolder,csvFileName + '.csv'),'w',newline='')
            csvWriter = csv.writer(csvFile, delimiter=';',lineterminator='\n')
            sheet = wb[sheetName]
            for rowNum in range(1, sheet.max_row + 1):
                rowData = []
                for colNum in range(1, sheet.max_column + 1):
                    rowData.append(sheet.cell(rowNum,colNum).value)
                csvWriter.writerow(rowData)
        csvFile.close()
print('Done...')
print('CSV files in ' + outputFolder)
            
