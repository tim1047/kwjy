import account_book.service.main_account_book_service as main_account_book_service
import datetime

def asset_accum():
    proc_dt = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    request_param = {
        'procDt': proc_dt
    }
    try:
        main_account_book_service.insert_my_asset_accum(request_param)
    except Exception as e:
        print(e)