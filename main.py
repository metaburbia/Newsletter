import sys
from newsletter import news
from newsletter import weather
from newsletter import currency
from newsletter import images
from newsletter import flickr

from newsletter import flytime
from datetime import datetime
import time
import newsrssfeeds


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
    narr = '<h2 id="narrh">What''s ' + cityname + ' Doing?</h2>\
<p class="narr">In ' + cityname + ' the last time we checked \
the temperature was  ' + weather['current_conditions']['temp_f'] + '&deg;F\
, humidity was ' + strHumidity[1] + ' &#8212;  and\
 it was ' +  (weather['current_conditions']['condition']).lower() + '</p>'

    return narr

def daysToGo():

    flyTime = datetime(*(time.strptime(flytime.FlightTime, "%Y-%m-%d")[0:6]))
    #flyTime = datetime.strptime(flytime.FlightTime,'%Y-%m-%d')
    currentDateTime = datetime.now() 
    return (flyTime - currentDateTime).days 
    
def getNewsletterIntro():
    weather = oWeather.getWeather('Denver')
    forecastTimeString = weather['forecast_information']['forecast_date']

    forecastTime = datetime(*(time.strptime(forecastTimeString, "%Y-%m-%d")[0:6]))
    #forecastTime = datetime.strptime(forecastTimeString,'%Y-%m-%d')
    
    forecastDayNum  = int(forecastTime.strftime("%d"))
    
    newsletterTime = datetime(*(time.strptime(flytime.FlightTime, "%Y-%m-%d")[0:6]))
    #newsletterTime = datetime.strptime(flytime.FlightTime,'%Y-%m-%d')
    flyTime = datetime.now()
    diff = flyTime - newsletterTime
    intro = 'It''s ' +  forecastTime.strftime("%A") +  ' ' + ordinal(forecastDayNum) + ' of ' + forecastTime.strftime("%B") + ',\
 '+ str(daysToGo()) + ' days\
 until you fly to Denver'
    return intro
    
def createWeatherTable():
    # get the first row to extact the # of forecasts
    firstkey = weatherLocations.items()[0][0]
    weather = oWeather.getWeather(firstkey)
    print weather
    forecastsLength = len(weather['forecasts'])
    header = '<tr>'
    for i in range(0,3):
        header = '<th>' + header + '<th>' 
        
    for forecast in weather['forecasts'][1:4]:
        header = header + '<th>' + forecast['day_of_week'] + '</th>'
    header = header + '</tr>'
    table = '<table id="tbw">' 
    table=table+header
    
    for key, value in weatherLocations.items():
        weather = oWeather.getWeather(key)
        table = table + '<tr>'
        table = table + '<td>' + value + '</td>'
        table = table + '<td>' + weather['current_conditions']['temp_f'] + '&deg;F</td>'
        table = table + '<td class="cond">' + weather['current_conditions']['condition'] + '</td>'
        for forecast in weather['forecasts'][1:4]:
            table = table + '<td class="temp">' +  forecast['high'] + '&deg;F</td>'
        table = table + '</tr>' 
    table = table + '</table>'
    return table

flickr.getFlickr()  

sys.exit('')

intro = getNewsletterIntro()
writeFile('intro.inc',intro)

images.createCountdown(daysToGo())

getMainCityDetails('Denver')
writeFile('narrative.inc',getMainCityDetails('Denver'))

writeFile('currency.inc',currency.convert('GBP', "&pound;", 'USD', '$'))

table = createWeatherTable()
writeFile('weatherTable.inc',table)

oNews = news.news()
for key in newsrssfeeds.newsfeeds:
    item =  newsrssfeeds.newsfeeds[key]
    writeFile(item['outputfile'],oNews.getNews(item['url'],int(item['items'])))

 

              
              
              