#! python3
#try to input as single english word from a list as a password
#prints password if found. list of possibilites in dictionary.txt
#pip install PyPDF2
import os, PyPDF2, sys
import tkinter as tk
from tkinter import filedialog
    
root = tk.Tk()
root.withdraw() #to hide the empty window, only show Windows GUI
path = filedialog.askopenfilename()
dictFile = open('dictionary.txt','r')

pdfReader = PyPDF2.PdfFileReader(open(path, 'br'))

if pdfReader.isEncrypted == 0:
    print('no password')
    sys.exit()
for line in dictFile:
    line = line.replace("\n","")
    print(pdfReader.decrypt(line))
    if pdfReader.decrypt(line) == 1:
        print(line)
        break
    if pdfReader.decrypt(line.lower()) == 1:
        print(line.lower())
        break
print('done')
dictFile.close()
