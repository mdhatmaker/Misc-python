import matplotlib.pyplot as plt
import pandas as pd                                                                                                                            
import yfinance as yf                                                                                                                                          
from fredapi import Fred
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
import logging
import sys


# https://pypi.org/project/fredapi/
# https://analyzingalpha.com/yfinance-python
# https://plotly.com/python/line-charts/


def get_stock_data(ticker, period='5y', interval='1d', add_info = False):    # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]                                                                                                                         
    """                                                                                                                                                       
    Get stock data from yahoo finance                                                                                                                         
                                                                                                                                                              
    Args:                                                                                                                                                     
        ticker (str): stock ticker symbol                                                                                                                    
        period (str): time period to get data                                                                                                                
                                                                                                                                                              
    Returns:                                                                                                                                                  
        pandas.DataFrame: stock data                                                                                                                          
    """                                                                                                                                                       
    stock = yf.Ticker(ticker)
    if add_info:        
        info = yf.info
        info.keys()  
        print(info['sector'])       
        options = stock.option_chain()   
        calls = options.calls
        calls
        puts = options.puts    
        puts                                                                                                  
    stock_df = stock.history(period=period, interval=interval)                                                                                                                
    return stock_df


# now = datetime.now() # current date and time
# year = now.strftime("%Y")
# month = now.strftime("%m")
# day = now.strftime("%d")
# time = now.strftime("%H:%M:%S")
# date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
def get_fred_data(series, period='5y', interval='1d'):
    now = datetime.now()
    date_end = now.strftime("%m/%d/%Y")
    date_start = "1/1/2000"
    df = fred.get_series(series, observation_start=date_start, observation_end=date_end)
    return df

#===========================================================================================================================================
def display_chart(df, xcol = '', plot_title = 'Historical values', x_title = 'Date', y_title = 'Value', line_styles = {}):
    display_chart_plotly(df, xcol, plot_title, x_title, y_title, line_styles)
    #display_chart_matplotlib(df)

def display_chart_plotly(df, xcol = '', plot_title = '(chart title)', x_title = '???', y_title = '???', line_styles = {}):
    # Display summary of the data
    for k,v in df.items():
      print(k)
      print(v)    
    fig = go.Figure()
    for k,v in df.items():
        #fig = px.line(df)   #, x="year", y="lifeExp", color='country')
        if xcol == '':
            if k in line_styles:
                fig.add_trace(go.Scatter(x=v.index, y=v, mode='lines', name=k, line=line_styles[k]))  #dict(width=4, dash=line_styles[k])))
            else:
                fig.add_trace(go.Scatter(x=v.index, y=v, mode='lines', name=k))
        else:
            if k in line_styles:
                fig.add_trace(go.Scatter(x=v.index, y=v[xcol], mode='lines', name=k, line=line_styles[k]))
            else:
                fig.add_trace(go.Scatter(x=v.index, y=v[xcol], mode='lines', name=k))
            #fig.add_trace(go.Scatter(x=v.index, y=v[xcol], mode='lines+markers', name=k))
            #fig.add_trace(go.Scatter(x=v.index, y=v[xcol], mode='markers', name=k))
    # Edit the layout
    fig.update_layout(title=plot_title, xaxis_title=x_title, yaxis_title=y_title)
    #fig.update_layout(legend_title='<b> Trend </b>')
    fig.update_layout(legend=dict(x=.02, y=.98, traceorder="normal", font=dict(family="sans-serif", size=12, color="black"), bgcolor="White", bordercolor="Black", borderwidth=2))    # x, y between 0 and 1
    fig.update_layout(margin=dict(l=5, r=20, t=30, b=5), )
    fig.show()

def display_chart_matplotlib(df):
    # Display summary of the data
    for k,v in df.items():
        print(k)
        print(v)   
    # Plotting the data                                                                                                                                           
    plt.figure(figsize=(18,10)) 
    for k,v in df.items():
        plt.plot(v, label=k)                                                                                                                                   
    plt.title('Historical values')                                                                                                         
    plt.xlabel('Date')                                                                                                                                            
    plt.ylabel('Value')                                                                                                                                   
    plt.legend()           
    plt.tight_layout()      
    plt.axhline()                                                                                                                            
    plt.show()    
#===========================================================================================================================================

#===========================================================================================================================================
def sample_sparklines():
    df = px.data.stocks(indexed=True)
    fig = px.line(df, facet_row="company", facet_row_spacing=0.01, height=200, width=200)
    # hide and lock down axes
    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible=False, fixedrange=True)
    # remove facet/subplot labels
    fig.update_layout(annotations=[], overwrite=True)
    # strip down the rest of the plot
    fig.update_layout(
        showlegend=False,
        plot_bgcolor="white",
        margin=dict(t=10,l=10,b=10,r=10)
    )
    # disable the modebar for such a small plot
    fig.show(config=dict(displayModeBar=False))

def sample_lineplot1():
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
    fig.show()

def sample_lineplot2():
    df = px.data.gapminder().query("continent=='Oceania'")
    fig = px.line(df, x="year", y="lifeExp", color='country')
    fig.show()

def sample_lineplot3():
    df = px.data.gapminder().query("continent == 'Oceania'")
    fig = px.line(df, x='year', y='lifeExp', color='country', symbol="country")
    fig.show()

def sample_lineplot_dates():
    df = px.data.stocks()
    fig = px.line(df, x='date', y="GOOG")
    fig.show()

def sample_lineplot_markers():
    df = px.data.gapminder().query("continent == 'Oceania'")
    fig = px.line(df, x='year', y='lifeExp', color='country', markers=True)
    fig.show()

def sample_lineplot_dataorder():
    df = pd.DataFrame(dict(
        x = [1, 3, 2, 4],
        y = [1, 2, 3, 4]
    ))
    fig = px.line(df, x="x", y="y", title="Unsorted Input") 
    fig.show()
    df = df.sort_values(by="x")
    fig = px.line(df, x="x", y="y", title="Sorted Input") 
    fig.show()

def sample_lineplot_modes():
    # Create random data with numpy
    import numpy as np
    np.random.seed(1)
    N = 100
    random_x = np.linspace(0, 1, N)
    random_y0 = np.random.randn(N) + 5
    random_y1 = np.random.randn(N)
    random_y2 = np.random.randn(N) - 5
    # Create traces
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=random_x, y=random_y0, mode='lines', name='lines'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y1, mode='lines+markers', name='lines+markers'))
    fig.add_trace(go.Scatter(x=random_x, y=random_y2, mode='markers', name='markers'))
    fig.show()

def sample_lineplot_styles():
    # Add data
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    high_2000 = [32.5, 37.6, 49.9, 53.0, 69.1, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
    low_2000 = [13.8, 22.3, 32.5, 37.2, 49.9, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
    high_2007 = [36.5, 26.6, 43.6, 52.3, 71.5, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
    low_2007 = [23.6, 14.0, 27.0, 36.8, 47.6, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
    high_2014 = [28.8, 28.5, 37.0, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
    low_2014 = [12.7, 14.3, 18.6, 35.5, 49.9, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]
    fig = go.Figure()
    # Create and style traces
    fig.add_trace(go.Scatter(x=month, y=high_2014, name='High 2014', line=dict(color='firebrick', width=4)))
    fig.add_trace(go.Scatter(x=month, y=low_2014, name = 'Low 2014', line=dict(color='royalblue', width=4)))
    fig.add_trace(go.Scatter(x=month, y=high_2007, name='High 2007', line=dict(color='firebrick', width=4, dash='dash'))) # dash options include 'dash', 'dot', and 'dashdot'
    fig.add_trace(go.Scatter(x=month, y=low_2007, name='Low 2007', line = dict(color='royalblue', width=4, dash='dash')))
    fig.add_trace(go.Scatter(x=month, y=high_2000, name='High 2000', line = dict(color='firebrick', width=4, dash='dot')))
    fig.add_trace(go.Scatter(x=month, y=low_2000, name='Low 2000', line=dict(color='royalblue', width=4, dash='dot')))
    # Edit the layout
    fig.update_layout(title='Average High and Low Temperatures in New York', xaxis_title='Month', yaxis_title='Temperature (degrees F)')
    fig.show()

def sample_plotly():
    logging.info("Plotly sample charts : starting")
    sample_lineplot_modes()
    sample_sparklines()
    sample_lineplot_dates()
    logging.info("Plotly sample charts : ending")
#===========================================================================================================================================


def treasury1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['t10y2y'] = fred.get_series('T10Y2Y')  # 10-year Treasury Constant Maturity Minus 2-Year Treasury Constant Maturity  
    df['10yreal'] = fred.get_series('REAINTRATREARAT10Y')  # 10-Year Treasury Inflation-Indexed Security, Constant Maturity                                                                                                                            
    display_chart(df)

def stock1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['amzn'] = get_stock_data('AMZN', period, interval)       # Getting AMZN data                                                                                                                                      
    df['aapl'] = get_stock_data('AAPL', period, interval)       # Getting AAPL data                                                                                                                                      
    df['meta'] = get_stock_data('META', period, interval)       # Getting META data                                                                                                                                      
    df['goog'] = get_stock_data('GOOG', period, interval)       # Getting GOOG data
    df['nflx'] = get_stock_data('NFLX', period, interval)       # Getting NFLX data
    df['nvda'] = get_stock_data('NVDA', period, interval)       # Getting NVDA data
    df['intc'] = get_stock_data('INTC', period, interval)       # Getting INTC data
    df['msft'] = get_stock_data('MSFT', period, interval)       # Getting MSFT data
    df['qcom'] = get_stock_data('QCOM', period, interval)       # Getting MSFT data
    display_chart(df, 'Close', f'<b>Tech</b> Stock Prices ({interval})', 'Date', 'Price')

def stock2(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['dis'] = get_stock_data('DIS', period, interval)         # Getting DIS data
    df['spy'] = get_stock_data('SPY', period, interval)         # Getting SPY data
    #df['vix'] = get_stock_data('VIX', period, interval)         # Getting VIX data
    display_chart(df, 'Close', f'<b>More</b> Stock Prices ({interval})', 'Date', 'Price')

def housing1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['houseinv'] = fred.get_series('HOSINVUSM495N')           # Housing Inventory: Total for United States 
    df['existhomesales'] = fred.get_series('EXHOSLUSM495S')     # Existing Home Sales for United States
    df['medprice'] = fred.get_series('MSPUS')                   # Median Sales Price of Houses Sold for the United States
    df['houseaffordidx'] = fred.get_series('FIXHAI')            # Housing Affordability Index for the United States
    df['cpiurban'] = fred.get_series('CPALTT01USM657N')      # Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
    df['cpitotalusa'] = fred.get_series('CPIAUCSL')             # Consumer Price Index: All Items, Total for U.S.
    #df['10yreal'] = fred.get_series('REAINTRATREARAT10Y')   # 10-Year Treasury Inflation-Indexed Security, Constant Maturity                                                                                                                            
    display_chart(df, '', 'Housing Data')

def index1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    #df['spx'] = get_stock_data('ES=F', period, interval)                                                                                                                                    
    df['dow'] = get_stock_data('YM=F', period, interval)                                                                                                                                   
    df['ndq'] = get_stock_data('NQ=F', period, interval)
    #df['russ2k'] = get_stock_data('RTY=F', period, interval)
    display_chart(df, 'Close', '<b>Stock</b> Indexes ({interval})', 'Date', 'Price')

def index2(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['spx'] = get_stock_data('ES=F', period, interval)
    df['russ2k'] = get_stock_data('RTY=F', period, interval)
    df['cmc200'] = get_stock_data('^CMC200', period, interval)
    display_chart(df, 'Close', '<b>Medium-Sized</b> Indexes ({interval})', 'Date', 'Price')

def index3(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['vix'] = get_stock_data('^VIX', period, interval)
    display_chart(df, 'Close', '<b>Small</b> Indexes ({interval})', 'Date', 'Price')

def index4(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['sp500'] = fred.get_series('SP500')  #, period, interval)                                                                                                                                   
    display_chart(df)

def commodity1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    #df['gold'] = get_stock_data('GC=F', period, interval)
    df['crude'] = get_stock_data('CL=F', period, interval)
    df['silver'] = get_stock_data('SI=F', period, interval)
    display_chart(df, 'Close', '<b>Commodity</b> Prices ({interval})', 'Date', 'Price')

def commodity2(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['gold'] = get_stock_data('GC=F', period, interval)
    display_chart(df, 'Close', '<b>Commodity</b> Prices ({interval})', 'Date', 'Price')

def crypto1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['btc'] = get_stock_data('BTC-USD', period, interval)
    df['cmc200'] = get_stock_data('^CMC200', period, interval)
    display_chart(df, 'Close', '<b>Crypto</b> Prices ({interval})', 'Date', 'Price')

def bond1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['10yUSD'] = get_stock_data('ZN=F', period, interval)
    df['5yUSD'] = get_stock_data('ZF=F', period, interval)
    df['2yUSD'] = get_stock_data('ZT=F', period, interval)
    #df['2yUSD'] = get_stock_data('2YY=F', period, interval)
    display_chart(df, 'Close', '<b>Bond</b> Prices ({interval})', 'Date', 'Price')

def yield1(period = '5y', interval = '1d'):
    df = {}                                
    df['30yUSD'] = get_stock_data('^TYX', period, interval)                                                                                       
    df['10yUSD'] = get_stock_data('^TNX', period, interval)
    df['5yUSD'] = get_stock_data('^FVX', period, interval)
    df['13wkBILL'] = get_stock_data('^IRX', period, interval)
    display_chart(df, 'Close', '<b>Treasury Yield</b> Prices ({interval})', 'Date', 'Price')

def rates1(period = '5y', interval = '1d'):
    df = {}                                
    df['30yUSD'] = get_stock_data('^TYX', period, interval)                                                                                       
    df['10yUSD'] = get_stock_data('^TNX', period, interval)
    df['5yUSD'] = get_stock_data('^FVX', period, interval)
    df['13wkBILL'] = get_stock_data('^IRX', period, interval)
    display_chart(df, 'Close', '<b>Treasury</b> Rates', 'Date', 'Rate')

def rates2(period = '5y', interval = '1d'):
    df = {}
    line_styles = {}                          
    df['FedFunds'] = get_fred_data('FEDFUNDS', period, interval)
    df['30yFIX'] = get_fred_data('MORTGAGE30US', period, interval)
    df['15yFIX'] = get_fred_data('MORTGAGE15US', period, interval)
    df['5yARM'] = get_fred_data('MORTGAGE5US', period, interval)
    df['1yARM'] = get_fred_data('MORTGAGE1US', period, interval)
    df['T10Y2Y'] = get_fred_data('T10Y2Y', period, interval)
    df['T10Y3M'] = get_fred_data('T10Y3M', period, interval)
    df['T10YFF'] = get_fred_data('T10YFF', period, interval)
    line_styles['FedFunds'] = dict(color='darkblue', width=3, dash='dash')   #, dash='dash' or dash='dot' or dash='dashdot'
    line_styles['T10Y2Y'] = dict(color='black', width=2)    
    line_styles['T10Y3M'] = dict(color='goldenrod', width=1)
    line_styles['T10YFF'] = dict(color='grey', width=1)
    display_chart(df, '', '<b>Mortgage</b> Rates', 'Date', 'Rate', line_styles)

def fx1(period = '25y', interval = '1d'):
    df = {}
    line_styles = {}                          
    df['EUR/USD'] = get_stock_data('EURUSD=X', period, interval)
    df['GBP/USD'] = get_stock_data('GBPUSD=X', period, interval)
    df['AUD/USD'] = get_stock_data('AUDUSD=X', period, interval)
    df['NZD/USD'] = get_stock_data('NZDUSD=X', period, interval)
    df['EUR/GBP'] = get_stock_data('EURGBP=X', period, interval)
    df['EUR/CAD'] = get_stock_data('EURCAD=X', period, interval)
    df['EUR/CHF'] = get_stock_data('EURCHF=X', period, interval)
    #df['USD/JPY'] = get_stock_data('JPY=X', period, interval)
    line_styles['EUR/USD'] = dict(color='darkblue', width=3)   #, dash='dash' or dash='dot' or dash='dashdot'
    line_styles['GBP/USD'] = dict(width=3)
    line_styles['AUD/USD'] = dict(width=3)
    line_styles['NZD/USD'] = dict(width=3)
    display_chart(df, 'Close', '<b>Currency</b> FX (1)', 'Date', 'Rate', line_styles)

def fx2(period = '25y', interval = '1d'):
    df = {}
    line_styles = {}                          
    df['USD/JPY'] = get_stock_data('JPY=X', period, interval)
    df['GBP/JPY'] = get_stock_data('GBPJPY=X', period, interval)
    df['EUR/JPY'] = get_stock_data('EURJPY=X', period, interval)
    df['EUR/SEK'] = get_stock_data('EURSEK=X', period, interval)
    df['EUR/HUF'] = get_stock_data('EURHUF=X', period, interval)
    df['USD/SGD'] = get_stock_data('SGD=X', period, interval)
    df['USD/MYR'] = get_stock_data('MYR=X', period, interval)
    df['USD/CNY'] = get_stock_data('CNY=X', period, interval)
    df['USD/HKD'] = get_stock_data('HKD=X', period, interval)
    df['USD/INR'] = get_stock_data('INR=X', period, interval)
    df['USD/MXN'] = get_stock_data('MXN=X', period, interval)
    df['USD/PHP'] = get_stock_data('PHP=X', period, interval)
    df['USD/THB'] = get_stock_data('THB=X', period, interval)
    df['USD/ZAR'] = get_stock_data('ZAR=X', period, interval)
    df['USD/RUB'] = get_stock_data('RUB=X', period, interval)
    line_styles['USD/JPY'] = dict(color='darkblue', width=3)   #, dash='dash' or dash='dot' or dash='dashdot'
    line_styles['GBP/JPY'] = dict(width=3)
    line_styles['EUR/JPY'] = dict(width=3)
    display_chart(df, 'Close', '<b>Currency</b> FX (2)', 'Date', 'Rate', line_styles)


############################################################################################################################################
    
if __name__ != "__main__":
    sys.exit(0)

# set it to the evironment variable FRED_API_KEY
# save it to a file and use the ‘api_key_file’ parameter
# pass it directly as the ‘api_key’ parameter
#fred = Fred(api_key='insert api key here')
fred = Fred(api_key_file='/Users/michael/fred_api_key.txt')

# Search for data series
# You can always search for data series on the FRED website. But sometimes it can be more convenient to search programmatically. fredapi provides a search() method that does a fulltext search and returns a DataFrame of results.
# fred.search('potential gdp')
# You can also search by release id and category id with various options
# df1 = fred.search_by_release(11)
# df2 = fred.search_by_category(101, limit=10, order_by='popularity', sort_order='desc')



#===========================================================================================================================================


fx1()
fx2()
rates1()
rates2()
#yield1('max')
#stock1('10y', '1wk')
#housing1()
#index1()
#index2()
#index3()
#commodity1()
#commodity2()
#crypto1()
#bond1()
#treasury1()



