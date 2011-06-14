from newsletter import news
from newsletter import weather



oRSS = news.news()


#print oRSS.getNews('http://www.action3news.com/category/13544/strange-news?clienttype=rss', 4)


#print oRSS.getNews('http://www.rapidcityjournal.com/search/?f=rss&t=article&c=news/local&l=25&s=start_time&sd=desc', 4)

oWeather = weather.weather()

weatherLocations = {
                    'Salt+Lake+City':'Salt Lake City',
                    'Denver':'Denver',
                    }
'''
for loc in weatherLocations:
   print loc.values()
 '''
for key, value in weatherLocations.items():
    print key, value
'''
denverWeather = oWeather.getWeather('Denver')
print denverWeather
print denverWeather['current_conditions']['temp_f']
print denverWeather['current_conditions']['temp_c']
print denverWeather['current_conditions']['humidity']
print denverWeather['current_conditions']['condition']

print denverWeather['forecasts']
for forecast in denverWeather['forecasts']:
    print forecast['day_of_week']
    print forecast['high']
    print forecast['low']
    print forecast['condition']
'''
'''
denverWeather = oWeather.getChattyWeather('Denver')
print denverWeather

casperWeather = oWeather.getChattyWeather('Casper', 'Casper, Wyoming')
print casperWeather

saltLakeWeather = oWeather.getChattyWeather('Salt+Lake+City','Salt Lake City')
print saltLakeWeather
'''
denverWeather = oWeather.getWeather('Denver')

print denverWeather

for forecast in denverWeather['forecasts']:
    print forecast['day_of_week']
    print forecast['high']
    print forecast['low']
    print forecast['condition']
    print forecast
    