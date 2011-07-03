'''
Created on 26 Jun 2011

@author: david
'''
import htmllib

def unescape(s):
    p = htmllib.HTMLParser(None)
    p.save_bgn()
    p.feed(s)
    return p.save_end()

import os
import urllib2, string
from xml.dom import minidom
from xml.dom.minidom import parse, parseString

def getFlickr(items=10):
    # 
    url='http://api.flickr.com/services/feeds/photos_public.gne?tags=wyoming&amp;lang=en-us&amp;format=rss_200'
    handler = urllib2.urlopen(url)
    dom = minidom.parse(handler) 
    #print dom.toxml()   
    handler.close()
    entries = dom.getElementsByTagName('entry')
    flickrHTML='';
    for entry in entries[:items]:
        node = entry.getElementsByTagName('content')[0]
        node2 = entry.getElementsByTagName('content')[0].firstChild.data
        node2 = os.linesep.join([s for s in node2.splitlines() if s])
        node2 = node2.strip()
        try:
            dom2 = minidom.parseString('<test>' + node2+'</test>')
            imgtag = dom2.getElementsByTagName('img')
            atag = dom2.getElementsByTagName('a')

           
            hrefatt = atag[0].attributes['href']
            #print hrefatt.value
             
            imgatt = imgtag[0].attributes['src']

            flickrHTML = flickrHTML + '<a href="' +hrefatt.value  + ' "><img src="' +imgatt.value+ '" /></a>'
        except:
            pass
        
        #dom2 = parseString(unescape(node.toxml()))

    return flickrHTML;
    #items = entries_dom.getElementsByTagName('title')
    #for  (name, value) in items():
    #    print '    Attr -- Name: %s  Value: %s' % (name, value)
    #print str(item)
    
    