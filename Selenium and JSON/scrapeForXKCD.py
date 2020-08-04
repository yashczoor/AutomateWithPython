#! python3
#download all xkcd comics
def askUserForPath():
    import tkinter as tk
    from tkinter import filedialog
    import sys, re, os
    
    root = tk.Tk()
    root.withdraw() #to hide the empty window, only show Windows GUI
    path = filedialog.askdirectory()
    return path

import requests,os,bs4
url = 'http://xkcd.com'
pathToSave = askUserForPath()
imgCount = 1
while not url.endswith('#'):    
    #download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #download the image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic img')
    else:
        comicUrl = comicElem[0].get('src')
        print('Downloading image %s...' % (comicUrl))
        comicUrl = 'http:' + comicUrl
        res = requests.get(comicUrl)
        res.raise_for_status()
    #save to selected folder
        fileName = str(imgCount) + '.' + os.path.basename(comicUrl)
        #imageFile = open(os.path.join(pathToSave, os.path.basename(comicUrl)), 'wb')
        imageFile = open(os.path.join(pathToSave, fileName), 'wb')
        imgCount += 1
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    #get the prev button url
    prevLink = soup.select('a[rel="prev"]')[0]
    print(prevLink)
    print(prevLink.get('href'))
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')
