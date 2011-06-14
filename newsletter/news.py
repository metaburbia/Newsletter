'''
Created on 9 Jun 2011

@author: david
'''
import rss

class news(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def sayHello(self):
        print 'dffsf'
            
    def getNews(self,rssURL,numItems=10):
        oRSS = rss.RSSFeed()
        oRSS.rssURL = rssURL
        oRSS.getRSS()
        result=''
        data = oRSS.data 
        for entry in data.entries[:numItems]:
            result=result+ '<dt><a href="' + entry.link+ '">' + entry.title + '</a></dt>'
            result=result+ '<dd>' + entry.summary + '</dd>'
        if result != '':
            result = '<dl>' + result + '</dl>'
        return result
    
