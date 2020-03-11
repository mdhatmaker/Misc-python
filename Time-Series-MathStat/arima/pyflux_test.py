import numpy as np
import pandas as pd
import pyflux as pf
from datetime import datetime
import matplotlib.pyplot as plt
#%matplotlib inline

data = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/datasets/sunspot.year.csv')
data.index = data['time'].values

# Model
model = pf.ARIMA(data=data, ar=4, ma=4, target='sunspot.year', family=pf.Normal())

# Fitting the model
x = model.fit("MLE")

# plot with matpltlib
#ax = p1.plot()
#test.plot(ax=ax)
#plt.plot(x.data)
plt.plot(data)
plt.show()
