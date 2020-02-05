import sys
import os
import urllib, json
import time
import requests


# change to directory in which this python script is running
dir_path_this = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path_this)


def get_kraken_ticker(pair):
    url = "https://api.kraken.com/0/public/Ticker?pair=%s" % (pair)
    response = requests.get(url)
    data = json.loads(response.text)
    symbol = data['result'].keys()[0]
    ticker = data['result'][symbol]
    inside_market = [float(ticker['b'][1]), float(ticker['b'][0]), float(ticker['a'][0]), float(ticker['a'][1])]
    return symbol, ticker, inside_market

#s, d, im = get_kraken_ticker('XXBTZEUR')
#s, d, im = get_kraken_ticker('BTCEUR')
#print s
#print d
#print im

filename = '/Users/mhatmaker/Dropbox/alvin/documents/KRAKEN trading system trades 2018-02-09.txt'
lines = list(open(filename))
print "Reading trades from file: '%s'" % filename

pair = 'BTCEUR'
print "KRAKEN trades: '%s'" % (pair)
trades = [s for s in lines if s.startswith(pair)]

maker_fee = 0.0016
taker_fee = 0.0026
fees = 0

split = trades[0].split()
print '1x', split[1], split[5], split[9]+split[10][:-1]
fees += 1 * float(split[5]) * taker_fee
if split[1] == 'buy':
    total = -1 * float(split[5])
else:
    total = 1 * float(split[5])
    
for t in trades[1:]:
    split = t.split()
    #print split[0], split[1], split[2], split[3], split[4], split[5]
    print '2x', split[1], split[5], split[9]+split[10][:-1]
    fees += 2 * float(split[5]) * taker_fee
    if split[1] == 'buy':
        total -= 2 * float(split[5])
    else:
        total += 2 * float(split[5])
        
trade_count = len(trades)
units_traded = 2 * trade_count - 1

s, d, im = get_kraken_ticker(pair)

print "\n%s ticker:  %fx%f|%fx%f" % (pair, im[0], im[1], im[2], im[3])

print
print "trades: %d     units: %d" % (trade_count, units_traded)
print
print "SUBTOTAL: %f" % total
print "FEES: ?" #%.2f" % (fees)
if trades[-1].split()[1] == 'buy':
    print "last trade was a BUY, so add this number to the current %s trading price to get P&L (in units)" % (pair)
    price = float(d['b'][0])
    print "selling at %f gives TOTAL: %f" % (price, total + price)
else:
    print "last trade was a SELL, so subtract the current %s trading price from this number to get P&L (in units)" % (pair)
    price = float(d['a'][0])
    print "buying at %f gives TOTAL: %f (units)" % (price, total - price)


'''
# KRAKEN FEE SCHEDULE
# https://www.kraken.com/en-us/help/fees

XBTEUR
Maker Taker Volume
0.16% 0.26% <50,000
0.14% 0.24% <100,000
0.12% 0.22% <250,000
0.10% 0.20% <500,000
0.08% 0.18% <1,000,000
0.06% 0.16% <2,500,000
0.04% 0.14% <5,000,000
0.02% 0.12% <10,000,000
0.00% 0.10% >10,000,000
'''
