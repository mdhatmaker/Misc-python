from iqapi import historicData
from datetime import datetime, timedelta
from dateutil import relativedelta
import pandas as pd
from pandas.tseries.offsets import BDay
import numpy as np
import os.path
import math
import sys
"""
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
import lstm, time  # helper libraries
"""

#-------------------------------------------------------------------------------
# Add to the PYTHONPATH the folder containing python function modules
li = ["C:\\Users\\Trader\\Dropbox\\alvin\\python", "D:\\Users\\mhatmaker\\Dropbox\\alvin\\python", "/Users/michael/Dropbox/alvin/python"]
sys.path.extend( [path for path in li if os.path.exists(path)] )

from f_data_folder import *
from f_chart import *
import f_dataframe as fdf

#-------------------------------------------------------------------------------

mocodes = ['F','G','H','J','K','M','N','Q','U','V','X','Z']

interval_1min = 60
interval_1hour = 3600


# Given a symbol root (ex: "@VX") and a datetime object
# Return the mYY futures contract symbol (ex: "@VXM16") 
def mYY(symbol_root, dt):
    m = dt.month
    y = dt.year
    return symbol_root + mocodes[m-1] + str(y)[-2:]


# Given a symbol in XXXmYY format (ex: "@VXM16")
# Return the datetime of the first day of that symbol month
# TODO: For now, we assume a XXXmYY (6-char) future symbol
# TODO: Also, we assume year is >= 2000
def get_symbol_date(symbol):
    m = mocodes.index(symbol[3])+1
    y = 2000 + int(symbol[-2:])
    return datetime(y, m, 1)

    
# Given a symbol root (ex: "@VX") and a month (1-12) and a year (4-digit)
# Return the future symbols for the front month, one month out, and two months out (tuple of 3 values)
def get_symbols(symbol_root, m, y):
    dt0 = datetime(y, m, 1)
    dt1 = dt0 + relativedelta.relativedelta(months=1)
    dt2 = dt1 + relativedelta.relativedelta(months=1)
    return mYY(symbol_root, dt0), mYY(symbol_root, dt1), mYY(symbol_root, dt2)


# Given an IQFeed symbol and the start/end dates and interval in seconds (0=daily) and begin/end filter time ("HHmmSS")
# Return a dataframe containing the historical data for this symbol (using IQFeed)
def get_historical(symbol, dateStart, dateEnd, interval=0, beginFilterTime='', endFilterTime=''):
    iq = historicData(dateStart, dateEnd, interval, beginFilterTime, endFilterTime)
    df = iq.download_symbol(symbol)
    df['Volume'] = df['Volume'].astype(np.int)
    df['oi'] = df['oi'].astype(np.int)
    return df


# Given a contract symbol and date start/end and interval in seconds (0=daily) and begin/end filter time ("HHmmSS")
# Return a dataframe containing the historical data for this contract (using IQFeed)
def get_historical_contract(symbol, dateStart, dateEnd, interval=0, beginFilterTime='', endFilterTime=''):
    df = get_historical(symbol, dateStart, dateEnd, interval, beginFilterTime, endFilterTime)
    df = df.reset_index()                           # initially, the DateTime is the index
    df.sort_values(["DateTime"], ascending=True, inplace=True)
    return df

    
# Given month (1-12) and year (4-digit)
# Return a dataframe containing the historical data for this futures contract (using IQFeed)
def get_historical_future(symbol_root, m, y):
    dateEnd = datetime(y, m, 28)
    dateStart = dateEnd - timedelta(days=365)       
    mYY = mocodes[m-1] + str(y)[-2:]
    symbol = symbol_root + mYY
    #iq = historicData(dateStart, dateEnd, interval_1hour)
    #symbolOneData = iq.download_symbol(symbolOne)
    symbolData = get_historical(symbol, dateStart, dateEnd)
    return symbolData


# Given a symbol root (ex: "@VX") and a starting/ending year (y1/y2)
# create a .CSV file with the symbol root as the name that contains price data for all
#  futures in year range
def create_historical_futures_df(symbol_root, y1, y2):
    df = pd.DataFrame()
    for y in range(y1, y2+1):
        for m in range(1, 12+1):
            dfx = get_historical_future(symbol_root, m, y)            
            if df.shape[0] == 0:
                df = dfx
            else:
                df = df.append(dfx)
    df = df.reset_index()
    #df['Volume'] = df['Volume'].astype(np.int)
    #df['oi'] = df['oi'].astype(np.int)
    df['sort'] = df['Symbol'].apply(lambda x: x[4:6] + x[3])
    df.sort_values(["sort", "DateTime"], ascending=True, inplace=True)
    df.drop(['sort'], axis=1, inplace=True)
    df.to_csv(symbol_root + ".csv", index=False)
    return df


# Given a symbol root (ex: "@VX") and a starting/ending year (y1/y2)
# recreate the functionality of create_historical_futures_df, but ONLY for those symbols that
#  may have updated prices
def update_historical_futures_df(symbol_root, y1, y2):
    raise NotImplementedError
    return


# Given a symbol root (ex: "@VX")
# create a dataframe file containing the contango values (ex: "contango_@VX.csv")
# this file includes "front" contango (1m0 x 1m1), "next" contango (1m1 x 1m2), and the 1x3x2 contango
def create_contango_df(symbol_root):
    df = pd.read_csv(symbol_root + '.csv', parse_dates=True)
    unique = df.Symbol.unique()
    dfz = pd.DataFrame()
    y1 = 2003
    y2 = 2017
    for y in range(y1, y2+1):
        for m in range(1, 12+1):
            symbols = get_symbols(symbol_root, m, y)
            if symbols[0] in unique and symbols[1] in unique and symbols[2] in unique:
                df0 = df[df.Symbol == symbols[0]]
                df1 = df[df.Symbol == symbols[1]]
                df2 = df[df.Symbol == symbols[2]]
                dfx = pd.merge(df0, df1, on="DateTime")
                dfx = pd.merge(dfx, df2, on="DateTime")
                if dfx.shape[0] > 0:
                    print(dfx.head(1)['DateTime'].values[0], dfx.tail(1)['DateTime'].values[0], symbols[0], symbols[1], symbols[2], dfx.shape[0])
                    if dfz.shape[0] == 0:
                        dfz = dfx.copy()
                    else:
                        dfz = dfz.append(dfx)

    dfz.drop(['Open_x','High_x','Low_x','Volume_x','oi_x','Open_y','High_y','Low_y','Volume_y','oi_y','Open','High','Low','Volume','oi'], axis=1, inplace=True)
    dfz.rename(columns={'Close_x':'Close0', 'Symbol_x':'Symbol', 'Close_y':'Close1', 'Symbol_y':'Symbol1', 'Close':'Close2', 'Symbol':'Symbol2'}, inplace=True)
    dfz['contango'] = dfz.Close1 - dfz.Close0
    dfz['contango2'] = dfz.Close2 - dfz.Close1
    dfz['contango1x3x2'] = (2 * dfz.contango2) - dfz.contango
    dfz.contango = dfz.contango.round(2)
    dfz.contango2 = dfz.contango2.round(2)
    dfz.contango1x3x2 = dfz.contango1x3x2.round(2)
    filename = "contango_{0}.raw.DF.csv".format(symbol_root)
    dfz.to_csv(filename, index=False)
    return dfz


# Given a datetime
# Return the datetime of the third Friday of that month
def third_friday(dt):
    dtx = dt.replace(day=1)
    if dtx.weekday() == 4:                  # weekday 4 is FRIDAY
        count = 1
    else:
        count = 0
    while count < 3:
        dtx += timedelta(days=1)
        if dtx.weekday() == 4:
            count += 1
    return dtx


# The Final Settlement Date for a contract with the "VX" ticker symbol is on the Wednesday
# that is 30 days prior to the third Friday of the calendar month immediately following the
# month in which the contract expires.
# http://cfe.cboe.com/cfe-products/vx-cboe-volatility-index-vix-futures/contract-specifications
def get_final_settlement_VX(symbol):
    dt = get_symbol_date(symbol)
    dt_nextmonth = dt + relativedelta.relativedelta(months=1)
    dt_thirdfri = third_friday(dt_nextmonth)
    dt = dt_thirdfri - timedelta(days=30)
    while dt.weekday() != 2:                # weekday 2 is WEDNESDAY
        dt -= timedelta(days=1)
    return dt.replace(hour=8, minute=0, second=0)       # 8am? (TODO)

# Given a VX future symbol (ex: "@VXmYY")
# Return the roll date for this VX future
def get_roll_date_VX(symbol):
    return get_final_settlement_VX(symbol) - BDay(1)


# Given an input dataframe filename (that has a 'DateTime' and a 'Symbol' column) and a roll function
# create a dataframe with the given output filename with the correct continuous front-month contracts
def create_continuous_df(input_filename, output_filename, fn_roll_date):
    # Read in the continuous futures file (ex: 'contango_@VX.raw.DF.csv')
    df = pd.read_csv(input_filename, parse_dates=['DateTime'])

    # We will build a new DataFrame that has the rows for which the front-month contract is correct
    # (check roll dates)
    dfz = pd.DataFrame()

    # The dataframe should be sorted by Symbol-then-Datetime, so these unique Symbols should be sorted also
    unique = df.Symbol.unique()

    dt1 = df.DateTime.min()
    for symbol in unique:
        roll_date = fn_roll_date(symbol)
        dfx = df[(df.DateTime >= dt1) & (df.DateTime < roll_date) & (df.Symbol==symbol)]
        if dfz.shape[0] == 0:
            dfz = dfx.copy()
        else:
            dfz = dfz.append(dfx)
        #print symbol, dt1, roll_date
        dt1 = roll_date
    print()
    print("Rows in RAW: {0}    Rows in CONTINUOUS: {1}".format(df.shape[0], dfz.shape[0]))

    # No longer RAW...
    # We now have a file in which the dates have the correct front-month contract (ex: 'contango_@VX.DF.csv')
    dfz.to_csv(output_filename, index=False)
    print("Output to '{0}'".format(output_filename))
    return dfz


# Given a full dataset and a subset of the full dataset
# Return a list of df_subset rows where the rows are contiguous ranges
def get_ranges_df(df_full, df_subset):
    df_rows = []
    dt1 = None
    dt2 = None
    for ix,r in df_subset.iterrows():
        if dt1 == None:
            dt1 = r.DateTime
        else:   # dt2 == None:
            dt2 = r.DateTime
            
        if dt1 != None and dt2 != None:
            dfx = df_full[(df_full.DateTime >= dt1) & (df_full.DateTime <= dt2)]
            dfy = df_subset[(df_subset.DateTime >= dt1) & (df_subset.DateTime <= dt2)]
            nx = dfx.shape[0]
            ny = dfy.shape[0]
            if nx == ny:
                pass
            else:
                df_rows.append(dfy.iloc[0:dfy.shape[0]-1].copy())
                dt1 = dt2
                dt2 = None
    if dt1 != None and dt2 == None:
        df_rows.append(df_subset[df_subset.DateTime >= dt1])
    return df_rows
                

# For the given date range (defaults to 2003-til-current) calculate the ES Quartiles using daily VIX and ES data
def get_es_quartiles(dt1=datetime(2003,1,1), dt2=datetime.now()):
    df_vix = get_historical_contract("VIX.XO", dt1, dt2)
    df_es = get_historical_contract("@ES#", dt1, dt2)
    df = pd.merge(df_es, df_vix, on=["DateTime"], suffixes=('_ES','_VIX'))
    df['std'] = df.Close_VIX / math.sqrt(252)
    df['Qd4'] = (df.Close_ES - 4 * (df['std']/100.0*df.Close_ES/4.0)).round(2)
    df['Qd3'] = (df.Close_ES - 3 * (df['std']/100.0*df.Close_ES/4.0)).round(2)
    df['Qd2'] = (df.Close_ES - 2 * (df['std']/100.0*df.Close_ES/4.0)).round(2)
    df['Qd1'] = (df.Close_ES - 1 * (df['std']/100.0*df.Close_ES/4.0)).round(2)
    df['Qunch'] = df.Close_ES
    df['Qu1'] = (df.Close_ES + 1 * (df['std']/100.0*df.Close_ES/4.0)).round(2)
    df['Qu2'] = (df.Close_ES + 2 * (df['std']/100.0*df.Close_ES/4.0)).round(2)
    df['Qu3'] = (df.Close_ES + 3 * (df['std']/100.0*df.Close_ES/4.0)).round(2)
    df['Qu4'] = (df.Close_ES + 4 * (df['std']/100.0*df.Close_ES/4.0)).round(2)
    df.loc[:,'Qd4':'Qu4'] = df.loc[:,'Qd4':'Qu4'].shift(1)
    df.drop(0,inplace = True)                               # remove the first row (which contains NaN after shift)
    return df

# For the given date range (defaults to 2003-til-current) calculate the ES Quartiles using daily VIX and ES data
def get_vix_quartiles(dt1=datetime(2003,1,1), dt2=datetime.now()):
    df_vvix = get_historical_contract("VVIX.XO", dt1, dt2)
    df_vix = get_historical_contract("VIX.XO", dt1, dt2)
    df = pd.merge(df_vix, df_vvix, on=["DateTime"], suffixes=('_VIX','_VVIX'))
    df['std'] = df.Close_VVIX / math.sqrt(252)
    df['Qd4'] = (df.Close_VIX - 4 * (df['std']/100.0*df.Close_VIX/4.0)).round(2)
    df['Qd3'] = (df.Close_VIX - 3 * (df['std']/100.0*df.Close_VIX/4.0)).round(2)
    df['Qd2'] = (df.Close_VIX - 2 * (df['std']/100.0*df.Close_VIX/4.0)).round(2)
    df['Qd1'] = (df.Close_VIX - 1 * (df['std']/100.0*df.Close_VIX/4.0)).round(2)
    df['Qunch'] = df.Close_VIX
    df['Qu1'] = (df.Close_VIX + 1 * (df['std']/100.0*df.Close_VIX/4.0)).round(2)
    df['Qu2'] = (df.Close_VIX + 2 * (df['std']/100.0*df.Close_VIX/4.0)).round(2)
    df['Qu3'] = (df.Close_VIX + 3 * (df['std']/100.0*df.Close_VIX/4.0)).round(2)
    df['Qu4'] = (df.Close_VIX + 4 * (df['std']/100.0*df.Close_VIX/4.0)).round(2)
    df.loc[:,'Qd4':'Qu4'] = df.loc[:,'Qd4':'Qu4'].shift(1)
    df.drop(0,inplace = True)                               # remove the first row (which contains NaN after shift)
    return df

# Given a dataframe of Quartiles and a dataframe of 1-minute OHLC summary data
# Return a dataframe of Quartile Hits (0 or 1)
def get_quartile_hits(dfq, df_ohlc):
    df = pd.merge(dfq, df_ohlc, on='DateTime')

    df['d4'] = df.Low<=df.Qd4
    df['d3'] = df.Low<=df.Qd3
    df['d2'] = df.Low<=df.Qd2
    df['d1'] = df.Low<=df.Qd1
    df['unch'] = (((df.Open<=df.Qunch)&(df.High>=df.Qunch)) | ((df.Open>=df.Qunch)&(df.Low<=df.Qunch)))
    df['u1'] = df.High>=df.Qu1
    df['u2'] = df.High>=df.Qu2
    df['u3'] = df.High>=df.Qu3
    df['u4'] = df.High>=df.Qu4

    df['d4'] = df['d4'].astype('int')
    df['d3'] = df['d3'].astype('int')
    df['d2'] = df['d2'].astype('int')
    df['d1'] = df['d1'].astype('int')
    df['unch'] = df['unch'].astype('int')
    df['u1'] = df['u1'].astype('int')
    df['u2'] = df['u2'].astype('int')
    df['u3'] = df['u3'].astype('int')
    df['u4'] = df['u4'].astype('int')

    dfz = df[['DateTime','d4','d3','d2','d1','unch','u1','u2','u3','u4']].copy()
    return dfz

def get_hit_ratios(df_vx, df_hit, lookback=5):
    df = pd.merge(df_vx, df_hit, on='DateTime')
    df['hr_d4'] = df.d4.rolling(lookback).mean()
    df['hr_d3'] = df.d3.rolling(lookback).mean()
    df['hr_d2'] = df.d2.rolling(lookback).mean()
    df['hr_d1'] = df.d1.rolling(lookback).mean()
    df['hr_unch'] = df.unch.rolling(lookback).mean()
    df['hr_u1'] = df.u1.rolling(lookback).mean()
    df['hr_u2'] = df.u2.rolling(lookback).mean()
    df['hr_u3'] = df.u3.rolling(lookback).mean()
    df['hr_u4'] = df.u4.rolling(lookback).mean()

    dfz = df[['DateTime','contango','d4','d3','d2','d1','unch','u1','u2','u3','u4','hr_d4','hr_d3','hr_d2','hr_d1','hr_unch','hr_u1','hr_u2','hr_u3','hr_u4']].copy()
    dfz.dropna(inplace=True)
    return dfz

# Given a dataframe of 1-minute data, calculate the Open,High,Low,Close for each day
def get_ohlc(df):
    df['just_date'] = df['DateTime'].dt.date
    unique_dates = df['just_date'].unique()
    rows = []
    for dt in unique_dates:
        dt1 = datetime(dt.year, dt.month, dt.day, 8, 30, 0)
        dt2 = datetime(dt.year, dt.month, dt.day, 15, 0, 0)
        dfx = df[(df.DateTime>dt1) & (df.DateTime<=dt2)]
        xopen = dfx.iloc[0]['Open']
        xhigh = dfx.High.max()
        xlow = dfx.Low.min()
        xclose = dfx.iloc[dfx.shape[0]-1]['Close']
        rows.append([dt, xopen, xhigh, xlow, xclose])
    return pd.DataFrame(rows, columns=['DateTime', 'Open', 'High', 'Low', 'Close'])
    
        
def show_contango_chart(df):
    # CREATE THE CHART
    lines = []
    lines.append(get_chart_line(df, 'contango1x3x2', line_color='rgb(255,0,0)')) #, line_dash='dot'))
    lines.append(get_chart_line(df, 'contango', line_color='rgb(0,0,255)')) #, line_dash='dot'))
    lines.append(get_chart_line(df, 'Close0', line_name='VX'))

    # Highlight the negative ranges on the chart
    #for dfx in rows:
    #    lines.append(get_chart_line(dfx, 'contango1x3x2', line_color='rgb(255,0,0)', line_width=3))

    show_chart(lines, 'VIX_contango')
    return

    
################################################################################
################################################################################
################################################################################


dt1 = datetime(2003, 1, 1)
dt2 = datetime.now()

#df = get_historical("QCL#", dt1, dt2)
#df = get_historical("@VX#", dt1, dt2)
#print df


# Download all historical ES futures and output to file '@ES.csv'
#df = create_historical_futures_df("@ES", 2003, 2017)

# Retrieve the 1-minute ES data and output to file '@ES_session_1min.DF.csv'
#df = get_historical_contract("@ES#", dt1, dt2, interval_1min, "083000", "150000")   # 8:30am to 3:00pm
#filename = "@ES_session_1min.DF.csv"
#df.to_csv(filename, index=False)
#print("Output 1-minute data to '{0}'".format(filename))

# Read the 1-minute ES data from file '@ES_session_1min.DF.csv' and output OHLC summary to file '@ES_session_ohlc.DF.csv'
#df_1min = pd.read_csv("@ES_session_1min.DF.csv", parse_dates=['DateTime'])
#df_ohlc = get_ohlc(df_1min)
#filename = "@ES_session_ohlc.DF.csv"
#df_ohlc.to_csv(filename, index=False)
#print("Output OHLC summary data to '{0}'".format(filename))

# Request the daily VIX.XO and @ES data and output the Quartile values to '@ES_quartiles.DF.csv'
#dfq = get_es_quartiles()
#filename = "@ES_quartiles.DF.csv"
#dfq.to_csv(filename, index=False)
#print("Output quartiles to '{0}'".format(filename))
                 
dfq = pd.read_csv("@ES_quartiles.DF.csv", parse_dates=['DateTime'])
df_ohlc = pd.read_csv("@ES_session_ohlc.DF.csv", parse_dates=['DateTime'])

# Calculate the Quartile Hits from Quartiles and OHLC summary data and output to '@ES_quartile_hits.DF.csv'
#dfz = get_quartile_hits(dfq, df_ohlc)
#filename = "@ES_quartile_hits.DF.csv"
#dfz.to_csv(filename, index=False)
#print("Output quartile hits to '{0}'".format(filename))

df_hit = pd.read_csv("@ES_quartile_hits.DF.csv", parse_dates=['DateTime'])
df_vx = pd.read_csv("contango_@VX.DF.csv", parse_dates=['DateTime'])

# Calculate the Quartile Hit Ratios from Quartile Hits and VIX Contango data and output to '@ES_quartile_hit_ratios.DF.csv' 
#df_hr = get_hit_ratios(df_vx, df_hit, 5)
#filename = "@ES_quartile_hit_ratios.DF.csv"
#df_hr.to_csv(filename, index=False)
#print("Output quartile hit ratios to '{0}'".format(filename))

df_hr = pd.read_csv("@ES_quartile_hit_ratios.DF.csv", parse_dates=['DateTime'])


df = get_vix_quartiles()
i1 = df.columns.get_loc('Qd4')
i2 = df.columns.get_loc('Qu4')
cols = ['DateTime']
cols.extend(df.columns.values[i1:i2+1])
#df_vix = df.iloc[:,i1:i2]
df_vix = df.loc[:,cols]
#print(df_vix)
filename = "@VIX_quartiles.DF.csv"
df_vix.to_csv(filename, index=False)
print("Output quartiles to '{0}'".format(filename))



sys.exit()


"""
#seq_len = 50

print('> Loading data... ')

seq_len = 40
prediction_len = 20
filename = "@ES_quartile_hit_ratios.DF.csv"
#df = fdf.read_dataframe(join(data_folder, "vix_es", "es_vix_daily_summary.DF.csv"))
df = pd.read_csv(filename, parse_dates=['DateTime'])
input_data_filename = 'NN_INPUT.csv'
f = open(input_data_filename, 'w')
for ix,r in df.iterrows():
    # We need to adjust this so there are no ZEROS in the data
    f.write("{0},{1},{2},{3},{4},{5},{6}\n".format(r['DateTime'],r['contango'],r['d4'],r['d3'],r['d2'],r['d1'],r['unch']))
f.close()

sys.exit()
"""

global_start_time = time.time()
epochs  = 1

seq_len  = 50
prediction_len = 50
input_data_filename = 'sp500.csv'

X_train, y_train, X_test, y_test = lstm.load_data(input_data_filename, seq_len, True)

print("TRAINING ROWS: {0}     TEST ROWS: {1}".format(X_train.shape[0], X_test.shape[0]))

print('> Data Loaded. Compiling...')

#model = lstm.build_model([1, 50, 100, 1])
# Don't hardcode "50" but use seq_len instead because seq_len is the lookback length
# original model layers were [1, 50, 100, 1]
model = lstm.build_model([1, seq_len, seq_len*2, 1])

model.fit(
    X_train,
    y_train,
    batch_size=512,
    nb_epoch=epochs,
    validation_split=0.05)

# For now, set our prediction length to our (input) sequence length
#prediction_len = seq_len

predictions = lstm.predict_sequences_multiple(model, X_test, seq_len, prediction_len)
#predicted = lstm.predict_sequence_full(model, X_test, seq_len)
#predicted = lstm.predict_point_by_point(model, X_test)        

print('Training duration (s) : ', time.time() - global_start_time)

#lstm.plot_results_multiple(predictions, y_test, prediction_len)

predict = lstm.predict_point_by_point(model, X_test)
lstm.plot_results(predict, y_test)


sys.exit()





symbol_root = '@VX'

# Create the '@VX.csv' file containing futures prices for the given year range
#create_historical_futures_df(symbol_root, 2003, 2017)

# Using the '@VX.csv' data file, create 'contango_@VX.raw.DF.csv' containing contango data
#dfz = create_contango_df(symbol_root)

# From the raw data, create the continuous contract contango file
input_filename = "contango_{0}.raw.DF.csv".format(symbol_root)
continuous_filename = "contango_{0}.DF.csv".format(symbol_root)
#dfz = create_continuous_df(input_filename, continuous_filename, get_roll_date_VX)




# Read in the 'contango_@VX.DF.csv' file
df = pd.read_csv(continuous_filename, parse_dates=['DateTime'])

#show_contango_chart(df)


"""
# Get datapoints where the 1x3x2 contango is negative
df_neg = df[df['contango1x3x2']<0]
rows = get_ranges_df(df, df_neg)            # get contiguous date ranges of the negative 1x3x2 values

# Find the slope leading into (before) a point where 1x3x2 is negative
# vs leading out (after)
li = []
for dfx in rows:
    dt1 = dfx.iloc[0].DateTime
    dt2 = dfx.iloc[dfx.shape[0]-1].DateTime
    #print dt1.strftime('%Y-%m-%d'), dt2.strftime('%Y-%m-%d'),
    ix = df[df.DateTime==dt1].index.values[0]
    length = 10
    ix1 = max(ix-length,0)
    ix2 = min(ix+length,df.shape[0]-1)
    dfy = df[ix1:ix]
    #print dfy.shape
    z = np.polyfit(dfy.index, dfy.Close0, 1)
    slope1 = round(z[0], 4)
    #print "{0:7.4f}".format(slope1),
    # f = np.poly1d(z)
    dfy = df[ix:ix2]
    if dfy.shape[0]==0:
        break
    z = np.polyfit(dfy.index, dfy.Close0, 1)
    slope2 = round(z[0], 4)
    #print "{0:7.4f}".format(slope2)
    li.append((slope1, slope2))
slopes = np.array(li)
s1 = abs(slopes[:,0])
s2 = abs(slopes[:,1])
print s1.mean()
print s2.mean()
"""














