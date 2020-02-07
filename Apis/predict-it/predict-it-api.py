#!/usr/bin/python3

import urllib.parse, urllib.request, urllib.error
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

    