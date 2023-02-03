from datetime import datetime
import requests

city = input('City: ')

url = 'http://api.openweathermap.org/data/2.5/forecast/daily'
url += '?appid=d1526a9039658a6f76950cff21823aff'
url += '&units=metric'
url += '&mode=json'
url += '&cnt=14'
url += '&q=' + city

print(url)

response = requests.get(url)
if (response.status_code == 200):
    decoded = response.json()
    # print(decoded)
    
    daily = decoded['list']
    # print(daily)
    
    for forecast in daily:
        # print(forecast)
        dt = datetime.fromtimestamp(forecast['dt'])
        temp_day = forecast['temp']['day']
        feels_like_day = forecast['feels_like']['day']
        description = forecast['weather'][0]['description']
        
        print(f"{dt.strftime('%d %B %Y %A'):28} {temp_day:8}°C {feels_like_day:8}°C   {description}")
    
else:
    print(f'Error for city {city}')
