import quandl
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt


### https://blog.quandl.com/api-for-futures-data
### https://docs.quandl.com/docs/in-depth-usage
### https://docs.quandl.com/docs/python-time-series


def get_quandl_REST(exchange, symbol, month_code, year):
    # example: http://www.quandl.com/api/v3/datasets/MGEX/MWH2012.csv
    # example: http://www.quandl.com/api/v3/datasets/MGEX/MWH2012.json
    return

quandl_api_key = "gCbpWopzuxctHw6y-qq5"
request_rows_count = 2500

def qget(quandl_code, **kwargs):
    print(f'---{quandl_code}---')
    data = quandl.get(quandl_code, **kwargs, api_key=quandl_api_key, rows=request_rows_count)
    return data

def get_year_data(df, subtract_years=1):
    #df = data.loc['2019-01-01':]
    df['dates'] = df.index.values
    df['dates'] = df['dates'].apply(lambda x: str(x)[:10])

    cur_year = datetime.today().year
    prev_year = cur_year - subtract_years

    filt = df.index >= f'{prev_year}-01-01'
    dfy = df[filt]
    return dfy

def plot_data(dfy, col_name, chart_title, show_chart=False):
    plt.style.use('fivethirtyeight')

    #plt.plot(x_vals, y_vals)
    plt.plot(dfy.index.values, dfy[col_name])
    #plt.locator_params(axis='x', nbins=10)

    '''fig, ax = plt.subplots()
    every_nth = 30
    for n, label in enumerate(ax.xaxis.get_ticklabels()):
        if n % every_nth != 0:
            label.set_visible(False)'''

    plt.tight_layout()

    fig = plt.gcf()
    fig.set_size_inches(11, 8)
    fig.savefig('my_chart.png', dpi=100)

    # To propagate the size change to an existing gui window add forward=True
    #fig.set_size_inches(18.5, 10.5, forward=True)

    if show_chart:
        plt.show()

###############################################################################
if __name__ == "__main__":

    # get last row_count rows using Quandl API key (Date, Value)
    #data = qget("EIA/PET_RWTC_D")
    # return as a NumPy array
    #data = qget("EIA/PET_RWTC_D", returns="numpy")

    # set start and end dates
    #data = qget("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")

    # request specific columns (in this case from two different symbols)
    #data = qget(["NSE/OIL.1", "WIKI/AAPL.4"])

    # change the sampling frequency
    #data = quandl.get("EIA/PET_RWTC_D", collapse="monthly")

    # perform elementary calculations on the data
    #data = qget("FRED/GDP", transformation="rdiff")

    # download an entire time-series dataset's data (bulk download as a ZIP file)
    #quandl.bulkdownload("ZEA")

    # continuous Gas Oil Futures
    #data = qget("CHRIS/ICE_G6")
    #data = qget("CHRIS/ICE_G2")
    #data = qget("CHRIS/ICE_G1")

    # continuous Heating Oil Futures
    #data = qget("CHRIS/ICE_O1", api_key=quandl_api_key, rows=row_count)

    # continuous Brent Crude Futures
    #data = qget("CHRIS/ICE_B12")
    #data = qget("CHRIS/ICE_B1")
    #data = qget("CHRIS/ICE_B1", collapse="monthly")
    #data = qget("CHRIS/ICE_B1", transformation="rdiff")

    # OPEC Crude Oil Price
    data_opec = qget("OPEC/ORB") #, transformation="rdiff")

    data_go = qget("CHRIS/ICE_G1")
    data_ho = qget("CHRIS/ICE_O1")
    data_cl = qget("CHRIS/ICE_B1")

    print(data_cl)

    #dfy = get_year_data(data_opec, 4)
    #plot_data(dfy, 'Value', 'OPEC Crude Oil', True)

    #dfy = get_year_data(data_go, 4)
    #plot_data(dfy, 'Settle', 'Gas Oil', True)

    dfy = get_year_data(data_ho, 4)
    plot_data(dfy, 'Settle', 'Heating Oil', True)

    dfy = get_year_data(data_cl, 4)
    plot_data(dfy, 'Settle', 'Brent Crude', True)


    



"""
### https://docs.quandl.com/docs/data-organization

WIKI    End of Day US Stock Prices    
CBOE    Chicago Board Options Exchange
CFTC    CFTC Commitment of Traders Data
FRED    Federal Reserve Economic Data

EIA/PET_RWTC_D = WTI Crude Oil Price from the US Department of Energy dataset

"""
