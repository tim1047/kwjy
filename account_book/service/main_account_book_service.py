import account_book.dao.main_account_book_dao as main_account_book_dao


def get_main_list(param):
    return main_account_book_dao.get_main_list(param)

def get_category_sum(param):
    return main_account_book_dao.get_category_sum(param)

def get_category_seq_sum(param):
    return main_account_book_dao.get_category_seq_sum(param)

def get_division_sum(param):
    division_sum_list = main_account_book_dao.get_division_sum(param)
    income, expense, interest, invest, invest_rate = 0, 0, 0, 0, 0.0
    
    for division_sum in division_sum_list:
        division_id = division_sum.get('division_id', None)
        if division_id == '1':
            income = division_sum.get('total_sum_price', 0)
        elif division_id == '2':
            invest = division_sum.get('total_sum_price', 0)
        elif division_id == '3':
            expense = division_sum.get('total_sum_price', 0)
    interest = income - expense

    if income > 0:
        invest_rate = round(invest / income * 100, 1)
    
    result = {
        'income': int(income),
        'interest': int(interest),
        'expense': int(expense),
        'invest': int(invest),
        'invest_rate': str(invest_rate) + '%'
    }
    return result

def get_member_sum(param):
    return main_account_book_dao.get_member_sum(param)

def get_fixed_price_sum(param):
    return main_account_book_dao.get_fixed_price_sum(param)

def get_division_sum_daily(param):
    result_list = []
    
    division_sum_daily_list = main_account_book_dao.get_division_sum_daily(param)
    division_sum_daily_info = {}
    for item in division_sum_daily_list:
        if not division_sum_daily_info.get(item.get('account_dt'), {}):
            division_sum_daily_info[item.get('account_dt')] = {
                'income': 0,
                'invest': 0,
                'expense': 0,
                'account_dt': item.get('account_dt')
            }
        if item.get('division_id', '') == '1':
            division_sum_daily_info[item.get('account_dt')]['income'] = item.get('sum_price', 0)
        elif item.get('division_id', '') == '2':
            division_sum_daily_info[item.get('account_dt')]['invest'] = item.get('sum_price', 0)
        elif item.get('division_id', '') == '3':
            division_sum_daily_info[item.get('account_dt')]['expense'] = item.get('sum_price', 0)
    
    for key, val in division_sum_daily_info.items():
        result_list.append(val)
    return result_list
