import FinanceDataReader as fdr
from pycoingecko import CoinGeckoAPI
import datetime
import yfinance as yf

cg = CoinGeckoAPI()

def get_stock_price(ticker, dt):
    df_stock = fdr.DataReader(ticker, dt, dt)
    
    if len(df_stock) == 0:
        dt_date = datetime.datetime.strptime(dt, '%Y%m%d')
        dt = dt_date - datetime.timedelta(days=7)
        df_stock = fdr.DataReader(ticker, dt).tail(1)
    return float(df_stock['Close'][0])

def get_crypto_price(coin_id, dt):
    crypto_price = cg.get_price(ids=coin_id, vs_currencies='usd')
    return float(crypto_price.get(coin_id, {}).get('usd', '0'))

def get_usd_krw_rate(dt):
    dt = datetime.datetime.strftime(datetime.datetime.strptime(dt, '%Y%m%d'), '%Y-%m-%d')
    df_usd = yf.download(['USDKRW=X'], start=dt, end=dt)

    if len(df_usd) == 0:
        dt_date = datetime.datetime.strftime(datetime.datetime.strptime(dt, '%Y-%m-%d') - datetime.timedelta(days=7), '%Y-%m-%d')
        df_usd = fdr.DataReader('USD/KRW', start=dt_date, end=dt)
    return int(df_usd['Close'][-1])