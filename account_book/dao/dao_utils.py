def load_sql_file(sql_file):
    with open(sql_file, 'r', encoding='utf8') as f:
        line = f.read()
    return line
