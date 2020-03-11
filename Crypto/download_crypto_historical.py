import pandas as pd
import numpy as np
import os
import requests
import shutil
#import sys
from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

pd.options.display.float_format = '{:.2f}'.format   # round pandas float numbers to 2 decimal places

#def similar(a,b):
#	return SequenceMatcher(None, a, b).ratio()

def parserDateTime(x):
    return pd.to_datetime(x, format='%Y-%m-%d %I-%p')

def parserDateOnly(x):
    return pd.to_datetime(x, format='%Y-%m-%d')

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

def get_crypto_historical_filename(exch, symbol, denom, period='d', year=''):
    # NOTE: gemini uses '1hr' as the time period while some of the others use '1h'
    #exch = "Coinbase"   # Coinbase, gemini, Kraken, Binance, Bitstamp, Bitfinex, Cexio, Itbit, Poloniex 
    #period = "d"        # d, 1h, 1min
    #symbol = "BTC"      # BTC, ETH, LTC ZEC, etc...
    #denom = "USD"       # USD, USDT, etc...
    #year = "_2018"      # '1min' period requires a year

    # gemini: BTCUSD, ZECUSD
    # Coinbase: BTCUSD, LTCUSD, 
    # Kraken: BTCUSD, ETHUSD, LTCUSD, XRPUSD, BTCEUR, ETHEUR, LTCEUR
    # Binance: BTCUSDT, ETHUSDT, LTCUSDT, NEOUSDT
    # Bitstamp: BTCUSD, ETHUSD, BTCEUR, ETHEUR, ...
    # Bitfinex: BTCUSD, ETHUSD, LTCUSD, XRPUSD, BTCEUR, ETHEUR, LTCEUR, XRPEUR
    # Cexio: BTCUSD, ETHUSD
    # Itbit: BTCUSD
    # Poloniex: BTCUSD, ETHUSD, LTCUSD, BCHUSD, XMRUSD, DASHUSD, ETCUSD

    if exch == "gemini" and period == "1h": period = "1hr"
    if exch == "Binance" and denom == "USD": denom = "USDT"
    if period != "1min": year = ""

    return exch + '_' + symbol + denom + year + '_' + period + '.csv'

def get_cryptodatadownload_url(filename):
    return 'https://www.cryptodatadownload.com/cdd/' + filename

def df_reverse_row_order(df):
    return df.iloc[::-1]

def add_all_EMAs(df, in_colname):
    add_EMA(df, in_colname, 5, 'ema5')      # 5-day EMA = strong momentum
    add_EMA(df, in_colname, 10, 'ema10')    # 10-day EMA = short term trend
    add_EMA(df, in_colname, 20, 'ema20')    # 20-day EMA = pullback support
    add_EMA(df, in_colname, 50, 'ema50')    # 50-day EMA = uptrend defense line
    add_EMA(df, in_colname, 100, 'ema100')  # 100-day EMA = big price dip
    #add_EMA(df, in_colname, 200, 'ema200')  # 200-day EMA = bull's last stand in uptrend, bear's last stand in downtrend
    #add_EMA(df, in_colname, 250, 'ema250')  # 250-day EMA = value zone
    return

def add_EMA(df, in_colname, span=10, out_colname='ema'):
    #df[out_colname] = df[[in_colname]].rolling(window=span, min_periods=span).mean() #[:span]
    #df.dropna(inplace=True)
    #df[out_colname] = df[out_colname].ewm(span=span, adjust=False).mean()
    df[out_colname] = pd.Series.ewm(df['Open'], span=span).mean()
    return

def add_all_momentums(df, in_colname):
    add_momentum(df, in_colname, 5, 'momentum5')
    add_momentum(df, in_colname, 10, 'momentum10')
    add_momentum(df, in_colname, 20, 'momentum20')
    return

def add_momentum(df, in_colname, span, out_colname):
    df[out_colname] = df[in_colname].shift(span)
    df[out_colname] = df[in_colname] / df[out_colname]
    return

###############################################################################

folder = 'data'

"""
filename = get_crypto_historical_filename('Coinbase', 'BTC', 'USD')
url = get_cryptodatadownload_url(filename)

#download_file(url, folder)
#exit()

#df = read_historical('gemini_ZECUSD_1hr.csv', folder)
#df = read_historical('Coinbase_BTCUSD_1h.csv', folder, parserA)
#df = read_historical('Kraken_BTCUSD_1h.csv', folder, parserA)
#df = read_historical('Binance_BTCUSDT_1h.csv', folder, parserA)
#filename = os.path.basename(url)
print("Reading {} from folder {}".format(filename, folder))
df = read_historical(filename, folder, parserDateOnly)
#df = read_historical(filename, folder, parserDateTime)

# Reverse row order
df = df_reverse_row_order(df)

df['avg'] = df[['Open', 'High', 'Low', 'Close']].mean(axis=1)

#add_EMA(df, 'Open', 5, 'ema5')
#add_EMA(df, 'Open', 10, 'ema10')
#add_all_EMAs(df, 'avg')
add_all_EMAs(df, 'avg')
add_all_momentums(df, 'avg')

df['signal'] = df['avg'] > df['ema20']

#print(len(df))
#print(df.columns)
#print(df.dtypes)
#print(df[['avg', 'momentum5', 'momentum10', 'momentum20', 'ema5', 'ema10', 'ema20', 'ema50', 'ema100']])
print(df)


print(df.tail(50))
"""