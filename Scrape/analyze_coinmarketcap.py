import sys
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import json
import time
import pytz
from datetime import datetime
import os


_headers = []
_lines = {}
#_times = set()

def printLine(li):
  timeGMT = li['timeGMT']
  symbol = li['symbol']
  name = li['name']
  #priceChange = li['priceChange']
  price = float(li['price$'])
  priceChange1h = float(li['priceChange1h%'])
  priceChange24h = float(li['priceChange24h%'])
  priceChange7d = float(li['priceChange7d%'])
  priceChange30d = float(li['priceChange30d%'])
  volume24h = float(li['volume24h'])
  print(f'{timeGMT} [{symbol:<9} {name:<30} {price:>14.8f}]  1h:{priceChange1h:>7.2f}%  24h:{priceChange24h:>7.2f}%  7d:{priceChange7d:>7.2f}%  30d:{priceChange30d:>7.2f}%  vol24h:{volume24h:>12.2f}')
  
def printLines(t, lineList):
  print(f'{t}  ({len(lineData)} crypto items)')
  for lineStr in lineList:
    #print(f'  {lineStr}')
    li = parseLine(lineStr)
    printLine(li)

def printSummary(symbol, lines):
  items = list(lines)
  count = len(items)
  first = items[0]
  last = items[-1]
  print(f"{symbol:<9} ({count:>4} lines  {first['timeGMT']} - {last['timeGMT']})", end='')

  highPct = 0.0
  highItem = None
  lowPct = 1000000.0
  lowItem = None
  for li in items:
    chg = float(li['priceChange24h%'])
    if chg > highPct:
      highPct = chg
      highItem = li
    if chg < lowPct:
      lowPct = chg
      lowItem = li
  #print(f"  low   {lowPct:>7.2f}%  at  {lowItem['timeGMT']}")
  #print(f"  high  {highPct:>7.2f}%  at  {highItem['timeGMT']}  -->  gain = {highPct-lowPct:.0f}%")
  elapsedTime = convertGMT(highItem['timeGMT']) - convertGMT(lowItem['timeGMT'])
  elapsedHours = elapsedTime.seconds / (60 * 60)
  print(f"  l:{lowPct:>5.1f}% {lowItem['timeGMT']}  h:{highPct:>5.1f}% {highItem['timeGMT']} --> gain = {highPct-lowPct:>4.0f}%  {elapsedHours:.1f}")

def findSymbol(symbol, displaySummary = False):
  rv = []
  for t in _lines:
    lineList = _lines[t]
    for lineStr in lineList:
      li = parseLine(lineStr)
      if li['symbol'] == symbol:
        rv.append(li)
  if displaySummary: printSummary(symbol, rv)
  return rv

def findAllSymbols():
  rv = {}
  for t in _lines:
    lineList = _lines[t]
    for lineStr in lineList:
      li = parseLine(lineStr)
      rv[li['symbol']] = li['name']
  return rv

def toCsvLines(dictList):
  rv = []
  now = nowStr()
  for li in dictList:
    name = li['name']
    symbol = li['symbol']
    prices = li['priceChange']
    price = prices['price']
    priceChange1h = prices['priceChange1h']
    priceChange24h = prices['priceChange24h']
    priceChange7d = prices['priceChange7d']
    priceChange30d = prices['priceChange30d']
    volume24h = prices['volume24h']
    rv.append(f'{now},{symbol},{name},{price:.8f},{priceChange1h:.2f},{priceChange24h:.2f},{priceChange7d:.2f},{priceChange30d:.2f},{volume24h:.2f}')
  return rv

def nowStr():
  return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())  # time.localtime())

def convertGMT(datetime_string):
    date_var = datetime.strptime(datetime_string + "+00:00", '%Y-%m-%d  %H:%M:%S%z')
    #date_var = date_var.replace(tzinfo=pytz.UTC)
    return date_var.astimezone(pytz.timezone('US/Central'))

def nowFilename():
  now = nowStr()
  now = now.replace(':', '-')
  now = now.replace(' ', '-')
  return 'crypto_gainers-' + now + '.csv'

def openFile(path, filename):
  pathname = os.path.join(path, filename)
  f = open(pathname, 'r')
  _headers.extend(f.readline().strip().split(','))
  prt(f'opened file "{pathname}"')
  return f

def cleanUp(f):
  f.close()

def parseLine(lineStr):
  lineData = lineStr.split(',')
  data = {}
  # count should be equal for lineData and _headers
  for i in range(len(_headers)):
    data[_headers[i]] = lineData[i]
  return data

"""def parseLines(lineList):
  data = {}
  for lineStr in lineList:
    li = parseLine(lineStr)
    data[li['timeGMT']] = li
  return data"""

def prt(s):
  print(f'[{nowStr()}]  ' + s)

def getSoup(URL):
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, 'html.parser')
  return soup

def getData(soup, debug_print = False):
  results = soup.find(id='__NEXT_DATA__')
  text = results.prettify()
  split = text.split('\n')
  jsonStr = split[1].strip()
  if debug_print: print(jsonStr, '\n')
  pyObj = json.loads(jsonStr)
  if debug_print: print(type(pyObj))   # 'dict'
  return pyObj

# Where name like 'goatcoin' or 'triumphx'
def getMarkets(unformattedName, soup = None):
  name = unformattedName.replace(' ', '-').lower()
  URL = f'https://coinmarketcap.com/currencies/{name}/'                   # overview
  #URL = f'https://coinmarketcap.com/currencies/{name}/markets/'           # markets
  #URL = f'https://coinmarketcap.com/currencies/{name}/historical-data/'   # historical data
  #URL = f'https://coinmarketcap.com/currencies/{name}/wallets/'           # wallets
  if soup is None:
    soup = getSoup(URL)
  #data = getData(soup)
  #d = data['props']['initialState']['cryptocurrency']
  #keys = ['listingLatest', 'listingHistorical', 'new', 'watchlist', 'map', 'info', 'prices', 'quotesLatest', 'quotesHistorical', 'ohlcvHistorical', 'related', 'marketPairsLatest', 'pricePerformanceStatsLatest', 'topDerivatives', 'yieldFarmingRankingLatest', 'gainersLosers', 'trendingCoins', 'mostViewed', 'spotlight']
  #prices = d['prices']
  exchanges = []
  for header in soup.find_all('h2'):
    nextNode = header
    while True:
        nextNode = nextNode.nextSibling
        if nextNode is None:
            break
        if isinstance(nextNode, NavigableString):
            stripStr = (nextNode.strip())
            #print(stripStr)
        if isinstance(nextNode, Tag):
            if nextNode.name == "h2":
                break
            if nextNode.name == "p":
                ptext = nextNode.get_text(strip=False).strip()
                if ptext.startswith('The top exchanges'):
                  #print(ptext)
                  i1 = ptext.find(' are currently ') + len(' are currently ')
                  i2 = ptext.find(' You can ')
                  exchStr = ptext[i1:i2-1]
                  exchStr = exchStr.replace(' and ', '')
                  exchanges = exchStr.replace(', ', ',').strip().split(',')
                #elif ptext.startswith('The live'):
                #  print(ptext)
            else:
              text = (nextNode.get_text(strip=False).strip())
              #print(text)
  return exchanges  #, soup



print("======================================================================================================================================================")
print("======================================================================================================================================================")

path = '/Users/michael/data/crypto_gainers'

# Read column headers and lines from CSV file
f = openFile(path, 'crypto_gainers-2021-04-28-06-09-00.csv')

count = 0
while True:
  li = f.readline()
  if not li:
    break
  count = count + 1
  line = li.strip()
  #_lines.append(line)
  t = line.split(',')[0]
  if t in _lines:
    _lines[t].append(line)
  else:
    _lines[t] = [ line ]
  #_times.add(t)
cleanUp(f)

symbols = findAllSymbols()
prt(f'read {count:,} lines ({len(_lines):,} time keys) ({len(symbols)} symbols)')


#symbols = ['BB', 'SNN', 'NYEX', 'GOAT', 'TRIX', 'XPRT', 'MOON STOP']
#soup = None
for symbol in symbols:
  #lines = findSymbol(symbol, True)
  name = symbols[symbol]
  print(f'{symbol:<12} {name}')      # print crypto symbol and name
  #exchanges = getMarkets(name)
  #print(f'  {exchanges}')
  #time.sleep(5)

#exchanges, soup = getMarkets('TriumphX')
#print(exchanges)
#exit()

