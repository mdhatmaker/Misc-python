#!/usr/bin/python3

#from xml.dom.minidom import parse
#import xml.dom.minidom
#import urllib.request
from xml.dom import minidom
#import urllib
from lxml import html
import requests
import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import sys
#import urllib2
import xmltodict


### https://predictit.freshdesk.com/support/solutions/articles/12000001878-does-predictit-make-market-data-available-via-an-api-
### https://www.predictit.org/api/marketdata/markets/3633
### https://www.reddit.com/r/predictit/comments/5prpct/predictit_python_api/
### https://projects.fivethirtyeight.com/2020-primary-forecast/?ex_cid=rrpromo


"""
The latest trade price and the best offers to buy and sell shares are available for
any active market via an API. Data is updated every sixty seconds.

If you wish to receive data for all markets on the site, the format for the API URL is:
https://www.predictit.org/api/marketdata/all/

If you wish to receive data for a specific market, the format for the API URL is:
https://www.predictit.org/api/marketdata/markets/[ID]

where [id] refers to the numerical code pertaining to the market.


Market: Who will win the 2020 Democratic presidential nomination?
https://www.predictit.org/api/marketdata/markets/3633
"""

 

def get_all_markets():
    url = "https://www.predictit.org/api/marketdata/all/"
    url_to_open = urllib.request.urlopen(url).read()
    tree = ET.parse(url_to_open)
    root_node = tree.getroot()
    
    lst = root_node.findall('MarketData')
    i = 0
    for item in lst:
        #print(item)
        i += 1
        print(i)

    return

    """
    #f = urllib.request.urlopen(url)
    #myfile = f.read()
    #print(myfile)
    #DOMTree = xml.dom.minidom.parse(f)
    #collection = DOMTree.documentElement

    dom = minidom.parse(urllib.request.urlopen(url)) # parse the data
    #owned = dom.getElementsByTagName('owned')
    #owned = int(owned[0].attributes['value'].value

    markets = dom.getElementsByTagName('MarketData')
    #categories = [items.attributes['value'].value for items in link if items.attributes['type'].value == "boardgamecategory"]
    for mkt in markets:
        print(mkt)

    return

    #if collection.hasAttribute("shelf"):
    #    print ("Root element : %s" % collection.getAttribute("shelf"))

    # Get all the movies in the collection
    markets = collection.getElementsByTagName("Markets")

    # Print detail of each movie.
    for mkt in markets:
        print ("*****Market*****")
        #if mkt.hasAttribute("title"):
        #    print ("Title: %s" % movie.getAttribute("title"))
        id = mkt.getElementsByTagName('ID')[0]
        print ("ID: %s" % id.childNodes[0].data)
        name = mkt.getElementsByTagName('Name')[0]
        print ("Name: %s" % name.childNodes[0].data)

    return


def parse_xml():
    # Open XML document using minidom parser
    DOMTree = xml.dom.minidom.parse("movies.xml")
    collection = DOMTree.documentElement
    if collection.hasAttribute("shelf"):
        print ("Root element : %s" % collection.getAttribute("shelf"))

    # Get all the movies in the collection
    movies = collection.getElementsByTagName("movie")

    # Print detail of each movie.
    for movie in movies:
        print ("*****Movie*****")
        if movie.hasAttribute("title"):
            print ("Title: %s" % movie.getAttribute("title"))

        type = movie.getElementsByTagName('type')[0]
        print ("Type: %s" % type.childNodes[0].data)
    """


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


def homepage0(request):
    file = urllib2.urlopen('https://www.goodreads.com/review/list/20990068.xml?key=nGvCqaQ6tn9w4HNpW8kquw&v=2&shelf=toread')
    data = file.read()
    file.close()
    dom = parseString(data)

def homepage(url):  #request):
    file = urllib.request.urlopen(url)
    data = file.read()
    file.close()

    strdata = data.decode('UTF-8')
    print('\n\n' + strdata + '\n\n')

    data = xmltodict.parse(strdata)
    #return render_to_response('my_template.html', {'data': data})
    return data


if __name__ == "__main__":

    data = homepage('https://www.predictit.org/api/marketdata/markets/3633')
    print(data)
    sys.exit()
    #get_all_markets()
 
    """
    list_of_ints = []
    response = requests.get(url)
    #tree = ET.parse(response.content)
    #tree = html.fromstring(response.content)
    tree = ET.fromstring(response.content)
    root = tree.getroot()
    lst = root.findall('MarketData')    #root.findall('comment')
    for item in lst:
        #print(item)     #item.find('count'))
        print("hi")
    sys.exit()
    """

    """
    url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
    response = requests.get(url)
    dom = minidom.parse(urllib.request.urlopen(url))
    markets = dom.getElementsByTagName('comment')
    #myvalue= int(markets[0].attributes['value'].value
    for mkt in markets:
        #print(mkt.hasChildNodes())    # dir(mkt))
        elem = mkt.getElementsByTagName('name')[0]
        print(getText(elem.childNodes), end='   ')
        elem = mkt.getElementsByTagName('count')[0]
        print(getText(elem.childNodes))


    url = 'https://www.predictit.org/api/marketdata/all/'
    response = requests.get(url)
    dom = minidom.parse(urllib.request.urlopen(url))
    markets = dom.getElementsByTagName('Markets')
    for mkt in markets:
        elem = mkt.getElementsByTagName('ID')[0]
        print(getText(elem.childNodes), end='   ')
        elem = mkt.getElementsByTagName('Name')[0]
        print(getText(elem.childNodes))
    """

    url = 'https://www.predictit.org/api/marketdata/markets/3633'



    sys.exit()

    """
    count = tree.xpath('//count')
    #total =  sum(int(i.text) for i in count)
    #print(f'The sum of all count is doc is: {total}')
    #print(f'count = {count}')
    for i in count:
        print(i.text)
    comments = tree.xpath('//comment')
    for item in comments:
        print(item)
    """


