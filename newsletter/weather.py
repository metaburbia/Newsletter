'''
Created on 11 Jun 2011

@author: david
'''
import urllib2, string
from xml.dom import minidom
GOOGLE_WEATHER_URL = 'http://www.google.com/ig/api?weather=%s&hl=%s'

class weather(object):
    '''
    classdocs
    '''
    weatherData =''

    def __init__(self):
        '''
        Constructor
    
        '''
    def sayHello(self):
        print 'Weather'    

    def getWeather(self,location_id, hl = ''):
        """
        Fetches weather report from Google
    
        Parameters 
          location_id: a zip code (10001); city name, state (weather=woodland,PA); city name, country (weather=london,england); or possibly others.
          hl: the language parameter (language code)
    
        Returns:
          weather_data: a dictionary of weather data that exists in XML feed. 
        """
    
        url = GOOGLE_WEATHER_URL % (location_id, hl)
        handler = urllib2.urlopen(url)
        dom = minidom.parse(handler)    
        handler.close()
    
        weather_data = {}
        weather_dom = dom.getElementsByTagName('weather')[0]
    
        data_structure = { 
            'forecast_information': ('city', 'postal_code', 'latitude_e6', 'longitude_e6', 'forecast_date', 'current_date_time', 'unit_system'),
            'current_conditions': ('condition','temp_f', 'temp_c', 'humidity', 'wind_condition', 'icon')
        }           
        for (tag, list_of_tags2) in data_structure.iteritems():
            tmp_conditions = {}
            for tag2 in list_of_tags2:
                tmp_conditions[tag2] =  weather_dom.getElementsByTagName(tag)[0].getElementsByTagName(tag2)[0].getAttribute('data')
            weather_data[tag] = tmp_conditions
    
        forecast_conditions = ('day_of_week', 'low', 'high', 'icon', 'condition')
        forecasts = []
        
        for forecast in dom.getElementsByTagName('forecast_conditions'):
            tmp_forecast = {}
            for tag in forecast_conditions:
                tmp_forecast[tag] = forecast.getElementsByTagName(tag)[0].getAttribute('data')
            forecasts.append(tmp_forecast)
    
        weather_data['forecasts'] = forecasts    
        dom.unlink()
        print weather_data
        return weather_data
    
    def getChattyWeather(self,location_id, location_string = ''):
        
        if location_string == '':
            location_string = location_id
        report = self.getWeather(location_id)
        strHumidityPos = report['current_conditions']['humidity'].find(':')
        strHumidity = report['current_conditions']['humidity'].split()
        script = ('In ' + location_string + ' it\'s ' + report['current_conditions']['condition'] + '. '
         + 'Temperature\'s ' + str(report['current_conditions']['temp_f'])
        + 'F (' + str(report['current_conditions']['temp_c']) + 'C) '
       ' with  ' + strHumidity[1] + ' humidity.'
        )
        return script
        