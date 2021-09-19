from django.db import connection
from account_book.dao.dao_utils import load_sql_file


def get_main_list(param):
    sql_file = 'account_book/sql/get_main_list.sql'

    with connection.cursor() as cursor:
        sql = load_sql_file(sql_file)

        cursor.execute(sql, param)

        columns = [col[0] for col in cursor.description]
        result = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return result

def get_category_sum(param):
    sql_file = 'account_book/sql/get_category_sum.sql'

    with connection.cursor() as cursor:
        sql = load_sql_file(sql_file)

        cursor.execute(sql, param)

        columns = [col[0] for col in cursor.description]
        result = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return result

def get_category_seq_sum(param):
    sql_file = 'account_book/sql/get_category_seq_sum.sql'

    with connection.cursor() as cursor:
        sql = load_sql_file(sql_file)

        cursor.execute(sql, param)

        columns = [col[0] for col in cursor.description]
        result = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return result

def get_division_sum(param):
    sql_file = 'account_book/sql/get_division_sum.sql'

    with connection.cursor() as cursor:
        sql = load_sql_file(sql_file)

        cursor.execute(sql, param)

        columns = [col[0] for col in cursor.description]
        result = [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]
    return result
