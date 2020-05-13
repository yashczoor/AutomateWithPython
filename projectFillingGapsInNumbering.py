#! python3
#program to fill the gaps in numbering of files. File name is prefix###, e.g. spam001, spam002, spam003

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)
#using rreplace in case folder is of the same name as one of the files
#to replace last occurence of name in string
import os, shutil
from collections import OrderedDict

print('input file prefix:')
prefix = input()
#select a folder TODO
path = "C:\\Users\\Piotr Jaroszuk\\Desktop\\python_kurs\\Automate Boring Stuff\\spamspam"
#get file names to the list
filesDict = {}
for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if filename.startswith(prefix):
            filesDict[filename] = os.path.join(foldername, filename)
print(filesDict)
flagFirst = True
for k, v in filesDict.items():
    fileNumber = k[len(prefix):len(prefix)+3]
    if flagFirst:
        if not fileNumber == '001':
            print(fileNumber)
            print('change first name to 001')
            newPath = rreplace(v, fileNumber, '001', 1)
            print(newPath)
            shutil.move(v, newPath)
            k = os.path.basename(newPath)
        print('first loop')
        flagFirst = False
        previousFile = k
        continue
    else:
        previousFileNumber = previousFile[len(prefix):len(prefix)+3]
        if not int(fileNumber) == int(previousFileNumber) + 1:
            newFileNumber = str(int(previousFileNumber) + 1).zfill(3)
            print('changing ' + fileNumber + ' to ' + newFileNumber)
            print(v)
            previousFile = rreplace(previousFile, previousFileNumber, newFileNumber, 1)
            newFullPath = os.path.join(os.path.dirname(v),previousFile)
            #TODO actual file chaange
            shutil.move(v, newFullPath)
        else:
            print('Order correct')
            previousFile = k
