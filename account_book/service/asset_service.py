import FinanceDataReader as fdr
import pyupbit


def get_stock_price(ticker, dt):
    df_stock = fdr.DataReader(ticker, dt, dt)
    return int(df_stock['Close'][0])

def get_crypto_price(ticker, dt):
    df_crypto = pyupbit.get_ohlcv('KRW-' + ticker, count=1, interval='day')
    return int(df_crypto['close'][0])
