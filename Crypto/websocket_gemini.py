from geminiwss_client import GeminiWss
import time


wss = GeminiWss()

wss.subscribe('marketdata/btcusd')
wss.subscribe('marketdata/ethbtc')
wss.subscribe('marketdata/ethusd')

time.sleep(30)

while not wss.endpoint_qs['marketdata/btcusd'].empty():
    print('BTCUSD', wss.endpoint_qs['marketdata/btcusd'].get())

while not wss.endpoint_qs['marketdata/ethbtc'].empty():
    print('ETHBTC', wss.endpoint_qs['marketdata/ethbtc'].get())

while not wss.endpoint_qs['marketdata/ethusd'].empty():
    print('ETHUSD', wss.endpoint_qs['marketdata/ethusd'].get())
    
