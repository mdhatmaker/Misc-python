import statsmodels.api as sm  # import model API for statsmodels
import statsmodels
import pandas as pd
import pandas_datareader
import numpy as np
from os.path import join, exists
import sys


#-------------------------------------------------------------------------------
# Add to the PYTHONPATH the folder containing python function modules
li = ["C:\\Users\\Trader\\Dropbox\\alvin\\python", "D:\\Users\\mhatmaker\\Dropbox\\alvin\\python", "/Users/michael/Dropbox/alvin/python"]
sys.path.extend( [path for path in li if exists(path)] )

import f_data_folder
from f_data_folder import *

#-------------------------------------------------------------------------------

# Given a dataframe with a 'Close' (closing price) column
# Return a dataframe with an added 'diff' column that contains the price change in each row
def get_diff_close(df):
    df['prev_close'] = df['Close']
    df['prev_close'] = df.Close.shift(1)
    df['diff'] =  df.Close - df.prev_close
    df.dropna(inplace=True)
    return df

def set_datetime_index(df):
    df = df.set_index(pd.DatetimeIndex(df['DateTime']))
    df.drop(['DateTime'], axis=1, inplace=True)
    return df

"""
start = pandas.datetime(2013,1,1)
end = pandas.datetime.today()

data = DataReader('GOOG','yahoo')
arma =tsa.ARMA(data['Close'], order =(2,2))
results= arma.fit()
results.predict(start=start,end=end)
"""

df = pd.read_csv(join(df_folder, "@ES_continuous.DF.csv") ,date_parser=['DateTime'])
df = get_diff_close(df)
df = set_datetime_index(df)


data = df[['diff']]
d = 1
q = 0
min_aic = -1, 1000000000
for p in range(1, 5):
    #arima = sm.tsa.ARIMAResults(X, order=(p, d, q))
    arima = sm.tsa.ARIMA(data, order=(p, d, q))
    arima = sm.tsa.ARMA(data, order=(p, q))
    #arma_mod20 = sm.tsa.ARMA(X, (2,0)).fit(disp=False)
    #print(arma_mod20.params)
    #print arima.params
    results = arima.fit()
    results.predict(start='2017-08-01', end='2017-08-04')
    print results.summary()
    #print(arima.summary())
    if results.aic < min_aic[1]:
        min_aic = (p, results.aic)

print min_aic        
#t = results.summary().tables
#for i in range(0, len(t[1])):
#    print t[1][i][4]
    
prediction = results.predict(start=0, end=len(data) - 1)
prediction.index = data.index
df['predict'] = prediction
print(prediction)



#arma    = sm.tsa.ARMA(data, order =(4,4));
#arma    = sm.tsa.ARMA(data, order =(1, 1));
#arma    = sm.tsa.ARMA(data, order =(1, 0));
#results = arma.fit( full_output=False, disp=0);
	
#pred = results.predict();
pred = prediction
	
# this is the nsteps ahead predictor function
from statsmodels.tsa.arima_model import _arma_predict_out_of_sample
res = sm.tsa.ARMA(data, (3, 2)).fit(trend="nc")

# get what you need for predicting one-step ahead
params = res.params
residuals = res.resid
p = res.k_ar
q = res.k_ma
k_exog = res.k_exog
k_trend = res.k_trend
steps = 1

_arma_predict_out_of_sample(params, steps, residuals, p, q, k_trend, k_exog, endog=data, exog=None, start=len(data))

