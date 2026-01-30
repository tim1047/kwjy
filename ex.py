import yfinance as yf
import datetime
import FinanceDataReader as fdr



def get_usd_krw_rate(dt):
    dt = datetime.datetime.strftime(datetime.datetime.strptime(dt, '%Y%m%d'), '%Y-%m-%d')
    # df_usd = yf.download(['USDKRW=X'], start=dt)
    df_usd = fdr.DataReader('USD/KRW', dt, dt)

    if len(df_usd) == 0:
        dt_date = datetime.datetime.strftime(
            datetime.datetime.strptime(dt, '%Y-%m-%d') - datetime.timedelta(days=7), '%Y-%m-%d'
        )
        # df_usd = yf.download(['USDKRW=X'], start=dt_date)
        df_usd = fdr.DataReader('USD/KRW', dt_date, dt)
    return int(df_usd['Close'].iloc[-1].item())

def get_jpy_krw_rate(dt):
    dt = datetime.datetime.strftime(datetime.datetime.strptime(dt, '%Y%m%d'), '%Y-%m-%d')
    # df_jpy = yf.download(['JPYKRW=X'], start=dt)
    df_jpy = fdr.DataReader('JPY/KRW', dt, dt)

    if len(df_jpy) == 0:
        dt_date = datetime.datetime.strftime(
            datetime.datetime.strptime(dt, '%Y-%m-%d') - datetime.timedelta(days=7), '%Y-%m-%d'
        )
        # df_jpy = yf.download(['JPYKRW=X'], start=dt_date)
        df_jpy = fdr.DataReader('JPY/KRW', dt_date, dt)
    return float(df_jpy['Close'].iloc[-1].item())


print(get_usd_krw_rate('20260130'))
print(get_jpy_krw_rate('20260130'))