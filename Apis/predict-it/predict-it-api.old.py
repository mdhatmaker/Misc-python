#!/usr/bin/python3

#from xml.dom.minidom import parse
from xml.dom import minidom
from lxml import html
import requests
import urllib.parse, urllib.request, urllib.error
import xml.etree.ElementTree as ET
import xmltodict
import json
import sys


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
    strdata = get_text_from_url(url)
    print('\n\n' + strdata + '\n\n')
    data = xmltodict.parse(strdata)
    #return render_to_response('my_template.html', {'data': data})
    return data
"""


class MarketData:
    def __init__(self, cdict):
        self.id = cdict['id']
        self.name = cdict['name']
        self.shortName = cdict['shortName']
        self.image = cdict['image']
        self.url = cdict['url']
        self.contracts = cdict['contracts']
        self.timeStamp = cdict['timeStamp']
        self.status = cdict['status']

    def __str__(self):
        return "{} [{}] {} '{}'  {}  ==>  {} contracts".format(self.id, self.shortName, self.status, self.name, self.timeStamp, len(self.contracts))

class MarketContract:
    def __init__(self, cdict):
        self.id = cdict['id']
        self.dateEnd = cdict['dateEnd']
        self.image = cdict['image']
        self.name = cdict['name']
        self.shortName = cdict['shortName']
        self.status = cdict['status']
        self.lastTrade = cdict['lastTradePrice']
        self.bestBuy = cdict['bestBuyYesCost']
        self.bestBuy0 = cdict['bestBuyNoCost']
        self.bestSell = cdict['bestSellYesCost']
        self.bestSell0 = cdict['bestSellNoCost']
        self.closePrice = cdict['lastClosePrice']
        self.displayOrder = cdict['displayOrder']

    def __str__(self):
        return "{} {} [{}] {} '{}'   last:{}  buy:{} sell:{}  close:{}".format(self.id, self.dateEnd, self.shortName, self.status, self.name, self.lastTrade, self.bestBuy, self.bestSell, self.closePrice)



def get_text_from_url(url):
    file = urllib.request.urlopen(url)
    data = file.read()
    file.close()
    strdata = data.decode('UTF-8')
    return strdata

def get_market(market_id):
    strdata = get_text_from_url('https://www.predictit.org/api/marketdata/markets/{}'.format(market_id))
    data = json.loads(strdata)
    return data

def get_all_markets():
    strdata = get_text_from_url('https://www.predictit.org/api/marketdata/all/')
    data = json.loads(strdata)
    return data

def print_market(id):
    mdict = get_market(id)
    mkt = MarketData(mdict)
    print()
    print(mkt)    
    print('    IMAGE  ' + mkt.image)
    print('    URL    ' + mkt.url)
    #print()
    for i,cdict in enumerate(mkt.contracts):
        #print('{}'.format(i), end='  ')
        c = MarketContract(cdict)
        print(c)
    print()
    return


###############################################################################
if __name__ == "__main__":

    markets = get_all_markets()['markets']
    print('\n\n*** {} markets ***\n'.format(len(markets)))
    for i,mdict in enumerate(markets):
        m = MarketData(mdict)
        print(m)
    print()
    #sys.exit()

    print_market(3633)
    sys.exit()

    
 
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


