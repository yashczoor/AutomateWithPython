#!python 3
#backupToZip - copies an entire folder and its contents into a ZIP file.Number in a name increments with each copy

import zipfile, os

def backupToZip(folder):
    #bup contents of folder into a zip
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + ' ' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

#create a ZIP
    print("Creating %s..." % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')
    
#walk the folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        #add curr folder to ZIP
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #don't backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('done')



backupToZip("D:\\AlsPythonBook")
