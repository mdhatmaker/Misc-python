import sys
import requests
from bs4 import BeautifulSoup
import json
import time
#from datetime import datetime
import os

DEBUG = False

def prt(s):
  print(f'[{nowStr()}]  ' + s)

def nowStr():
  return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())  # time.localtime())

def nowFilename(prefix):
  now = nowStr()
  now = now.replace(':', '-')
  now = now.replace(' ', '-')
  return f'{prefix}-{now}.csv'

def createFile(path, filePrefix):
  filename = nowFilename(filePrefix)
  pathname = os.path.join(path, filename)
  f = None
  if not DEBUG:
    f = open(pathname, 'w')
    f.write(getHeaders() + '\n')
  prt(f'created file "{pathname}"')
  return f, filename, pathname

def cleanUp(f):
  if not DEBUG:
    f.close()

def writeToFile(f, outputList):
  for li in outputList:
    if not DEBUG:
      f.write(li + '\n')
    else:
      print(f'   {li}')

def getSoup(URL):
  soup = None
  try:
    if DEBUG: prt(f'requesting URL: {URL}')
    page = requests.get(URL)
    if DEBUG: prt(f'parsing HTML')
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup
  except:
    prt(f'ERROR')
    return None


def getTableRows(table, parseHeader = False):
  data = []
  #table = soup.find('table', attrs={'class':'lineItemsTable'})
  #table_body = table.find('tbody')
  #rows = table_body.find_all('tr')
  rows = table.find_all('tr')
  for row in rows:
      if parseHeader == True:
        cols = row.find_all('th')
        parseHeader = False
      else:
        cols = row.find_all('td')
      cols = [ele.text.strip() for ele in cols]
      data.append([ele for ele in cols if ele]) # Get rid of empty values
  return data
#######################################################################################################################
def getTopCryptos():
  data = {}
  URL = 'https://cryptomarkettoday.com/markets/top-cryptos.aspx'
  soup = getSoup(URL)
  if soup is not None:
    table = soup.find(id='tblGainers')  # tblGainers, tblLosers, tblMostActive, tblUnusualVolume
    data['Gainers'] = getTableRows(table, True)
    table = soup.find(id='tblLosers')
    data['Losers'] = getTableRows(table, True)
    table = soup.find(id='tblMostActive')
    data['MostActive'] = getTableRows(table, True)
    table = soup.find(id='tblUnusualVolume')
    data['UnusualVolume'] = getTableRows(table, True)
  return data

def getHeaders():
  return 'timeGMT,symbol,name,price$,priceChange%,volume$,mktcap'
  #<th>symb</th><th class='moverNameTH'>name</th><th>$price</th><th>%chg</th><th>$volume</th><th>MktCap</th>

def parseLine(line):
  data = {}
  data['symbol'] = line[0]
  data['name'] = line[1]
  data['price$'] = line[2]
  data['priceChange%'] = line[3]
  data['volume$'] = line[4]
  data['mktcap'] = line[5]
  return data

def toCsvLines(lines, skipHeader = True, displayLines = False):
  rv = []
  if displayLines: print(f'\n{getHeaders()}')
  now = nowStr()
  for line in lines:
    if skipHeader:
      skipHeader = False
      continue
    li = parseLine(line)
    #----------------------------------
    symbol = li['symbol']
    name = li['name']
    price = li['price$']
    priceChangePct = li['priceChange%']
    volume = li['volume$']
    marketCap = li['mktcap']
    #----------------------------------
    rv.append(f'{now},{symbol},{name},{price},{priceChangePct},{volume},{marketCap}')
    if displayLines: print(f'{now},{symbol},{name},{price},{priceChangePct},{volume},{marketCap}')
    #if displayLines: print(f'  [{symbol:<9}  {name:<30}  {price:>14.8f}]     chg:{priceChangePct:>7.2f}%  volume:${volume:>12.2f}  MktCap:{marketCap}')
  return rv

def writeCurrentToFile(f):
  d = getTopCryptos()
  if 'Gainers' in d:
    gainersList = toCsvLines(d['Gainers'])
    writeToFile(f, gainersList)
    if not DEBUG:
      f.flush()


print("======================================================================================================================================================")
print("======================================================================================================================================================")

DATA_SUBFOLDER = 'cryptomarkettoday'
FILE_PREFIX = 'CMT' #'CryptoMarketToday'
SLEEP_SECONDS = 60 * 1

path = f'/Users/michael/data/{DATA_SUBFOLDER}'


# Create CSV file and write out the csv column headers
f, filename, pathname = createFile(path, FILE_PREFIX)

while True:
  writeCurrentToFile(f)
  prt(f'updated {filename}')
  time.sleep(SLEEP_SECONDS)

cleanUp(f)

