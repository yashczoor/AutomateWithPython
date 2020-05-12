#! python3
#program to fill the gaps in numbering of files. File name is prefix###, e.g. spam001, spam002, spam003
import os
from collections import OrderedDict

print('file prefix:')
prefix = input()
#select a folder TODO
path = "C:\\Users\\Piotr Jaroszuk\\Desktop\\python_kurs\\Automate Boring Stuff\\spamspam"
#get file names to the list
filesDict = {}
for foldername, subfolders, filenames in os.walk(path):
    for filename in filenames:
        if filename.startswith(prefix):
            filesDict[filename] = os.path.join(foldername, filename)
            #filesList.append(os.path.join(foldername, filename))          
print(filesDict)
#filesDict = OrderedDict(sorted(filesDict.items())) 
ignoreFirstFile = True
#TODO if the first file isnt 001, change it

for k, v in filesDict.items():
    while ignoreFirstFile:
        latterFile = k
        ignoreFirstFile = False
        continue
    if not int(k[len(prefix):len(prefix)+3]) = int(latterFile[len(prefix):len(prefix)+3]) + 1:
        #change the name of k file to latter+1
    #save k as latter
        
    print(k + ' ' + v)

#sort list,
#iterate, comparing file to the next one. If next one is not named + 1 then change, and check again
