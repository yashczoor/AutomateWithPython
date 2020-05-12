#! python3
'''from tkinter import Tk
from tkinter.filedialog import askdirectory'''
import tkinter as tk
from tkinter import filedialog

import sys
import re
import os

root = tk.Tk()
root.withdraw() #to hide the empty window, only show Windows GUI
path = filedialog.askdirectory()
print('Give me regex to look for!!!:')
regexUser = re.compile(input())
#regexUser = re.compile("bar")
for file in os.listdir(path):
    if file.endswith('.txt'):
        file = open(os.path.join(path, file),'r')
        strTempTex = file.read()
        matches = regexUser.findall(strTempTex)
        print(file.name + ":")
        for match in matches:
            print(match)
print('done')




