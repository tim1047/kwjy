from account_book.dao.dao_utils import load_sql_file, select_list


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
