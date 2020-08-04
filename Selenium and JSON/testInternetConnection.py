#! python 3, pip install requests
import requests

def isInternet():
    url = 'http://google.com/'
    try:
        requests.get(url, timeout = 5)
        return True
    except:
        print('Connection error')
        return False
        
isInternet()
