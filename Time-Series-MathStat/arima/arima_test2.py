import warnings
import itertools
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from pylab import rcParams
plt.style.use('fivethirtyeight')

# https://www.digitalocean.com/community/tutorials/a-guide-to-time-series-forecasting-with-arima-in-python-3

plot = False    # turn on/off the plotting (for testing)


data = sm.datasets.co2.load_pandas()
y = data.data

# The 'MS' string groups the data in buckets by start of the month
y = y['co2'].resample('MS').mean()

# The term bfill means that we use the value before filling in missing values
y = y.fillna(y.bfill())

print(y)

y.plot(figsize=(15, 6))
if plot: plt.show()

# Define the p, d and q parameters to take any value between 0 and 2
p = d = q = range(0, 2)

# Generate all different combinations of p, q and q triplets
pdq = list(itertools.product(p, d, q))

# Generate all different combinations of seasonal p, q and q triplets
seasonal_pdq = [(x[0], x[1], x[2], 12) for x in list(itertools.product(p, d, q))]

print('Examples of parameter combinations for Seasonal ARIMA...')
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[1]))
print('SARIMAX: {} x {}'.format(pdq[1], seasonal_pdq[2]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[3]))
print('SARIMAX: {} x {}'.format(pdq[2], seasonal_pdq[4]))

# We will use the AIC (Akaike Information Criterion) value, which is conveniently
# returned with ARIMA models fitted using statsmodels. The AIC measures how well a
# model fits the data while taking into account the overall complexity of the model.
# A model that fits the data very well while using lots of features will be assigned
# a larger AIC score than a model that uses fewer features to achieve the same goodness-of-fit.
#
# Therefore, we are interested in finding the model that yields the lowest AIC value.

warnings.filterwarnings("ignore") # specify to ignore warning messages

for param in pdq:
    for param_seasonal in seasonal_pdq:
        try:
            mod = sm.tsa.statespace.SARIMAX(y,
                                            order=param,
                                            seasonal_order=param_seasonal,
                                            enforce_stationarity=False,
                                            enforce_invertibility=False)

            results = mod.fit()

            print('ARIMA{}x{}12 - AIC:{}'.format(param, param_seasonal, results.aic))
        except:
            continue

# The output of our code suggests that SARIMAX(1, 1, 1)x(1, 1, 1, 12) yields the lowest AIC
# value of 277.78. We should therefore consider this to be optimal option out of all the models
# we have considered.

# We'll start by plugging the optimal parameter values into a new SARIMAX model: 
mod = sm.tsa.statespace.SARIMAX(y,
                                order=(1, 1, 1),
                                seasonal_order=(1, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()

print(results.summary().tables[1])

#==============================================================================
#                 coef    std err          z      P>|z|      [0.025      0.975]
#------------------------------------------------------------------------------
#ar.L1          0.3182      0.092      3.443      0.001       0.137       0.499
#ma.L1         -0.6255      0.077     -8.165      0.000      -0.776      -0.475
#ar.S.L12       0.0010      0.001      1.732      0.083      -0.000       0.002
#ma.S.L12      -0.8769      0.026    -33.811      0.000      -0.928      -0.826
#sigma2         0.0972      0.004     22.634      0.000       0.089       0.106
#==============================================================================

# The coef column shows the weight (i.e. importance) of each feature and how each one
# impacts the time series. The P>|z| column informs us of the significance of each feature
# weight. Here, each weight has a p-value lower or close to 0.05, so it is reasonable to
# retain all of them in our model.

# When fitting seasonal ARIMA models (and any other models for that matter), it is important
# to run model diagnostics to ensure that none of the assumptions made by the model have been
# violated. The plot_diagnostics object allows us to quickly generate model diagnostics and
# investigate for any unusual behavior.

results.plot_diagnostics(figsize=(15, 12))
if plot: plt.show()

# Our primary concern is to ensure that the residuals of our model are uncorrelated and
# normally distributed with zero-mean. If the seasonal ARIMA model does not satisfy these
# properties, it is a good indication that it can be further improved.

# In this case, our model diagnostics suggests that the model residuals are normally
# distributed based on the following:
#
# In the top right plot, we see that the red KDE line follows closely with the N(0,1) line
# (where N(0,1)) is the standard notation for a normal distribution with mean 0 and standard
# deviation of 1). This is a good indication that the residuals are normally distributed.
# The qq-plot on the bottom left shows that the ordered distribution of residuals (blue dots)
# follows the linear trend of the samples taken from a standard normal distribution with N(0, 1).
# Again, this is a strong indication that the residuals are normally distributed.
# The residuals over time (top left plot) don't display any obvious seasonality and appear right,
# to be white noise. This is confirmed by the autocorrelation (i.e. correlogram) plot on the bottom
# which shows that the time series residuals have low correlation with lagged versions of itself.


# We have obtained a model for our time series that can now be used to produce forecasts.
# We start by comparing predicted values to real values of the time series, which will help
# us understand the accuracy of our forecasts. The get_prediction() and conf_int() attributes
# allow us to obtain the values and associated confidence intervals for forecasts of the
# time series.
pred = results.get_prediction(start=pd.to_datetime('1998-01-01'), dynamic=False)
pred_ci = pred.conf_int()

# The dynamic=False argument ensures that we produce one-step ahead forecasts, meaning that
# forecasts at each point are generated using the full history up to that point.

# We can plot the real and forecasted values of the CO2 time series to assess how well we did.
# Notice how we zoomed in on the end of the time series by slicing the date index.

if plot:
    ax = y['1990':].plot(label='observed')
    pred.predicted_mean.plot(ax=ax, label='One-step ahead Forecast', alpha=.7)

    ax.fill_between(pred_ci.index,
                pred_ci.iloc[:, 0],
                pred_ci.iloc[:, 1], color='k', alpha=.2)

    ax.set_xlabel('Date')
    ax.set_ylabel('CO2 Levels')
    plt.legend()

    plt.show()

# It is also useful to quantify the accuracy of our forecasts. We will use the
# MSE (Mean Squared Error), which summarizes the average error of our forecasts.
# For each predicted value, we compute its distance to the true value and square
# the result. The results need to be squared so that positive/negative differences
# do not cancel each other out when we compute the overall mean.
y_forecasted = pred.predicted_mean
y_truth = y['1998-01-01':]

# Compute the mean square error
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))


# The MSE of our one-step ahead forecasts yields a value of 0.07, which is very low as
# it is close to 0. An MSE of 0 would that the estimator is predicting observations of
# the parameter with perfect accuracy, which would be an ideal scenario but it not
# typically possible.

# However, a better representation of our true predictive power can be obtained using
# dynamic forecasts. In this case, we only use information from the time series up to a
# certain point, and after that, forecasts are generated using values from previous
# forecasted time points.
#
# In the code chunk below, we specify to start computing the dynamic forecasts and
# confidence intervals from January 1998 onwards.
pred_dynamic = results.get_prediction(start=pd.to_datetime('1998-01-01'), dynamic=True, full_results=True)
pred_dynamic_ci = pred_dynamic.conf_int()

if plot:
    ax = y['1990':].plot(label='observed', figsize=(20, 15))
    pred_dynamic.predicted_mean.plot(label='Dynamic Forecast', ax=ax)

    ax.fill_between(pred_dynamic_ci.index,
                    pred_dynamic_ci.iloc[:, 0],
                    pred_dynamic_ci.iloc[:, 1], color='k', alpha=.25)

    ax.fill_betweenx(ax.get_ylim(), pd.to_datetime('1998-01-01'), y.index[-1],
                     alpha=.1, zorder=-1)

    ax.set_xlabel('Date')
    ax.set_ylabel('CO2 Levels')

    plt.legend()
    plt.show()

# Once again, we quantify the predictive performance of our forecasts by computing the MSE:
# Extract the predicted and true values of our time series
y_forecasted = pred_dynamic.predicted_mean
y_truth = y['1998-01-01':]

# Compute the mean square error
mse = ((y_forecasted - y_truth) ** 2).mean()
print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))

# The predicted values obtained from the dynamic forecasts yield an MSE of 1.01. This is
# slightly higher than the one-step ahead, which is to be expected given that we are relying
# on less historical data from the time series.

# The get_forecast() attribute of our time series object can compute forecasted values for
# a specified number of steps ahead.
# Get forecast 500 steps ahead in future
pred_uc = results.get_forecast(steps=500)

# Get confidence intervals of forecasts
pred_ci = pred_uc.conf_int()

if plot:
    ax = y.plot(label='observed', figsize=(20, 15))
    pred_uc.predicted_mean.plot(ax=ax, label='Forecast')
    ax.fill_between(pred_ci.index,
                    pred_ci.iloc[:, 0],
                    pred_ci.iloc[:, 1], color='k', alpha=.25)
    ax.set_xlabel('Date')
    ax.set_ylabel('CO2 Levels')

    plt.legend()
    plt.show()


# When working with time-series data, a lot can be revealed through visualizing it.
# A few things to look out for are:
#
# seasonality: does the data display a clear periodic pattern?
# trend: does the data follow a consistent upwards or downward slope?
# noise: are there any outlier points or missing values that are not consistent with the rest of the data?




# Time series decomposition allows us to decompose our time series into three distinct
# components: trend, seasonality, and noise:
rcParams['figure.figsize'] = 11, 9

decomposition = sm.tsa.seasonal_decompose(y, model='additive')
if plot:
    fig = decomposition.plot()
    plt.show()















