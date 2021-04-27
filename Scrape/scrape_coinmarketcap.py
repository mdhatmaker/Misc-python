import sys
import requests
from bs4 import BeautifulSoup
import json
import time
#from datetime import datetime
import os


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

def printIt(dictList, header):
  print('\n', header)
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
    print(f'  [{symbol:<9}  {name:<30}  {price:>14.8f}]     1h:{priceChange1h:>7.2f}%  24h:{priceChange24h:>7.2f}%  7d:{priceChange7d:>7.2f}%  30d:{priceChange30d:>7.2f}%  vol24h:{volume24h:>12.2f}')
    
def getHeaders():
  return 'timeGMT,symbol,name,price$,priceChange1h%,priceChange24h%,priceChange7d%,priceChange30d%,volume24h$'

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

def getGainersLosers():
  URL = 'https://coinmarketcap.com/gainers-losers/'
  soup = getSoup(URL)
  data = getData(soup)
  gainersLosers = data['props']['initialState']['cryptocurrency']['gainersLosers']
  gainers = gainersLosers['gainers']
  losers = gainersLosers['losers']
  return (gainers, losers)

def nowStr():
  return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())  # time.localtime())

def nowFilename():
  now = nowStr()
  now = now.replace(':', '-')
  now = now.replace(' ', '-')
  return 'crypto_gainers-' + now + '.csv'

def createFile(path):
  filename = nowFilename()
  pathname = os.path.join(path, filename)
  f = open(pathname, 'w')
  f.write(getHeaders() + '\n')
  print(f'>>> Created file "{pathname}"')
  return f

def cleanUp(f):
  f.close()

def writeToFile(f, outputList):
  for li in outputList:
    f.write(li + '\n')

def writeCurrentToFile(f):
  gainers, losers = getGainersLosers()
  gainList = toCsvLines(gainers)
  writeToFile(f, gainList)
  f.flush()

def demo():
  gainers, losers = getGainersLosers()
  printIt(gainers, "--- GAINERS (ranked by 24h) ---")
  printIt(losers, "--- LOSERS (ranked by 24h) ---")
  gainList = toCsvLines(gainers)
  loseList = toCsvLines(losers)
  print('\n   GAINERS (ranked by 24h)\n', getHeaders(), '\n\n', gainList, '\n')
  print('\n   LOSERS (ranked by 24h)\n', getHeaders(), '\n\n', loseList, '\n')


path = '/Users/michael/data/crypto_gainers'

# Create CSV file and write out the csv column headers
f = createFile(path)

while True:
  writeCurrentToFile(f)
  print(f'{nowStr()}  updated')
  time.sleep(60)

cleanUp(f)



"""     CODE GRAVEYARD
URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    print(job_elem, end='\n'*2)

for job_elem in job_elems:
    # Each job_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    #print(title_elem)
    #print(company_elem)
    #print(location_elem)
    if None in (title_elem, company_elem, location_elem):
        continue
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()

python_jobs = results.find_all('h2', string='Python Developer')
"""
