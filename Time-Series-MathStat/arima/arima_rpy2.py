import rpy2.robjects as R
import rpy2.rinterface as rinterface
from rpy2.robjects.packages import importr
import rpy2.robjects.numpy2ri
from rpy2.robjects.vectors import FloatVector, StrVector
import datetime
import numpy as np
forecast = importr("forecast")
R.r.source("arima-fn.R")

x = np.loadtxt("garan.dat",  skiprows=1)
n = len(x)
m = 10
terms = 4

x = np.insert(x, 10, np.nan) # put in a NaN to see what happens
n += 1

print x

R.r.assign('x',x)
R.r.assign('n',n)
R.r.assign('m',m)
R.r.assign('terms',terms)

R.r('fit = Arima(x=x, order=c(2,0,1), xreg=fourier(1:n,terms,m))')
R.r('f = forecast(fit, h=2*m, xreg=fourier(n+1:(2*m),terms,m))')
res = R.r('forecast_results(f)')
for x in res:
  print x

