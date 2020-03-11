import datetime
import numpy as np
import pandas as pd

# Post Function for fetch_csv where vix data from Quandl is standardized
def rename_col0(df0):
    df0 = df0.rename(columns={'Close': 'price'})
    df0 = df0.fillna(method='ffill')
    df0 = df0[['price', 'Adjusted Close','sid']]
    # Shifting data by one day to avoid forward-looking bias
    return df0.shift(1)

# Post Function for fetch_csv where futures data from Quandl is standardized
def rename_col1(df):
    df = df.rename(columns={'Close': 'price','Trade Date': 'Date'})
    df = df.fillna(method='ffill')
    df = df[['price', 'Settle','sid']]
    # Shifting data by one day to avoid forward-looking bias
    return df.shift(1)
    
def initialize(context):
    # Pulling spot VIX
    fetch_csv('https://www.quandl.com/api/v3/datasets/YAHOO/INDEX_VIX.csv', 
        date_column='Date', 
        date_format='%Y-%m-%d',
        symbol='v',
        post_func=rename_col0)
    # Pulling front month VIX futures data
    fetch_csv('https://www.quandl.com/api/v1/datasets/CHRIS/CBOE_VX1.csv', 
        date_column='Trade Date', 
        date_format='%Y-%m-%d',
        symbol='v1',
        post_func=rename_col1)
    # Pulling second month VIX futures data
    fetch_csv('https://www.quandl.com/api/v1/datasets/CHRIS/CBOE_VX2.csv', 
        date_column='Trade Date', 
        date_format='%Y-%m-%d',
        symbol='v2',
        post_func=rename_col1)
    # Declaring XIV, UPRO, and UVXY as the three ETFs to be used
    context.xiv = sid(40516)
    context.upro = sid(38533)
    context.uvxy = sid(41969)
    
    # set the current maximum value and drawdown
    context.max_val = context.portfolio.portfolio_value 
    context.drawdown = 0 
    
    #set_benchmark(sid(40516))
    
    # Scheduling the order function to occur everyday at open
    schedule_function(my_rebalance, date_rules.every_day(), time_rules.market_open(hours = 0, minutes = 1))
    
def adjust_portfolio(context, SID):
    order_target_percent(context.upro,0)
    order_target_percent(context.uvxy,0)
    order_target_percent(context.xiv,0)
    if SID =="XIV":
        order_target_percent(context.xiv,1)
    elif SID == "UVXY":
        order_target_percent(context.uvxy,1)
    elif SID == "UPRO":
        order_target_percent(context.upro,1)
    
def my_rebalance(context, data):

    # Calculate max value
    if context.max_val < context.portfolio.portfolio_value:
        context.max_val = context.portfolio.portfolio_value
    
    # Calculate drawdown
    last_drawdown = context.portfolio.portfolio_value/context.max_val - 1 ;
    if last_drawdown < context.drawdown:
        context.drawdown = last_drawdown
    
    # Calculating the gap between spot vix and the first month vix future
    last_ratio_v_v1 = data.current('v','Adjusted Close')/data.current('v1','Settle')

    # Calculating the contango ratio of the front and second month VIX Futures 
    last_ratio_v1_v2 = data.current('v1','Settle')/data.current('v2','Settle')

    # Calculating the custom ratio to be used in setting thresholds. We are biased
    # towards the gap between the gap between VIX and the first month future as that moves the
    # ETF far more and also influences contango. However, we do give a bit of weight to Contango
    # as that influences the daily rebalancing of the ETF
    last_ratio = .7*last_ratio_v_v1 + .3*last_ratio_v1_v2 -1
 
    #log.info("Vix %f" %data.current('v','Adjusted Close'))
    #log.info("V1 %f" %data.current('v1','Settle'))
    #log.info("V2 %f" %data.current('v2','Settle'))

    # log.info("v_v1 %f" %last_ratio_v_v1)
    # log.info("v1_v2 %f" %last_ratio_v1_v2)
    # log.info("last ratio %f" %last_ratio)
    
    # Specifying the contango ratio threshold to buy XIV, buy UVXY, or buy UPRO
    # If the ratio is less that -3%, it means there is meaningful upside to XIV
    # from gap between spot VIX and first month future plus contango
    # Anything less than 3% is a wash and can go either way
    # However, if the ratio is greater than 6.5%, it means that there is significant backwardation
    # so we should hold UVXY. We do not set the threshold at +3% as UVXY is double leveraged and
    # we need protection in case there's a suddon move. So we need more than double the other threshold
    # If the ratio is between these two thresholds we just hold UPRO to stay long the market as likely
    # the market will trend sideways and we always want to be long
    
    threshold_xiv= -0.03
    threshold_uvxy = 0.065

    if last_ratio < threshold_xiv:
        if context.xiv not in context.portfolio.positions:
            # If we are not holding XIV then sell everything in portfolio then move to XIV
            adjust_portfolio(context,"XIV")
    elif last_ratio > threshold_uvxy:
        if context.uvxy not in context.portfolio.positions:
            # If we are not holding UVXY then sell everything in portfolio then move to UVXY
            adjust_portfolio(context,"UVXY")
    else:
        if context.upro not in context.portfolio.positions:
            # If we are not holding UPRO then sell everything in portfolio then move to UPRO
            adjust_portfolio(context,"UPRO")
     
    record(drawdown=context.drawdown*100)
    record(ratio=last_ratio*100)
