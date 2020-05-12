#! python3
#get names of large files (over >100 mb)
import enum
# Enum for size units
class SIZE_UNIT(enum.Enum):
   BYTES = 1
   KB = 2
   MB = 3
   GB = 4
 
def convert_unit(size_in_bytes, unit):
   """ Convert the size from bytes to other units like KB, MB or GB"""
   if unit == SIZE_UNIT.KB:
       return size_in_bytes/1024
   elif unit == SIZE_UNIT.MB:
       return size_in_bytes/(1024*1024)
   elif unit == SIZE_UNIT.GB:
       return size_in_bytes/(1024*1024*1024)
   else:
       return size_in_bytes

import os
import tkinter as tk
from tkinter import filedialog
#get folder to copy from
root = tk.Tk()
root.withdraw() #to hide the empty window, only show Windows GUI
path = filedialog.askdirectory()
for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        #print(round(os.path.getsize(os.path.join(foldername, filename))/(1024*1024),2))
        fileSizeMB = os.path.getsize(os.path.join(foldername, filename))/(1024*1024) 
        if fileSizeMB > 100:
            print(os.path.join(foldername, filename) + "\nWeighs: " + str(round(fileSizeMB,2)))
            



