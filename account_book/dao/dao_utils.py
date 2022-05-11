from django.db import connection
from django.conf import settings


BASE_DIR = getattr(settings, 'BASE_DIR', '')

def load_sql_file(sql_file):
    with open(BASE_DIR + '/' + sql_file, 'r', encoding='utf8') as f:
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
