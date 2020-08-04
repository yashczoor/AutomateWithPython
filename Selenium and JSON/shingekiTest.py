import requests,os,bs4
url = 'https://w16.attack-on-titan.com/manga/shingeki-no-kyojin-chapter-1/'
pathToSave = 'C:\\Users\\Piotr Jaroszuk\\Desktop\\shingeki'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
#print(soup.prettify())
comicElem = soup.select('img')
print(comicElem)
