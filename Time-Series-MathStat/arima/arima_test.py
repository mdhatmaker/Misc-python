from __future__ import print_function
import statsmodels.api as sm  # import model API for statsmodels
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_process import arma_generate_sample
import sys

np.random.seed(12345)


arparams = np.array([.75, -.25])
maparams = np.array([.65, .35])

arparams = np.r_[1, -arparams]
maparams = np.r_[1, maparams]
nobs = 250
y = arma_generate_sample(arparams, maparams, nobs)

dates = sm.tsa.datetools.dates_from_range('1980m1', length=nobs)
y = pd.Series(y, index=dates)
arima = sm.tsa.ARIMA(y, order=(2,0,0))
#results = arima.fit(trend='nc', disp=-1)
#arima.predict(start=y.shape[0], end=y.shape[0])
#arima.predict(start='2017-01-11', end='2017-01-12')
results = arima.fit()
print(results.summary())
#results.predict(start='2017-01-11', end='2017-01-12')
predicted_values = results.predict(start='1999-06-30', end='2002-05-31')   #, typ='levels')
# See the typ keyword of predict in the docstring. It determines whether you get predictions
# in terms of differences or levels. The default is 'linear' differences not levels.



print(predicted_values)

#fig, ax = plt.subplots(figsize=(10,8))
#fig = results.plot_predict(start='1999-06-30', end='2001-05-31', ax=ax)
#legend = ax.legend(loc='upper left')






