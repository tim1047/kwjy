from django.db import connection
from account_book.dao.dao_utils import load_sql_file


def get_division_list():
    sql_file = 'account_book/sql/get_division_list.sql'

    with connection.cursor() as cursor:
        sql = load_sql_file(sql_file)

        cursor.execute(sql)

        columns = [col[0] for col in cursor.description]
        result = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return result

def get_member_list():
    sql_file = 'account_book/sql/get_member_list.sql'

    with connection.cursor() as cursor:
        sql = load_sql_file(sql_file)

        cursor.execute(sql)

        columns = [col[0] for col in cursor.description]
        result = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return result

def get_payment_list(param):
    sql_file = 'account_book/sql/get_payment_list.sql'

    with connection.cursor() as cursor:
        sql = load_sql_file(sql_file)

        cursor.execute(sql, param)

        columns = [col[0] for col in cursor.description]
        result = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return result

def get_category_list_by_division_id(param):
    sql_file = 'account_book/sql/get_category_list_by_division_id.sql'

    with connection.cursor() as cursor:
        sql = load_sql_file(sql_file)

        cursor.execute(sql, param)

        columns = [col[0] for col in cursor.description]
        result = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return result

def get_category_seq_list(param):
    sql_file = 'account_book/sql/get_category_seq_list.sql'

    with connection.cursor() as cursor:
        sql = load_sql_file(sql_file)

        cursor.execute(sql, param)

        columns = [col[0] for col in cursor.description]
        result = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return result

def insert_account(param):
    sql_file = 'account_book/sql/insert_account.sql'

    with connection.cursor() as cursor:
        sql = load_sql_file(sql_file)
        cursor.execute(sql, param)
        
