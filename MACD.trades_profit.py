import os
import pandas as pd;


def display_profit(filename):
    df = pd.read_csv(filename)

    df['x'] = df['Size'] * df['Price']
    count = df.shape[0]
    df.loc[count-1, 'Size'] = 0.1

    #print df

    dfs = df[df.Side=='sell']
    dfb = df[df.Side=='buy']

    sellQty = dfs['Size'].sum()
    avgSell = dfs['x'].sum() / sellQty
    buyQty = dfb['Size'].sum()
    avgBuy = dfb['x'].sum() / buyQty
    profit = (avgSell - avgBuy)
    unitSize = 0.1
    profitPct = round((profit / unitSize) * 100, 2)
    if abs(profitPct) > 5:
        print filename
        print "{}% {}   SELL qty:{} avg_price:{}   BUY qty:{} avg_price:{}\n".format(profitPct, profit, sellQty, avgSell, buyQty, avgBuy)
    return

def getTradeFilesLike(path, lookFor):
    files = []
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)) and f.startswith(lookFor):  # '001_MN_DX' in f:
            files.append(f)
    return sorted(files)


tradesDir = "/Users/michael/Dropbox/dev/csharp"
tradesDir += "/CryptoMania/CryptoMania/bin/Debug/netcoreapp2.0/DATA"
#filename += "/BINANCE.MACD.trades.NEOETH.5.180218002046.DF.csv"
#filename = dir + "/BINANCE.MACD.trades.NEOETH.60.180218010449.DF.csv"

#display_profit(tradesDir + "/BINANCE.MACD.trades.NEOETH.5.180218002046.DF.csv")
#display_profit(tradesDir + "/BINANCE.MACD.trades.NEOETH.60.180218010449.DF.csv")


files = getTradeFilesLike(tradesDir, "BINANCE.MACD.trades.")
for f in files:
    pathname = os.path.join(tradesDir, f)
    display_profit(pathname)


