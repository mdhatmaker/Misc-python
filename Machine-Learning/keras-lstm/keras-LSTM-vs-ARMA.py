from __future__ import print_function
from keras.models import Sequential
from keras.layers import Dense, LSTM
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

from statsmodels.tsa.arima_process import arma_generate_sample
# from statsmodels.tsa.arima_model import _arma_predict_out_of_sample
np.random.seed(11111)
nobs = 1000
dates = sm.tsa.datetools.dates_from_range('1980m1', length=nobs)
ar_params=[0.5]
ma_params=[0.5]

def sqerror(predicted,actual):
    return (actual-predicted).pow(2)

tsteps = 1
batch_size = 5
epochs = 20
# number of elements ahead that are used to make the prediction
# lahead = 1

print('Creating Model')
model = Sequential()
model.add(LSTM(10,
               batch_input_shape=(batch_size, tsteps, 1),
               return_sequences=True,
               stateful=False))
model.add(LSTM(10,
               return_sequences=False,
               stateful=True))
model.add(Dense(1))
model.compile(loss='mse', optimizer='rmsprop')

print('Training')
for i in range(epochs):
    print('Epoch', i, '/', epochs)
    y=arma_generate_sample(np.r_[1, -np.array(ar_params)],
                       np.r_[1,  np.array(ma_params)],
                       nsample=nobs,
                       sigma=1)
    y=y/y.std()
    yexp=np.expand_dims(np.expand_dims(y,axis=1),axis=1)
    resexp=np.expand_dims(np.roll(y,shift=-1),axis=1)
    model.fit(yexp,
              resexp,
              batch_size=batch_size,
              verbose=0,
              nb_epoch=1,
              shuffle=False)
    model.reset_states()

# generate unseen one for predicting
y=arma_generate_sample(np.r_[1, -np.array(ar_params)],
                   np.r_[1,  np.array(ma_params)],
                   nsample=nobs,
                   sigma=1)
y=y/y.std()
ys = pd.Series(y, index=dates)
yexp=np.expand_dims(np.expand_dims(y,axis=1),axis=1)

print('LSTM Predicting')
# Shift 1 because the current forecast is for the next point in time
predicted_output = np.roll(model.predict(yexp, batch_size=batch_size),shift=1)
lstmerr=sqerror(predicted_output[:,0],ys)

print('ARMA Model and predicting')
arma_mod = sm.tsa.ARMA(ys, order=(len(ar_params),len(ar_params)))
arma_res = arma_mod.fit(trend='nc', disp=-1)
armapred=arma_res.predict(start=0,end=nobs-1)
# BIGGEST HACK HERE: shift ahead by one
# I'm giving it a perhaps an unfair boost
# I suspect not properly forecasting
# armapred=armapred.shift(-1)
armaerr=sqerror(armapred,ys)

# Zero model
zeroerr=sqerror(np.zeros(armapred.shape),ys)
# Perfect model
perfecterr=sqerror(ys,ys)

print(lstmerr.mean())
print(armaerr.mean())

plot_limit=200
plt.subplot(2,1,1)
plt.plot(yexp[:plot_limit,0,0],'o-',alpha=0.7,label='actual')
plt.plot(predicted_output[:plot_limit,0],'o-',alpha=0.7,label='lstm')
plt.plot(armapred[:plot_limit],'o-',alpha=0.7,label='arma')
plt.legend()
plt.title('time series')
plt.subplot(2,1,2)
plt.plot((perfecterr).cumsum()[:plot_limit],label='perfect')
plt.plot((lstmerr).cumsum()[:plot_limit],label='lstm')
plt.plot((armaerr).cumsum()[:plot_limit],label='arma')
plt.legend()
plt.title('Accumulated square errors (lower is better)')
plt.show()