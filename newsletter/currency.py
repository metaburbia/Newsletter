import urllib2, feedparser
import re
import getopt

'''
def ExchangeRate(fromCurrency, toCurrency):
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	url = 'http://www.google.co.uk/search?q='+fromCurrency+'+to='+toCurrency
	headers={'User-Agent':user_agent,}
	print url
	request=urllib2.Request(url,None,headers) 
	response = urllib2.urlopen(request)
	data = response.read()
	where  = data.find('<b>1 British pound')

	print data
'''	
def convert(currencyFrom, symbol1, currencyTo, symbol2):
    currencyline=urllib2.urlopen('http://www.google.com/ig/calculator?hl=en&q=1' + currencyFrom + '%3D%3F' + currencyTo).read()
    result = re.search(".*rhs: \"(\d\.\d*)", currencyline)
    if result:
        return symbol1 +"1"  + " = " + symbol2 + result.group(1)
        
  


	
	