from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
from requests.exceptions import * 
#
# dummy keys de cuenta binance sin saldo y login a Binance
def binanceConnect():
    global client
    key = ""
    secret = ""
    client = Client(key, secret)
#
def binancePrice(sym):
    try:
        klines = client.get_historical_klines(sym, Client.KLINE_INTERVAL_1MINUTE, "now")
    except BinanceAPIException as bi:
        print(bi)
        errbin=bi.status_code
        if errbin==418:
            print("IP auto-banned")
            exit
        elif errbin==429:
            print("Breaking request limit")
            exit
    except Exception as ex:
        print(ex)
    print(klines)
    most_recent = klines.pop()
# Close price goes on 4th position
    price = float(most_recent[4])
    print("sym:",sym,"=",price)
    return price
#
binanceConnect()
binancePrice("BTCUSDT")
binancePrice("BNBUSDT")
binancePrice("BNBBTC")