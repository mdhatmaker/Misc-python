import pandas as pd
import json


exchanges_filter_all = ["NYMEX", "CME", "NASDAQ", "EEXP", "DTN", "ENID", "NYSE", "EEXE", "EEXN", "FTSE", "SGX", "CME-FL", "CBOT", "MGE", "NFX", "ICEFU", "ICEFC", "KCBOT", "ICEEF", "ICEEC", "KBCB", "MGKB", "MGCB", "COMEX", "CFE", "PK_SHEETS", "DJ", "OPRA", "NYSE_MKT", "ASXCM", "BMF", "BATS", "TENFORE", "CMEUR", "SAFEX", "CBOE", "EUREX", "FXCM", "BLOOMBERG", "ICEENDEX", "CVE", "TSE", "ENCOM", "CFTC", "ICEEA", "DCE", "ELSPOT", "N2EX", "CANTOR", "MDEX", "MCX", "LSE", "LME", "SGXAC", "RUSSELL-FL", "RUSSELL", "EEXC", "TOCOM", "USDA", "GRNST", "WASDE", "EOXCOR", "EOXNGF", "EOXPWF", "ZCE"]
exchanges_filter_main = ["NYMEX", "CME", "DTN", "CME-FL", "CBOT", "COMEX", "CFE", "CBOE", "EUREX", "FXCM", "LME", "TOCOM"]


def print_data(dfx):
    for (ix,row) in dfx.iterrows():
        print "{0:10} {1:10} {2}".format(row['Symbol'], row['Exchange'], row['Description'])
    print "count:", dfx.shape[0]

def search_symbol(text, print_results=True, security_type='FUTURE', allow_mixed_case=False, exchange_filter=exchanges_filter_main):
    if allow_mixed_case == True:
        txt = text
    else:
        txt = text.upper()
    dfx = df[(df.Symbol.str.contains(txt))&(df.SecurityType==security_type)]
    dfx = dfx[dfx.Exchange.isin(exchange_filter)]
    if print_results:
        print_data(dfx)
    return dfx

def search_description(text, print_results=True, security_type='FUTURE', allow_mixed_case=False, exchange_filter=exchanges_filter_main):
    if allow_mixed_case == True:
        txt = text
    else:
        txt = text.upper()
    dfx = df[(df.Description.str.contains(txt))&(df.SecurityType==security_type)]
    dfx = dfx[dfx.Exchange.isin(exchange_filter)]
    if print_results:
        print_data(dfx)
    return dfx

################################################################################

# Read exchanges from JSON file
#f = open('exchanges.json', 'r')
#all_exchanges = json.load(f)
#f.close()

symbol_filename = "mktsymbols_v2.txt"
f = open(symbol_filename, 'r')

symbols = {}

print "Reading symbols. . .",

#exchanges = []

rows = []

count = 0
line = f.readline()
# skip first line of file which contains column headers
# SYMBOL	DESCRIPTION	EXCHANGE	LISTED MARKET	SECURITY TYPE	SIC	FRONTMONTH	NAICS
line = f.readline()
while line:
    count += 1
    if count % 100000 == 0:
        print ".",
    line = line.strip('\n')
    #print line
    splits = line.split('\t')
    
    #exchange = splits[2]
    #if not exchange in exchanges:
    #    print exchange
    #    exchanges.append(exchange)

    #if exchange in exchanges_filter:
    #    rows.append(splits)

    rows.append(splits)
    
    line = f.readline()
f.close()
print

print "Done. Symbol count = {0:,}.".format(count)

# Write exchanges to JSON file
#f = open('exchanges.json', 'w')
#json.dump(exchanges, f)
#f.close()
# SYMBOL	DESCRIPTION	EXCHANGE	LISTED MARKET	SECURITY TYPE	SIC	FRONTMONTH	NAICS

df = pd.DataFrame(rows, columns=['Symbol', 'Description', 'Exchange', 'ListedMarket', 'SecurityType', 'SIC', 'FrontMonth', 'NAICS'])

print "\nExchanges:", df['Exchange'].unique()
print "\nListed Markets:", df['ListedMarket'].unique()
print "\nSecurity Types:", df['SecurityType'].unique()
print

# Search for FUTURE whose symbol contains 'ZN'
#dfx = df[(df.Symbol.str.contains('ZN'))&(df.SecurityType=='FUTURE')]

# Search descriptions for 'YEN'
#dfx = df[(df.Description.str.contains('YEN'))&(df.SecurityType=='FUTURE')]

print "Use 'search_symbol(text)' or 'search_description(text)' to search symbols."

# Search for an INDEX with 'VOLATILITY' in its description
#dfx = search_description('VOLATILITY', security_type='INDEX')

