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


def parser(x):
    return dt.datetime.strptime('190'+x, '%Y-%m')

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


#series = pd.read_csv('shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
#df = pd.read_csv('data/shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
df = pd.read_csv('data/gemini_BTCUSD_1hr.csv', header=0, parse_dates=[1], index_col=1, squeeze=True)
df1 = pd.read_csv('data/gemini_ETHUSD_1hr.csv', header=0, parse_dates=[1], index_col=1, squeeze=True)
df2 = pd.read_csv('data/gemini_LTCUSD_1hr.csv', header=0, parse_dates=[1], index_col=1, squeeze=True)
df3 = pd.read_csv('data/gemini_ZECUSD_1hr.csv', header=0, parse_dates=[1], index_col=1, squeeze=True)

df['log'] = df['Close'].apply(lambda x: math.log(x))
df1['log'] = df1['Close'].apply(lambda x: math.log(x))
df2['log'] = df2['Close'].apply(lambda x: math.log(x))
df3['log'] = df3['Close'].apply(lambda x: math.log(x))

print("Done loading DataFrames")

df['LTC'] = df2['log'].copy()
df['ZEC'] = df3['log'].copy()
#df['spread'] = df['LTC'].sub - df['ZEC']
df['spread'] = df.LTC.fillna(df.ZEC)
df['spread'] = df['LTC'] - df['ZEC']

print("First few data points:")
print(df.head(10))
print

#plot_series(df['Close'])
col = 'log'
pyplot.plot(df[col], color='green')
pyplot.plot(df1[col], color='blue')
pyplot.plot(df2[col], color='red')
pyplot.plot(df3[col], color='gray')
pyplot.plot(df['spread'], color='black')
show_plot("(green=BTC  blue=ETH  red=LTC  gray=ZEC)")
exit()

"""
plot_series(df)
plot_autocorrelation(df)

# fit model
model = ARIMA(df, order=(5,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# plot residual errors
plot_residual_errors(model_fit)
"""

print("Mean Squared Error (MSE) for different lags (lower = better fit):")
lag_count = 5
errors = [None] * lag_count
for lag in range(1,lag_count+1):
    (actual, predictions, error) = calc_arima(df.values, lag)
    print('lag %d    MSE: %.3f' % (lag, error))
    errors[lag-1] = error
    

min_mse = min(errors)
lag = errors.index(min_mse) + 1
(actual, predictions, error) = calc_arima(df.values, lag)
    
# plot
pyplot.plot(actual)
pyplot.plot(predictions, color='red')
show_plot("lag {0}    (red=predicted  blue=actual)".format(lag))




"""
blue = 'rgb(0, 0, 255)'

chart_data = []
df = df.sort_values('Month')
chart_data.extend(get_plot_lines(df, blue))

layout = go.Layout(showlegend=False)
fig = go.Figure(data=chart_data, layout=layout)
plotly.offline.plot(fig, filename='shampoo.html')
"""
