# load and plot dataset
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt



# https://machinelearningmastery.com/tune-arima-parameters-python/


# load dataset
def parser(x):
    return datetime.strptime('190'+x, '%Y-%m')

def test1():
    series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    # summarize first few rows
    print(series.head())
    # line plot
    series.plot()
    pyplot.show()
    return

def test2():
    series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    # split into train and test sets
    X = series.values
    train, test = X[0:-12], X[-12:]
    history = [x for x in train]
    predictions = list()
    # walk-forward validation
    for t in range(len(test)):
            # fit model
            model = ARIMA(history, order=(4,1,0))
            model_fit = model.fit()
            # one step forecast
            yhat = model_fit.forecast()[0]
            # store forecast and ob
            predictions.append(yhat)
            history.append(test[t])
    # evaluate forecasts
    rmse = sqrt(mean_squared_error(test, predictions))
    print('Test RMSE: %.3f' % rmse)
    # plot forecasts against actual outcomes
    pyplot.plot(test)
    pyplot.plot(predictions, color='red')
    pyplot.show()
    return

def test3():
    series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    # split into train and test sets
    X = series.values
    size = int(len(X) * 0.66)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    # walk-forward validation
    for t in range(len(test)):
        # fit model
        model = ARIMA(history, order=(4,1,0))
        model_fit = model.fit(disp=False)
        # one step forecast
        yhat = model_fit.forecast()[0]
        # store forecast and ob
        predictions.append(yhat)
        history.append(test[t])
    # evaluate forecasts
    rmse = sqrt(mean_squared_error(test, predictions))
    print('Test RMSE: %.3f' % rmse)
    return

# Running the example shows the 4 AR terms specified in the order of the model plus the first term in the array,
# which is a trend constant.
# 'trend' is 'nc' or 'c'
def test4(trend = 'c'):
    series = read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
    # split into train and test sets
    X = series.values
    size = int(len(X) * 0.66)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    # walk-forward validation
    for t in range(len(test)):
            # fit model
            model = ARIMA(history, order=(4,1,0))
            model_fit = model.fit(disp=False, trend=trend)
            print(model_fit.params)
            # one step forecast
            yhat = model_fit.forecast()[0]
            # store forecast and ob
            predictions.append(yhat)
            history.append(test[t])
    # evaluate forecasts
    rmse = sqrt(mean_squared_error(test, predictions))
    print('Test RMSE: %.3f' % rmse)
    return


#########################################################################################################################

if __name__ == "__main__":
    test4('c')


# Although the smaller the RMSE, the better, you can make theoretical claims on levels of the
# RMSE by knowing what is expected from your DV in your field of research. Keep in mind that you
# can always normalize the RMSE.
#
# Experiment on your own problem and determine whether this constant improves performance.
#
# My own experimentation suggests that ARIMA models may be less likely to converge with the trend
# term disabled, especially when using more than zero MA terms.

# The solver parameter specifies the numerical optimization method to fit the coefficients
# to the data.
#
# There is often little reason to tune this parameter other than execution speed if you have a
# lot of data. The differences will likely be quite minor.
# The default is the fast “lbfgs” method (Limited-memory BFGS).
# Generally, “lbfgs” and “bfgs” provide good real-world tradeoff between speed, performance, and stability.



# SUMMARY
# In this tutorial, you discovered some of the finer points in configuring your ARIMA model with
# Statsmodels in Python.
#
# Specifically, you learned:
#
# How to turn off the noisy convergence output from the solver when fitting coefficients.
# How to evaluate the difference between different solvers to fit your ARIMA model.
# The effect of enabling and disabling a trend term in your ARIMA model.




"""
It is important to evaluate time series forecasting models consistently.

In this section, we will define how we will evaluate the three forecast models in this tutorial.

First, we will hold the last one year of data back and evaluate forecasts on this data. Given the
data is monthly, this means that the last 12 observations will be used as test data.

We will use a walk-forward validation method to evaluate model performance. This means that each
time step in the test dataset will be enumerated, a model constructed on history data, and the
forecast compared to the expected value. The observation will then be added to the training
dataset and the process repeated.

Walk-forward validation is a realistic way to evaluate time series forecast models as one would
expect models to be updated as new observations are made available.

Finally, forecasts will be evaluated using root mean squared error, or RMSE. The benefit of RMSE
is that it penalizes large errors and the scores are in the same units as the forecast values
(car sales per month).

An ARIMA(4,1,0) forecast model will be used as the baseline to explore the additional parameters
of the model. This may not be the optimal model for the problem, but is generally skillful against
some other hand tested configurations.

In summary, the test harness involves:

The last 2 years of data used a test set.
Walk-forward validation for model evaluation.
Root mean squared error used to report model skill.
An ARIMA(4,1,0) model will be used as a baseline.
"""

