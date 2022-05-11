from account_book.dao.dao_utils import load_sql_file, select_list, insert, update, delete
from django.conf import settings

BASE_DIR = getattr(settings, 'BASE_DIR', '')

def get_main_list(param):
    sql_file = 'account_book/sql/get_main_list.sql'
    return select_list(sql_file, param)

def get_category_sum(param):
    sql_file = 'account_book/sql/get_category_sum.sql'
    return select_list(sql_file, param)

def get_category_seq_sum(param):
    sql_file = 'account_book/sql/get_category_seq_sum.sql'
    return select_list(sql_file, param)

def get_division_sum(param):
    sql_file = 'account_book/sql/get_division_sum.sql'
    return select_list(sql_file, param)

def get_member_sum(param):
    sql_file = 'account_book/sql/get_member_sum.sql'
    return select_list(sql_file, param)

def get_fixed_price_sum(param):
    sql_file = 'account_book/sql/get_fixed_price_sum.sql'
    return select_list(sql_file, param)

def get_division_sum_daily(param):
    sql_file = 'account_book/sql/get_division_sum_daily.sql'
    return select_list(sql_file, param)

def get_expense_sum_daily(param):
    sql_file = 'account_book/sql/get_expense_sum_daily.sql'
    return select_list(sql_file, param)

def get_my_asset_list(param):
    sql_file = BASE_DIR + '/account_book/sql/get_my_asset_list.sql'
    return select_list(sql_file, param)

def get_asset_list():
    sql_file = 'account_book/sql/get_asset_list.sql'
    return select_list(sql_file, None)

def insert_my_asset(param):
    sql_file = 'account_book/sql/insert_my_asset.sql'
    insert(sql_file, param)

def update_my_asset(param):
    sql_file = 'account_book/sql/update_my_asset.sql'
    update(sql_file, param)

def delete_my_asset(param):
    sql_file = 'account_book/sql/delete_my_asset.sql'
    delete(sql_file, param)

def insert_my_asset_accum(param):
    sql_file = BASE_DIR + '/account_book/sql/insert_my_asset_accum.sql'
    insert(sql_file, param)

def get_my_asset_accum_list(param):
    sql_file = 'account_book/sql/get_my_asset_accum_list.sql'
    return select_list(sql_file, param)