import pandas as pd
#from pandas.tools.plotting import autocorrelation_plot
from pandas.plotting import autocorrelation_plot # works fine
from matplotlib import pyplot
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from plotly.graph_objs import Scatter, Layout
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import datetime as dt
import math
import sys


def parserA(x):
    return pd.to_datetime(x, format='%Y-%m-%d %I-%p')

def get_plot_lines(df, color1):
    trace0 = go.Scatter(
        x=df.Month,
        y=df['Sales'],
        name='Sales',
        line = dict(color=(color1), width=1)
        )
#    trace1 = go.Scatter(
#        x=df.Month,
#        y=df['discount'],
#        name='discount',
#        line = dict(color=(blue), width=1)
#        )
    return [trace0]     #[trace0, trace1]

def show_plot(title):
    fig = pyplot.gcf()
    fig.canvas.set_window_title(title)
    pyplot.show()
    return

def plot_series(df):
    df.plot()
    show_plot('data series')
    return

def plot_autocorrelation(df):
    autocorrelation_plot(df)
    show_plot('autocorrelation')
    return

def plot_residual_errors(fit):
    residuals = pd.DataFrame(fit.resid)
    residuals.plot()
    show_plot('residual errors')
    residuals.plot(kind='kde')
    show_plot('error distribution')
    print()
    print("residual errors description:")
    print(residuals.describe())
    return

def calc_arima(X, p):
    size = int(len(X) * 0.66)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = list()
    for t in range(len(test)):
            model = ARIMA(history, order=(p,1,0))
            model_fit = model.fit(disp=0)
            output = model_fit.forecast()
            yhat = output[0]
            predictions.append(yhat)
            obs = test[t]
            history.append(obs)
            #print('predicted=%f, expected=%f' % (yhat, obs))
    error = mean_squared_error(test, predictions)
    #print('Test MSE: %.3f' % error)
    return (test, predictions, error)

################################################################################

df = pd.read_csv('data/gemini_BTCUSD_1hr.csv', header=0, parse_dates=[1], index_col=1, squeeze=True)
df1 = pd.read_csv('data/Coinbase_BTCUSD_1h.csv', header=0, parse_dates=['Date'], index_col='Date', squeeze=True, date_parser=parserA)
df2 = pd.read_csv('data/Kraken_BTCUSD_1h.csv', header=0, parse_dates=['Date'], index_col='Date', squeeze=True, date_parser=parserA)
df3 = pd.read_csv('data/Binance_BTCUSDT_1h.csv', header=0, parse_dates=['Date'], index_col='Date', squeeze=True, date_parser=parserA)

print("First few data points:")
print(df.head(10))
print

#plot_series(df['Close'])
col = 'Close'
pyplot.plot(df[col], color='green')
pyplot.plot(df1[col], color='blue')
pyplot.plot(df2[col], color='red')
pyplot.plot(df3[col], color='gray')
show_plot("(green=Gemini  blue=Coinbase  red=Kraken  gray=Binance)")
exit()