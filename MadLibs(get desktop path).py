#! python3
import os,sys, re

strFileName = "MadLibs.txt"
strDesktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
#txt file name is on Desktop and is called MadLibs.txt. If it's not, finish
strFilePath = os.path.join(strDesktopPath, strFileName)
regexWordsToSwap = re.compile("ADJECTIVE|NOUN|VERB|ADVERB")
try:
    file = open(strFilePath, 'r')
    strText = file.read()
    matchingObject = regexWordsToSwap.findall(strText)
    for match in matchingObject:
        print('Enter ' + str(match))
        tmpSubWith = input()
        strText = strText.replace(match,tmpSubWith,1)
    file = open(strFilePath,'w')
    file.write(strText)
    file.close()
    print('All changed')
except IOError:
    try:
        print('There was an error opening the file!')
        print('Expected to find MadLibs.txt on Desktop')
        sys.exit()
    except SystemExit:
        print('')
