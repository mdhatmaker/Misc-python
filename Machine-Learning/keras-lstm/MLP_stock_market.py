# To improve the performance of the MLP, the data is first scaled so that both the input
# and output data have mean 0 and variance 1. This can be accomplished as follows (take
# note that "Date Value" is in column index 1 and "High" is in column index 4):
import numpy as np
from TFANN import MLPR
import matplotlib.pyplot as mpl
from sklearn.preprocessing import scale

pth = filePath + 'yahoostock.csv'
A = np.loadtxt(pth, delimeter=",", skiprows=1, usecols=(1,4))
A = scale(A)
# y is the dependent variable
y = A[:, 1].reshape(-1, 1)
# A contains the independent variable
A = A[:, 0].reshape(-1, 1)
# Plot the high value of the stock price
mpl.plot(A[:, 0], y[:, 0])
mpl.show()
