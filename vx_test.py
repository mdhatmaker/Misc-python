import sys
import os
from os import listdir
from os.path import isfile, join
import pandas as pd
import numpy as np
import math

#-----------------------------------------------------------------------------------------------------------------------

execfile("f_folders.py")
execfile("f_date.py")

raw_folder = join(folder, "RAW_DATA")
df_folder = join(folder, "DF_DATA")
project_folder = join(folder, "vix_es")

#-----------------------------------------------------------------------------------------------------------------------

def read_dataframe(pathname):
    df = pd.read_csv(pathname, parse_dates=['DateTime'])
    return df

def get_df_pathname(symbol, resolution='1 Minute'):
    filename = symbol + " " + resolution + ".csv"
    return join(df_folder, filename)

def roll_date(m1, y1):
    #bizday_count = 10                                   # business days before end of month (used for roll)
    #return last_business_day(m1, y1, bizday_count)      # [bizday_count] business days before end of month
    (mn1, yn1) = next_month(m1, y1)    
    xdt = x_weekday_of_month(mn1, yn1, 3, weekdays['Fri'])  # get the 3rd Friday of the (next) month
    xdt -= timedelta(days=30)                               # 30 days previous
    while xdt.weekday() != weekdays['Wed']:                 # find the first Wed on or before this date
        xdt -= timedelta(days=1)
    return xdt
    
def get_roll_dates(m1, y1):
    (mp1, yp1) = prev_month(m1, y1)
    return (roll_date(mp1, yp1), roll_date(m1, y1))
    
################################################################################


print "Use this Python script to test various VIX/ES analytics ideas"
print


project_symbol = "vx"
symbol_root = "@VX"


print "Reading ES data file..."
es_file = "@ES#C 1 Minute.csv"
df = read_dataframe(join(df_folder, es_file))
#mindate = df.DateTime.min()
#maxdate = df.DateTime.max()

print "Reading VIX data fiel..."
vx_file = "vx_continuous.csv"
df_vx = read_dataframe(join(project_folder, vx_file))
#mindate = max(mindate, df_vx.DateTime.min())
#maxdate = min(maxdate, df_vx.DateTime.max())
mindate = df_vx.DateTime.min()
maxdate = df_vx.DateTime.max()

print "Date range: ", mindate.strftime("%Y-%m-%d"), maxdate.strftime("%Y-%m-%d")

# Trim the ES dataframe to match the date range for the VIX dataframe
df = df[df.DateTime >= mindate]
df = df[df.DateTime <= maxdate]

# Create two columns: vix and std
df["vix"] = np.NaN
df["std"] = np.NaN

i = 0

# For each ES data row, find the VIX value to use at that row (and calculate the std)
print "Calculating std",
mod_value = int(df.shape[0] / 100)      # this should allow us to output a dot more or less every 1% completion
for ix,row in df.iterrows():
    if ix % mod_value == 0:
        print ".",
    #dt2 = row.DateTime
    #dt1 = row.DateTime - timedelta(days=5)
    #dfx = df_vx[(df_vx.DateTime >= dt1) & (df_vx.DateTime <= dt2)]
    while i < df_vx.shape[0] and df_vx.DateTime.iloc[i] <= row.DateTime:
        i += 1
    i -= 1
    most_recent_vix = df_vx.Close.iloc[i]
    df.set_value(ix, 'vix', most_recent_vix)
    df.set_value(ix, 'std', round(most_recent_vix / math.sqrt(252), 2))
print

filename = "es_prices.csv"
df.to_csv(join(project_folder, filename), index=False)  #, cols=('A','B','sum'))

print
print "Output to file:", filename
print


print
print "Done."
print



