from newsletter import news
from newsletter import weather
from newsletter import currency
from newsletter import images
from newsletter import flytime
from datetime import datetime
import time


oRSS = news.news()


#print oRSS.getNews('http://www.action3news.com/category/13544/strange-news?clienttype=rss', 4)


#print oRSS.getNews('http://www.rapidcityjournal.com/search/?f=rss&t=article&c=news/local&l=25&s=start_time&sd=desc', 4)

oWeather = weather.weather()

weatherLocations = {
                    'Salt+Lake+City':'Salt Lake City',
                    'Cheyenne,Wyoming':'Cheyenne, Wyoming',
                    'Bryce+Canyon':'Bryce Canyon',
                    }
def writeFile(filename, contents):
    text_file = open(filename, "w")
    text_file.write(contents)
    text_file.close()
    
def ordinal(n):
    if 10 <= n % 100 < 20:
        return str(n) + 'th'
    else:
       return  str(n) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(n % 10, "th")

def getMainCityDetails(cityname):
    weather = oWeather.getWeather(cityname)
    strHumidity = weather['current_conditions']['humidity'].split()
    narr = '<h2>What''s ' + cityname + ' Doing?</h2>\
<p>In ' + cityname + ' the last time we checked \
the temperature was  ' + weather['current_conditions']['temp_f'] + '&deg;F\
, humidity was ' + strHumidity[1] + ' &#8212;  and\
 it was ' +  (weather['current_conditions']['condition']).lower() + '</p>'

    return narr


def getNewsletterIntro():
    weather = oWeather.getWeather('Denver')
    forecastTimeString = weather['forecast_information']['forecast_date']
    forecastTime = datetime.strptime(forecastTimeString,'%Y-%m-%d')
    forecastDayNum  = int(forecastTime.strftime("%d"))
    newsletter.FlyTime = datetime.strptime(newsletter.FlightTime,'%Y-%m-%d')
    flyTime = datetime.now()
    diff = flyTime - newsletterTime
    intro = 'It''s ' +  forecastTime.strftime("%A") +  ' ' + ordinal(forecastDayNum) + ' of ' + forecastTime.strftime("%B") + ',\
 '+ str(diff.days) + ' days\
 until you fly to Denver'
    print weather
    return intro
    
def createWeatherTable():
    # get the first row to extact the # of forecasts
    firstkey = weatherLocations.items()[0][0]
    weather = oWeather.getWeather(firstkey)

    forecastsLength = len(weather['forecasts'])
    header = '<tr>'
    for i in range(0,3):
        header = '<th>' + header + '<th>' 
        
    for forecast in weather['forecasts']:
        header = header + '<th>' + forecast['day_of_week'] + '</th>'
    header = header + '</tr>'
    table = '<table>' 
    table=table+header
    
    for key, value in weatherLocations.items():
        weather = oWeather.getWeather(key)
        table = table + '<tr>'
        table = table + '<td>' + value + '</td>'
        table = table + '<td>' + weather['current_conditions']['temp_f'] + '&deg;F</td>'
        table = table + '<td>' + weather['current_conditions']['condition'] + '</td>'
        for forecast in weather['forecasts']:
            table = table + '<td>' +  forecast['high'] + '&deg;F</td>'
        table = table + '</tr>' 
    table = table + '</table>'
    return table
'''

for loc in weatherLocations:
   print loc.values()
 '''
intro = getNewsletterIntro()
writeFile('intro.inc',intro)
 
table = createWeatherTable()
writeFile('weatherTable.inc',table)

getMainCityDetails('Denver')
writeFile('narrative.inc',getMainCityDetails('Denver'))

currency.convert('GBP', "&pound;", 'USD', '$')


writeFile('currency.inc',currency.convert('GBP', "&pound;", 'USD', '$'))

images.createCountdown(32)

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

denverWeather = oWeather.getWeather('Denver')

print denverWeather

for forecast in denverWeather['forecasts']:
    print forecast['day_of_week']
    print forecast['high']
    print forecast['low']
    print forecast['condition']
    print forecast
    '''