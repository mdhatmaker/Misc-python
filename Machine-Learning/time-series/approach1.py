import sys
import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import tensorflow as tf

from sklearn.metrics import mean_squared_error
from math import sqrt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

### https://youtu.be/d4Sn6ny_5LI
### https://www.analyticsvidhya.com/blog/2018/02/time-series-forecasting-methods/


# Step 1 - Import price data
filename = "gold-train.csv"
filepath = os.path.join(SCRIPT_DIR, "..", "data", filename)
df = pd.read_csv(filepath)

df.Timestamp = pd.to_datetime(df.Date,format='%Y/%m/%d')
df.index = df.Timestamp

df.drop(['Date'], axis=1, inplace=True)


# Step 2 - Split into training and testing set
count = df.shape[0]
cutoff = int(0.85 * count)
train = df[0:cutoff]
test = df[cutoff:]


# Step 3a - Naive Forecast
dd = np.asarray(train.Price)
y_hat = test.copy()
y_hat['naive'] = dd[len(dd)-1]  # price of next day = price of previous day
rms = sqrt(mean_squared_error(test.Price, y_hat.naive))
print("Naive RMS: %.2f" % (rms))

# Step 3b - Compute Average
y_hat_avg = test.copy()
y_hat_avg['avg_forecast'] = train['Price'].mean()
rms = sqrt(mean_squared_error(test.Price, y_hat_avg.avg_forecast))
print("Average RMS: %.2f" % (rms))

# Step 3c - Moving Average
#y_hat_avg = test.copy()
y_hat_avg['moving_avg_forecast'] = train['Price'].rolling(60).mean().iloc[-1]
rms = sqrt(mean_squared_error(test.Price, y_hat_avg.moving_avg_forecast))
print("Moving Average RMS: %.2f" % (rms))

# Step 3d - Weighted Moving Average
# i.e. Simple Exponential Smoothing (alpha (a) = smoothing parameter)
# y_hat_tplus1 = a*y[t] + a*(1-a)*y[t-1] + a*(1-a)^2*y[t-2] + ...
# (simplified, recursive)  y_hat(t+1,t) = a*y[t] + (1-a)*y_hat(t,t-1)
# https://www.statsmodels.org/dev/tsa.html
from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
#y_hat_avg = test.copy()
fit2 = SimpleExpSmoothing(np.asarray(train['Price'])).fit(smoothing_level=0.6, optimized=False)
y_hat_avg['SES'] = fit2.forecast(len(test))
rms = sqrt(mean_squared_error(test.Price, y_hat_avg.SES))
print("Simple Exponential Smoothing RMS: %.2f" % (rms))

# Holts Linear Trend - applies exp smoothing to both level and trend
# (can also add 'Seasonality' to Holt) "Holt's Winter Method"
import statsmodels.api as sm
#sm.tsa.seasonal_decompose(train.Price).plot()
#result = sm.tsa.stattools.adfuller(train.Price)
#plt.show()
fit1 = Holt(np.asarray(train['Price'])).fit(smoothing_level=0.3, smoothing_slope=0.1)
y_hat_avg['Holt_linear'] = fit1.forecast(len(test))
rms = sqrt(mean_squared_error(test.Price, y_hat_avg.Holt_linear))
print("Holt Linear RMS: %.2f" % (rms))



### So far, univariate time series (vs multivariate time series)

# Step 3e - Vector Auto Regression (multivariate)

# Step 3f - Recurrent Neural Networks (multivariate)

# Step 3g - LSTM Networks (multivariate)



# Step 3i - ARIMA
#y_hat_avg = test.copy()
#fit1 = sm.tsa.statespace.SARIMAX(train.Price, order=(2,1,4),seasonal_order=(0,1,1,7)).fit()
#y_hat_avg['ARIMA'] = fit1.predict(start="2019-01-01", end="2020-03-02", dynamic=True)
"""fit1 = sm.tsa.statespace.SARIMAX(train.Price, order=(2,1,4)).fit()
y_hat_avg['ARIMA'] = fit1.predict(start="2019-01-01", end="2020-03-02", dynamic=True)
rms = sqrt(mean_squared_error(test.Price, y_hat_avg.ARIMA))
print("ARIMA RMS: %.2f" % (rms))"""







# Step 4 - Plot
plt.figure(figsize=(12,8))
plt.plot(train.index, train['Price'], label='Train')
plt.plot(test.index, test['Price'], label='Test')
plt.plot(y_hat.index, y_hat['naive'], label='Naive Forecast')
plt.plot(y_hat_avg['avg_forecast'], label='Average Forecast')
plt.plot(y_hat_avg['moving_avg_forecast'], label='Moving Average Forecast')
plt.plot(y_hat_avg['SES'], label='SES')
plt.plot(y_hat_avg['Holt_linear'], label='Holt_linear')
#plt.plot(y_hat_avg['ARIMA'], label='ARIMA')


plt.legend(loc='best')
plt.title("Naive Forecast")
plt.show()

# Step 5 - Test Accuracy

