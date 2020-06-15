#! python3
#fetch weather for next few days from Web
#weather.py - weather [location] in cmd

import sys, requests, json
#Compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: weather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
#location = 'Poznań'
apiKey = '83dc0f3914959a9289efdf388b36fe17' #required since 2015. One needs free account at Open Weather Map
#TODO download json data
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location, apiKey)
response = requests.get(url)
response.raise_for_status()
weatherData = json.loads(response.text)
w = weatherData['weather']
print('Current weather in %s:' % (location))
print(w[0]['main'], '-',w[0]['description'])
