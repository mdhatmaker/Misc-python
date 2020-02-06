import plotly.plotly as py
import plotly.graph_objs as go
import plotly
from plotly.graph_objs import Scatter, Layout
from datetime import datetime
import pandas_datareader.data as web
import pandas as pd
import sys


def to_unix_time(dt):
    epoch =  datetime.utcfromtimestamp(0)
    return (dt - epoch).total_seconds() * 1000


"""
Time Series Plot with datetime Objects
df = web.DataReader("aapl", 'yahoo', datetime(2015, 1, 1), datetime(2016, 7, 1))
data = [go.Scatter(x=df.index, y=df.High)]
py.iplot(data)
"""

# Date Strings
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
data = [go.Scatter(x=df.Date, y=df['AAPL.Close'])]
#py.iplot(data)
plotly.offline.plot({
    "data": [Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
    "layout": Layout(title="hello world")
})


# Time Series Plot with Custom Date Range
x = [datetime(year=2013, month=10, day=04),
    datetime(year=2013, month=11, day=05),
    datetime(year=2013, month=12, day=06)]
data = [go.Scatter(
            x=x,
            y=[1, 3, 6])]
layout = go.Layout(xaxis = dict(
                   range = [to_unix_time(datetime(2013, 10, 17)),
                            to_unix_time(datetime(2013, 11, 20))]
    ))
fig = go.Figure(data = data, layout = layout)
plotly.offline.plot(fig)


# Manually Set Date Range
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
trace_high = go.Scatter(
                x=df.Date,
                y=df['AAPL.High'],
                name = "AAPL High",
                line = dict(color = '#17BECF'),
                opacity = 0.8)
trace_low = go.Scatter(
                x=df.Date,
                y=df['AAPL.Low'],
                name = "AAPL Low",
                line = dict(color = '#7F7F7F'),
                opacity = 0.8)
data = [trace_high,trace_low]
layout = dict(
    title = "Manually Set Date Range",
    xaxis = dict(
        range = ['2016-07-01','2016-12-31'])
)
fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename = "Manually Set Range")


# Time Series with Rangeslider
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")
trace_high = go.Scatter(
    x=df.Date,
    y=df['AAPL.High'],
    name = "AAPL High",
    line = dict(color = '#17BECF'),
    opacity = 0.8)
trace_low = go.Scatter(
    x=df.Date,
    y=df['AAPL.Low'],
    name = "AAPL Low",
    line = dict(color = '#7F7F7F'),
    opacity = 0.8)
data = [trace_high,trace_low]
layout = dict(
    title='Time Series with Rangeslider',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        type='date'
    )
)
fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename = "Time Series with Rangeslider")



"""
import plotly as py

colors=['rgb(53,195,176)',
'rgb(168,201,121)',
'rgb(255,210,181)',
'rgb(255,169,164)',
'rgb(255,140,148)']

points=points_sphere(N=100)
data2=get_data(points,  R=1.005, arcs=False, colorscale=[], colors=colors)

fig2 = Figure(data=data2, layout=plot_layout(ax=noaxis))
fig2['layout'].update(title='Polyhedral approximation of a spherical Voronoi diagram')
py.iplot(fig2, filename='polyhedral-voronoi')
"""
