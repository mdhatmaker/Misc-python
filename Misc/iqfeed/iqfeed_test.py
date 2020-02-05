# Use the following snippet to obtain list of Bar objects.
import pytz
from iqfeed import get_bars
import sys


seconds_1min = 60
seconds_1hour = 60 * 60

mocodes = ['F','G','H','J','K','M','N','Q','U','V','X','Z']



# Use IQFeed API to get historical data for a given instrument, date range, etc.
def get_historical(instrument, start_date, end_date, seconds_per_bar=seconds_1hour, tz = pytz.timezone('US/Central')):
    iqfeed_host = 'localhost'
    iqfeed_port = 9100
    return get_bars(instrument, start_date, end_date, tz, seconds_per_bar, iqfeed_host, iqfeed_port)

# Print OHLC and volume for a given historical data bar
def print_bar(bars, i):
    b = bars[i]
    dt = b[0]
    bo = b[1]
    bh = b[2]
    bl = b[3]
    bc = b[4]
    bv = b[5]
    print "{0}   O:{1:7.2f} H:{2:7.2f} L:{3:7.2f} C:{4:7.2f}   volume:{5}".format(dt, bo, bh, bl, bc, bv)
    return

# Print the first [count] bars in the given list (default=10)
def print_bars(bars, count=10):
    print("{0} bars".format(len(bars)))
    for i in range(1, count+1):
        print_bar(bars, i)
    print("...")
    for i in range(len(bars)-count-1,len(bars)-1):
        print_bar(bars, i)
    return

def get_historical_for_year(instrument, year, seconds_per_bar=seconds_1hour):
    y_str = str(year)
    d1_str = y_str + "0101"
    d2_str = y_str + "1231"
    return get_historical(instrument, d1_str, d2_str, seconds_per_bar)
    
def get_historical_futures_for_year(symbol_root, year, seconds_per_bar=seconds_1hour):
    d = {}
    for m in range(1, 12+1):
        mc = mocodes[m-1]
        YY = str(year)[-2:]
        mYY = mc + YY
        symbol = symbol_root + mYY
        print symbol
        y_str = str(year)
        d1_str = y_str + "0101"
        d2_str = y_str + "1231"
        hist = get_historical(symbol, d1_str, d2_str, seconds_per_bar)
        print(len(hist))
        d[symbol] = hist
    return d
    
    
################################################################################


"""
bars = get_historical_for_year('VIX.IO', 2017)
print_bars(bars)
sys.exit()


##### RETRIEVE EVERY MONTH OF DATA FOR A GIVEN YEAR RANGE #####
years = (2010, 2017)
for y in range(years[0], years[1]+1):
    d = get_historical_futures_for_year("@VX", y)
    sys.exit()
    
sys.exit()


##### MODIFIED TO USE A FUNCTION TO RETRIEVE HISTORICAL DATA #####
bars = get_historical('GLD', '20150101', '20151231')
print_bars(bars)
sys.exit()
"""

##### ORIGINAL CODE TO RETRIEVE HISTORICAL 'GLD' DATA USING IQFEED #####
instrument = 'GLD'
start_date = '20150101'
end_date = '20151231'
tz = pytz.timezone('US/Eastern')
seconds_per_bar = seconds_1hour
iqfeed_host = 'localhost'
iqfeed_port = 9100

bars = get_bars(instrument, start_date, end_date, tz, seconds_per_bar, iqfeed_host, iqfeed_port)
print "'bars' has length {0}".format(len(bars)) 
b = bars[0]


# The Bar object is a named tuple which holds the Open, High, Low, Close and Volume
# values for the given time:
# IQFeedBar(datetime=datetime.datetime(2015, 1, 2, 9, 30, tzinfo=<DstTzInfo 'US/Eastern' EST-1 day, 19:00:00 STD>), open=112.46, high=112.46, low=112.45, close=112.46, volume=192104)







