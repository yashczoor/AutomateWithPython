#! python3
def askUserForPath():
    import tkinter as tk
    from tkinter import filedialog
    import sys, re, os
    
    root = tk.Tk()
    root.withdraw() #to hide the empty window, only show Windows GUI
    path = filedialog.askdirectory()
    return path

def getNextUrl(soup):
    nextLink = soup.select('a[rel="next"]')[0]
    #print(nextLink.get('href'))
    url = nextLink.get('href')
    return url
    
import requests,os,bs4
url = 'https://w16.attack-on-titan.com/manga/shingeki-no-kyojin-chapter-1/'
pathToSave = askUserForPath()
#pathToSave = 'C:\\Users\\Piotr Jaroszuk\\Desktop\\shingeki'
count = 0
while not url.endswith('#'):
    count += 1
    #download the page
    print('Downloading comic %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    try:
        comicPath = os.path.join(pathToSave, str(count))#add try except for if exists continue with next comic
        comicFolder = os.mkdir(comicPath)
    except:
        print('Skipped to episode number ' + str(count + 1))
        url = getNextUrl(soup)
        continue
    comicPage = soup.findAll('img', class_='lazyload')
    print(comicPath)
    for p in comicPage:
        print(p.get('data-src'))
        pageUrl = p.get('data-src')
        fileName = os.path.basename(pageUrl)
        #imageFile = open(os.path.join(pathToSave, os.path.basename(comicUrl)), 'wb')
        imageFile = open(os.path.join(comicPath, fileName), 'wb')
        #for chunk in res.iter_content(1000000):
        res = requests.get(pageUrl)
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        url = getNextUrl(soup)
print('Done.')
