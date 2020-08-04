import requests, webbrowser, bs4

res = requests.get("https://itschool.pl/blog",'html.parser')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text)
#godzinySzkolen = soup.findAll('h2', class_='countLicznika clock')
godzinySzkolen = soup.find_all('link')
for i in range(len(godzinySzkolen)):
    print(godzinySzkolen[i].get('href'))
