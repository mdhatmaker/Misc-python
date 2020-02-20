
import quandl
import pandas as pd


### https://blog.quandl.com/api-for-futures-data
### https://docs.quandl.com/docs/in-depth-usage
### https://docs.quandl.com/docs/python-time-series


def get_quandl_REST(exchange, symbol, month_code, year):
    # example: http://www.quandl.com/api/v3/datasets/MGEX/MWH2012.csv
    # example: http://www.quandl.com/api/v3/datasets/MGEX/MWH2012.json
    return

quandl_api_key = "gCbpWopzuxctHw6y-qq5"
request_rows_count = 1500

def qget(quandl_code, **kwargs):
    print(f'---{quandl_code}---')
    data = quandl.get(quandl_code, **kwargs, api_key=quandl_api_key, rows=request_rows_count)
    return data


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
    data = qget("OPEC/ORB") #, transformation="rdiff")

    # read from existing c
    print(data)



"""
### https://docs.quandl.com/docs/data-organization

WIKI    End of Day US Stock Prices    
CBOE    Chicago Board Options Exchange
CFTC    CFTC Commitment of Traders Data
FRED    Federal Reserve Economic Data



EIA/PET_RWTC_D = WTI Crude Oil Price from the US Department of Energy dataset

"""