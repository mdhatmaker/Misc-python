from yahoo_finance import Share
from pprint import pprint
#from pandas_datareader import data as dreader
import pandas_datareader as pdr
import pandas as pd
import sys
import urllib as urllib
from os.path import join
from datetime import datetime
import quandl


output_path = r"/Users/michael/Dropbox/MyProjects/python/_data"


symbol = "AAPL"
data = quandl.get("WIKI/"+symbol, start_date="2002-01-01", end_date="2017-08-10")

df = data.loc[:,'Adj. Close':'Adj. Close']
df.rename(columns={'Adj. Close': 'AdjClose'}, inplace=True)
#print(df)

filename = join(output_path, symbol+".csv")
print "Writing output to: '{0}'".format(filename)
df.to_csv(filename)





"""
sys.exit()
aapl = pdr.get_data_yahoo('AAPL')
#ibm = pdr.get_data_yahoo(symbols='IBM', start=datetime(2017,1,1), end=datetime(2017,8,10)) 
#print(ibm['Adj Close'])


sys.exit()
base_url = "http://ichart.finance.yahoo.com/table.csv?s="

def make_url(ticker_symbol):
    return base_url + ticker_symbol

def make_filename(ticker_symbol, directory="S&P"):
    return join(output_path, directory, ticker_symbol + ".csv")

def pull_historical_data(ticker_symbol, directory="S&P"):
    try:
        urllib.urlretrieve(make_url(ticker_symbol), make_filename(ticker_symbol, directory))
    except urllib.ContentTooShortError as e:
        outfile = open(make_filename(ticker_symbol, directory), "w")
        outfile.write(e.content)
        outfile.close()


hist = pull_historical_data('AAPL')

sys.exit()
#symbols = ['GOOG', 'AAPL', 'MMM', 'ACN', 'A', 'ADP']
#pnls = {i:dreader.DataReader(i,'yahoo','1985-01-01','2017-08-10') for i in symbols}
symbols = ['GOOG', 'AAPL']
pnls = {i:dreader.DataReader(i,'yahoo','2017-01-01','2017-08-10') for i in symbols}

# Use .get method to retrieve data in dictionary:
df_goog = pnls.get('GOOG')
print(df_goog.head())


sys.exit()
yahoo = Share('YHOO')
print yahoo.get_open()
print yahoo.get_price()
#print yahoo.get_trade_datetime()

# Refresh data from market
yahoo.refresh()
#print yahoo.get_price()
#print yahoo.get_trade_datetime()

hist = yahoo.get_historical('2014-04-25', '2014-04-29')
print hist
pprint(hist)
"""
