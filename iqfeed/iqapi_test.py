from iqapi import historicData
from datetime import datetime, timedelta
from dateutil import relativedelta
import pandas as pd
import numpy as np
import sys


mocodes = ['F','G','H','J','K','M','N','Q','U','V','X','Z']


def mYY(symbol_root, dt):
    m = dt.month
    y = dt.year
    return symbol_root + mocodes[m-1] + str(y)[-2:]


# Given a symbol root (ex: "@VX") and a month (1-12) and a year (4-digit)
# Return the future symbols for the front month, one month out, and two months out (tuple of 3 values)
def get_symbols(symbol_root, m, y):
    dt0 = datetime(y, m, 1)
    dt1 = dt0 + relativedelta.relativedelta(months=1)
    dt2 = dt1 + relativedelta.relativedelta(months=1)
    return mYY(symbol_root, dt0), mYY(symbol_root, dt1), mYY(symbol_root, dt2)

        
symbol_root = '@VX'
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
                print dfx.head(1)['DateTime'].values[0], dfx.tail(1)['DateTime'].values[0], symbols[0], symbols[1], symbols[2], dfx.shape[0]
                if dfz.shape[0] == 0:
                    dfz = dfx.copy()
                else:
                    dfz = dfz.append(dfx)


            


sys.exit()





interval_1min = 60
interval_1hour = 3600


# Given month (1-12) and year (4-digit)
def get_historical(root_symbol, m, y):
    dateEnd = datetime(y, m, 28)
    dateStart = dateEnd - timedelta(days=365)       

    mYY = mocodes[m-1] + str(y)[-2:]
    symbolOne = symbol_root + mYY

    iq = historicData(dateStart, dateEnd, interval_1hour)
    symbolOneData = iq.download_symbol(symbolOne)
    return symbolOneData


df = pd.DataFrame()

symbol_root = '@VX'

y1 = 2003
y2 = 2017
for y in range(y1, y2+1):
    for m in range(1, 12+1):
        dfx = get_historical(symbol_root, m, y)
        if dfx.shape[0] == 0:
            df = dfx
        else:
            df = df.append(dfx)

df = df.reset_index()
df['Volume'] = df['Volume'].astype(np.int)
df['oi'] = df['oi'].astype(np.int)
df['sort'] = df['Symbol'].apply(lambda x: x[4:6] + x[3])
df.sort_values(["sort", "DateTime"], ascending=True, inplace=True)
df.drop(['sort'], axis=1, inplace=True)
df.to_csv(symbol_root + ".csv", index=False)


