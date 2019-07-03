import pandas as pd
import numpy as np
import os
import requests
import shutil
#import sys
#from datetime import datetime
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

#def similar(a,b):
#	return SequenceMatcher(None, a, b).ratio()
  
def get_data(url):
    r = requests.get(url)
    data = r.text
    #soup = BeautifulSoup(data, "html.parser")
    return data

def download_file(url, folder):
    #url = 'https://www.cryptodatadownload.com/cdd/gemini_BTCUSD_1hr.csv'
    #folder = 'data'

    pathname = os.path.join(folder, os.path.basename(url))
    print("Writing output to file '{}'".format(pathname))

    r = requests.get(url, auth=('usrname', 'password'), verify=False, stream=True)
    r.raw.decode_content = True
    with open(pathname, 'wb') as f:
        shutil.copyfileobj(r.raw, f)
    return

def read_historical(filename, folder):
    #filename = 'gemini_ETHUSD_1hr.csv'
    #folder = 'data'

    pathname = os.path.join(folder, filename)
    print("Reading from file '{}'".format(pathname))

    df = pd.read_csv(pathname, header=0, parse_dates=[1], index_col=1, squeeze=True)
    print("Loaded DataFrame from CSV.")
    return df

###############################################################################

folder = 'data'

#url = 'https://www.cryptodatadownload.com/cdd/gemini_BTCUSD_1hr.csv'
#download_file(url, folder)

filename = 'gemini_ETHUSD_1hr.csv'
df = read_historical(filename, folder)

print(len(df))
print(df.columns)
print(df)

