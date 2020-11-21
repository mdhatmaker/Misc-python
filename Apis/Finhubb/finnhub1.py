import sys
import requests
import json
#import simplejson as json


api_key = "bs5sakvrh5rajuf8n9lg"
token = "&token=" + api_key


api_root = "https://finnhub.io/api/v1/"
stock_api = api_root + "stock/"
candle_api = stock_api + "candle"
tick_api = stock_api + "tick"
quote_api = api_root + "quote"
profile_api = stock_api + "profile2"


def rget(url):
    r = requests.get(url + token)
    if not r.ok:
        print(r)
        #print(dir(r))
        print("  ERROR: " + r.text)
        return None
    else:
        return r


def get_json(data):
    jsd = str(data).replace("'", "\"")
    return json.loads(jsd)


"""
r = rget(profile_api + "?symbol=AAPL")
#r = rget(profile_api + "?isin=US5949181045")
#r = rget(profile_api + "?cusip=023135106")
data = r.json()
print(data)
print(data['country'])
print(data['currency'])
print(data['exchange'])
print(data['ipo'])
print(data['marketCapitalization'])
print(data['name'])
print(data['shareOutstanding'])
print(data['ticker'])
"""

# OHLC data
r = requests.get(candle_api + '?symbol=AAPL&resolution=1&from=1572651390&to=1572910590')
js = r.json()
print(js)
data = r.json()
status = data['s']
print(status)
sys.exit()
time = data['t']
o = data['o']
h = data['h']
l = data['l']
c = data['c']
volume = data['v']
ohlc = zip(time, o, h, l, c, volume)
for z in ohlc:
    print(z)
sys.exit()

# Tick data
r,data = requests.get(tick_api + '?symbol=AAPL&date=2020-03-25')
print(data)


# Quote data
r, data = requests.get(quote_api + "?symbol=AAPL")
print(data)


