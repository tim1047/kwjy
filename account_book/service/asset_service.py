import FinanceDataReader as fdr
import pyupbit
import datetime


def get_stock_price(ticker, dt):
    df_stock = fdr.DataReader(ticker, dt, dt)
    
    if len(df_stock) == 0:
        dt_date = datetime.datetime.strptime(dt, '%Y%m%d')
        dt = dt_date - datetime.timedelta(days=7)
        df_stock = fdr.DataReader(ticker, dt).tail(1)
    return int(df_stock['Close'][0])

def get_crypto_price(ticker, dt):
    df_crypto = pyupbit.get_ohlcv('KRW-' + ticker, count=1, interval='day')
    return int(df_crypto['close'][0])

def get_usd_krw_rate(dt):
    df_usd = fdr.DataReader('USD/KRW', dt, dt)
    return int(df_usd['Close'][0])