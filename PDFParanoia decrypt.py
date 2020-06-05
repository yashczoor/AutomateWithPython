#! python3
#decrypt all pdf in folder and subfolders
#pip install PyPDF2, shutil

import os, PyPDF2, shutil, sys
import tkinter as tk
from tkinter import filedialog

def getFolderPathFromUser():
    root = tk.Tk()
    root.withdraw() #to hide the empty window, only show Windows GUI
    path = filedialog.askdirectory()
    return path

def rewritePdfWithoutPassword(pdfReader, pdfPath):
    pdfWriter = PyPDF2.PdfFileWriter()
    pdfWriter.appendPagesFromReader(pdfReader)
    pdfWriter.write(open(pdfPath.replace('_encrypted',''), 'wb'))

password = ' '.join(sys.argv[1:])
#folderPath = os.path.join(os.getcwd(),'encrypt those')
folderPath = getFolderPathFromUser()
print('working with: ' + folderPath)
for foldername, subfolders, filenames in os.walk(folderPath):
    for filename in filenames:
        #get file full path
        if filename.endswith('.pdf'):
            pdfPath = os.path.join(foldername, filename)
            with open(pdfPath, mode='rb') as f:
                pdfReader = PyPDF2.PdfFileReader(f)
                if pdfReader.isEncrypted:
                    print(pdfPath + str(pdfReader.isEncrypted))
                    pdfReader.decrypt(password)
                    rewritePdfWithoutPassword(pdfReader, pdfPath)
                    f.close()
                    os.remove(pdfPath)  
                    #removeOldFile
                    
                
                

