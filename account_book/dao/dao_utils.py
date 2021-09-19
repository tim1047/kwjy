from django.db import connection


def load_sql_file(sql_file):
    with open(sql_file, 'r', encoding='utf8') as f:
        line = f.read()
    return line

def select_list(sql, param=None):
    with connection.cursor() as cursor:
        sql = load_sql_file(sql)

        if param:
            cursor.execute(sql, param)
        else:
            cursor.execute(sql)

        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

def insert(sql, param):
    with connection.cursor() as cursor:
        sql = load_sql_file(sql)
        cursor.execute(sql, param)

def update(sql, param):
    with connection.cursor() as cursor:
        sql = load_sql_file(sql)
        cursor.execute(sql, param)

def delete(sql, param):
    with connection.cursor() as cursor:
        sql = load_sql_file(sql)
        cursor.execute(sql, param)
