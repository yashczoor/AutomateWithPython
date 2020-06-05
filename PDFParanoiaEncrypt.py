#! python3
#encrypt all pdf in folder and subfolders
#PyPDF2, shutil

import os, PyPDF2, shutil, sys
import tkinter as tk
from tkinter import filedialog

def testEncryption(newPath, password):
    try:
        pdfReader = PyPDF2.PdfFileReader(open(newPath, 'rb'))
        print(pdfReader.isEncrypted)
        pdfReader.getPage(0)
    except:
        if pdfReader.decrypt(password) == 1:
            return True
            print('Encrypt ok')
        print('Encrpyt fail')
        return False

def getFolderPathFromUser():
    root = tk.Tk()
    root.withdraw() #to hide the empty window, only show Windows GUI
    path = filedialog.askdirectory()
    return path

password = ' '.join(sys.argv[1:])
print('encrypting with password ' + password)
#folderPath = os.path.join(os.getcwd(),'encrypt those')
folderPath = getFolderPathFromUser()
print(folderPath)
#pdfWriter = PyPDF2.PdfFileWriter()
for foldername, subfolders, filenames in os.walk(folderPath):
    for filename in filenames:
        #get file full path
        if filename.endswith('.pdf'):
            pdfPath = os.path.join(foldername, filename)
            print(pdfPath)
            pdfFile = open(pdfPath,'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()
            pdfWriter.appendPagesFromReader(pdfReader)
            pdfFile.close()
            pdfWriter.encrypt(password)
            resultPdf = open(pdfPath.replace('.pdf','_encrypted.pdf'), 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            newPath = pdfPath.replace('.pdf','_encrypted.pdf')
            if testEncryption(newPath, password):
                print('removing ' + pdfPath)
                os.remove(pdfPath)
            else:
                print('Fail')
            #shutil.move(pdfPath, newPath)
            
print('Done encrypting pdfs in ' + folderPath)
        #save with sufix
        #delete original
