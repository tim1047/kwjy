import datetime

import FinanceDataReader as fdr
import investpy
import pandas_datareader as pdr
import yfinance as yf
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


def get_stock_price(ticker, dt):
    import ssl

    ssl._create_default_https_context = ssl._create_unverified_context

    try:
        df_stock = fdr.DataReader(ticker, dt, dt)
    except Exception as e:
        dt_date = datetime.datetime.strptime(dt, '%Y%m%d')
        dt = dt_date - datetime.timedelta(days=7)
        df_stock = fdr.DataReader(ticker, dt).tail(1)
    return float(df_stock['Close'][0])


def get_pdr_stock_price(ticker, dt, datasource='yahoo'):
    try:
        dt = datetime.datetime.strftime(datetime.datetime.strptime(dt, '%Y%m%d'), '%Y-%m-%d')
        df_stock = pdr.DataReader(ticker, datasource, start=dt)
    except KeyError as e:
        dt_date = datetime.datetime.strftime(
            datetime.datetime.strptime(dt, '%Y-%m-%d') - datetime.timedelta(days=7), '%Y-%m-%d'
        )
        df_stock = pdr.DataReader(ticker, datasource, start=dt_date)
    return float(df_stock['Close'][-1])


def get_japan_stock_price(ticker):
    df_stock = investpy.get_stock_recent_data(stock=ticker, country='japan', order='descending')
    return float(df_stock.iloc[0]['Close'])


def get_crypto_price(coin_id, dt):
    crypto_price = cg.get_price(ids=coin_id, vs_currencies='usd')
    return float(crypto_price.get(coin_id, {}).get('usd', '0'))


def get_usd_krw_rate(dt):
    dt = datetime.datetime.strftime(datetime.datetime.strptime(dt, '%Y%m%d'), '%Y-%m-%d')
    df_usd = yf.download(['USDKRW=X'], start=dt)

    if len(df_usd) == 0:
        dt_date = datetime.datetime.strftime(
            datetime.datetime.strptime(dt, '%Y-%m-%d') - datetime.timedelta(days=7), '%Y-%m-%d'
        )
        df_usd = yf.download(['USDKRW=X'], start=dt_date)
    return int(df_usd['Close'][-1])


def get_jpy_krw_rate(dt):
    dt = datetime.datetime.strftime(datetime.datetime.strptime(dt, '%Y%m%d'), '%Y-%m-%d')
    df_jpy = yf.download(['JPYKRW=X'], start=dt)

    if len(df_jpy) == 0:
        dt_date = datetime.datetime.strftime(
            datetime.datetime.strptime(dt, '%Y-%m-%d') - datetime.timedelta(days=7), '%Y-%m-%d'
        )
        df_jpy = yf.download(['JPYKRW=X'], start=dt_date)
    return float(df_jpy['Close'][-1])
