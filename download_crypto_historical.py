import pandas as pd
import numpy as np
import os
import requests
import shutil
#import sys
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#def similar(a,b):
#	return SequenceMatcher(None, a, b).ratio()

def parserA(x):
    return pd.to_datetime(x, format='%Y-%m-%d %I-%p')

def parserZ(x):
    return pd.datetime.strptime(x, '%Y-%m')

def get_data(url):
    r = requests.get(url)
    data = r.text
    #soup = BeautifulSoup(data, "html.parser")
    return data

def download_file(url, folder, deleteFirstLine=True):
    # The downloads from cryptodatadownload.com place a descriptor line as the
    # first row in the text file, so we will delete the first line by default.
    #url = 'https://www.cryptodatadownload.com/cdd/gemini_BTCUSD_1hr.csv'
    #folder = 'data'

    pathname = os.path.join(folder, os.path.basename(url))
    print("Writing output to file '{}'".format(pathname))

    r = requests.get(url, auth=('usrname', 'password'), verify=False, stream=True)
    r.raw.decode_content = True
    with open(pathname, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
    # read the data file in as a list
    fin = open(pathname, "r" )
    data_list = fin.readlines()
    fin.close()
    # remove list items at index 0
    #del data_list[3:5+1]   # delete rows 3-5 (inclusive)
    del data_list[0]
    # write the changed data (list) to a file
    fout = open(pathname, "w")
    fout.writelines(data_list)
    fout.close()
    return

def read_historical(filename, folder, dateParser=None):
    #filename = 'gemini_ETHUSD_1hr.csv'
    #folder = 'data'

    pathname = os.path.join(folder, filename)
    print("Reading from file '{}'".format(pathname))

    df = pd.read_csv(pathname, header=0, parse_dates=['Date'], index_col='Date', squeeze=True, date_parser=dateParser)
    print("Loaded DataFrame from CSV.")
    return df

###############################################################################

folder = 'data'

# NOTE: gemini uses '1hr' as the time period while some of the others use '1h'
url = 'https://www.cryptodatadownload.com/cdd/Coinbase_BTCUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/gemini_ZECUSD_1hr.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Coinbase_LTCUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Kraken_BTCUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Kraken_BTCUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Kraken_ETHUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Kraken_LTCUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Kraken_XRPUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Kraken_BTCEUR_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Kraken_ETHEUR_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Kraken_LTCEUR_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Binance_BTCUSDT_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Binance_ETHUSDT_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Binance_LTCUSDT_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Binance_NEOUSDT_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Bitstamp_BTCUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Bitstamp_ETHUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Bitstamp_LTCUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Bitstamp_XRPUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Bitstamp_BTCEUR_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Bitstamp_ETHEUR_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Bitstamp_LTCEUR_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Bitfinex_BTCUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Bitfinex_ETHUSD_1h.csv'
#url = 'https://www.cryptodatadownload.com/cdd/Bitfinex_LTCUSD_1h.csv'

download_file(url, folder)
#exit()

#df = read_historical('gemini_ZECUSD_1hr.csv', folder)
#df = read_historical('Coinbase_BTCUSD_1h.csv', folder, parserA)
#df = read_historical('Kraken_BTCUSD_1h.csv', folder, parserA)
#df = read_historical('Binance_BTCUSDT_1h.csv', folder, parserA)
filename = os.path.basename(url)
print("Reading {} from folder {}".format(filename, folder))
df = read_historical(filename, folder, parserA)

print(len(df))
print(df.columns)
print(df)

