import pandas as pd

pd.set_option("display.width", 160)

_df = pd.read_csv("/Users/michael/Documents/GitHub/source/csharp/CryptoConsole/bin/debug/netcoreapp2.0/data.hitbtc_tickers.txt")

df = _df[_df.Symbol=="BCNBTC"]
print(df)
