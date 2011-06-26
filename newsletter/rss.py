'''
Created on 11 Jun 2011

@author: david
'''
import urllib2, feedparser

class RSSFeed:
    '''
    classdocs
    '''
    rssURL=''
    data=''
    
    def __init__(self):
        '''
        Constructor
        '''
    def sayHello(self):
        print 'dffsf'
        
    def getRSS(self):
        self.data=''
        #d=feedparser.parse('http://www.action3news.com/category/13544/strange-news?clienttype=rss', handlers = [proxy])
        self.data=feedparser.parse(self.rssURL)

        
    
