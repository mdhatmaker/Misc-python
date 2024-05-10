import matplotlib.pyplot as plt                                                                                                                               
import yfinance as yf                                                                                                                                          


# https://analyzingalpha.com/yfinance-python

def get_stock_data(ticker, period, interval='1d'):                                                                                                                           
    """                                                                                                                                                       
    Get stock data from yahoo finance                                                                                                                         
                                                                                                                                                              
    Args:                                                                                                                                                     
        ticker (str): stock ticker symbol                                                                                                                    
        period (str): time period to get data                                                                                                                
                                                                                                                                                              
    Returns:                                                                                                                                                  
        pandas.DataFrame: stock data                                                                                                                          
    """                                                                                                                                                       
    stock = yf.Ticker(ticker)                                                                                                                                 
    stock_df = stock.history(period=period)                                                                                                                  
    return stock_df


def display_chart(df):
    # Display summary of the data
    for k,v in df.items():
      print(k)
      print(v)    

    # Plotting the data                                                                                                                                           
    plt.figure(figsize=(18,10)) 
    for k,v in df.items():
      plt.plot(v['Close'], label=k)                                                                                                                                   
    plt.title('Historical stock values')                                                                                                         
    plt.xlabel('Date')                                                                                                                                            
    plt.ylabel('Closing Price')                                                                                                                                   
    plt.legend()           
    plt.tight_layout()                                                                                                                                       
    plt.show()    


def stock1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['aapl'] = get_stock_data('AAPL', period, interval)     # Getting AAPL data                                                                                                                                      
    df['meta'] = get_stock_data('META', period, interval)     # Getting META data                                                                                                                                      
    df['goog'] = get_stock_data('GOOG', period, interval)     # Getting GOOG data
    df['nflx'] = get_stock_data('NFLX', period, interval)     # Getting NFLX data
    df['dis'] = get_stock_data('DIS', period, interval)       # Getting DIS data
    #df['vix'] = get_stock_data('VIX', period, interval)       # Getting VIX data
    #df['spy'] = get_stock_data('SPY', period, interval)       # Getting SPY data
    display_chart(df)

def index1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    #df['spx'] = get_stock_data('ES=F', period, interval)                                                                                                                                    
    df['dow'] = get_stock_data('YM=F', period, interval)                                                                                                                                   
    df['ndq'] = get_stock_data('NQ=F', period, interval)
    #df['russ2k'] = get_stock_data('RTY=F', period, interval)
    display_chart(df)

def index2(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['spx'] = get_stock_data('ES=F', period, interval)
    df['russ2k'] = get_stock_data('RTY=F', period, interval)
    df['cmc200'] = get_stock_data('^CMC200', period, interval)
    display_chart(df)

def index3(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['vix'] = get_stock_data('^VIX', period, interval)
    display_chart(df)

def commodity1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['crude'] = get_stock_data('CL=F', period, interval)
    #df['gold'] = get_stock_data('GC=F', period, interval)
    df['silver'] = get_stock_data('SI=F', period, interval)
    display_chart(df)

def commodity2(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['gold'] = get_stock_data('GC=F', period, interval)
    display_chart(df)

def crypto1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['btc'] = get_stock_data('BTC-USD', period, interval)
    df['cmc200'] = get_stock_data('^CMC200', period, interval)
    display_chart(df)

def bond1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    #df['10yUSD'] = get_stock_data('^TNX', period, interval)
    df['10yUSD'] = get_stock_data('ZN=F', period, interval)
    #df['5yUSD'] = get_stock_data('^FVX', period, interval)
    df['5yUSD'] = get_stock_data('ZF=F', period, interval)
    #df['13wkBILL'] = get_stock_data('^IRX', period, interval)
    #df['2yUSD'] = get_stock_data('2YY=F', period, interval)
    df['2yUSD'] = get_stock_data('ZT=F', period, interval)
    display_chart(df)

def yield1(period = '5y', interval = '1d'):
    df = {}                                                                                                                           
    df['10yUSD'] = get_stock_data('^TNX', period, interval)
    df['5yUSD'] = get_stock_data('^FVX', period, interval)
    df['13wkBILL'] = get_stock_data('^IRX', period, interval)
    #df['10y2ySPREAD'] = df['10yUSD']['Close'] - df['13wkBILL']['Close']
    display_chart(df)


#stock1('5y', '1w')
#index1()
#index2()
#index3()
#commodity1()
#commodity2()
#crypto1()
#bond1()
yield1()

