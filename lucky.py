#! python3
#lucky.py - Opens several Google search results
import requests, sys, webbrowser, bs4

print('Googling...') #display while googling
res = requests.get('http://www.google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

#todo retrieve top search result links
#todo open a browser tab for each result
