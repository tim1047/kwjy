from account_book.dao.dao_utils import load_sql_file, select_list, insert, delete, update


def get_division_list():
    sql_file = 'account_book/sql/get_division_list.sql'
    return select_list(sql_file)

def get_member_list():
    sql_file = 'account_book/sql/get_member_list.sql'
    return select_list(sql_file)

def get_payment_list(param):
    sql_file = 'account_book/sql/get_payment_list.sql'
    return select_list(sql_file)

def get_category_list_by_division_id(param):
    sql_file = 'account_book/sql/get_category_list_by_division_id.sql'
    return select_list(sql_file, param)

def get_category_seq_list(param):
    sql_file = 'account_book/sql/get_category_seq_list.sql'
    return select_list(sql_file, param)

def insert_account(param):
    sql_file = 'account_book/sql/insert_account.sql'
    insert(sql_file, param)

def update_account(param):
    sql_file = 'account_book/sql/update_account.sql'
    update(sql_file, param)

def delete_account(param):
    sql_file = 'account_book/sql/delete_account.sql'
    delete(sql_file, param)

