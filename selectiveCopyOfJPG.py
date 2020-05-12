#! python3
#get .pdf or .jpg or other from folder
import os, datetime, shutil #,sys
strDesktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
import tkinter as tk
from tkinter import filedialog
#ask user for extension
print("What extension do you want to get?")
#extension = sys.argv[1]
extension = input()
if not extension[0] == ".":
    extension = "." + extension
#get folder to copy from
root = tk.Tk()
root.withdraw() #to hide the empty window, only show Windows GUI
copyFromPath = filedialog.askdirectory()
#create folder for results
x = datetime.datetime.now()
x = x.strftime("%d%B%Y") #using locale?
targetPath = os.path.join(strDesktopPath, "Target folder for " + extension[1:] + ' from ' + os.path.basename(os.path.normpath(copyFromPath)) + x)

#targetPath = os.path.join(strDesktopPath, "Target folder for " + extension[1:] + ' from ' + os.path.basename(os.path.normpath(copyFromPath)) + str(datetime.date))
if not os.path.exists(targetPath):
    print(targetPath + ' created')
    os.mkdir(os.path.join(strDesktopPath, "Target folder for " + extension[1:] + ' from ' + os.path.basename(os.path.normpath(copyFromPath)) + x))

for foldername, subfolders, files in os.walk(copyFromPath):
    for file in files:
        if file.endswith(extension):
            print(os.path.join(foldername,file) + ' to ' + targetPath)
            shutil.copy(os.path.join(foldername,file),targetPath)
print('done')
#loop through folders looking for extension
#copy to new folder on desktop if found


