#! python3
#rename files with mm-dd-yyyy date format to dd-mm-yyyy

import shutil, os, re

strPath = "C:\\Users\\Piotr Jaroszuk\\Desktop\\python_kurs\\Automate Boring Stuff\\9 Organizing files\\wrong dates"
#regex for am dates
datePattern = re.compile(r"""^(.*?) #all text before the date
    ((0|1)?\d)-                     #one or two digits for the month
    ((0|1|2|3)?\d)-                 #one or two digits for the day
    ((19|20)\d\d)                   #four digits for yer
    (.*?)$                          #all text after the date
    """, re.VERBOSE)
#loop working dir files
for amerFilename in os.listdir(strPath):
    mo = datePattern.search(amerFilename)
    #skip files without a date
    if mo == None:
        continue #next iteration
    #get parts of filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
    #form eur style filename
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    #get full, abs file paths
    absWorkingDir = strPath #os.path.abspath('.') <- I keep my path absolute from the beggining
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    #rename
    print(amerFilename)
    print(euroFilename)
    print('Renaming "%s" to "%s"...' % (amerFilename,euroFilename))
    #shutil.move(amerFilename,euroFilename) #uncomment after print test
    
