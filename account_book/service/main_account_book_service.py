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
    result_list = []
    fixed_price_sum_list = main_account_book_dao.get_fixed_price_sum(param)

    for i in range(0, 6):
        result = {
            'week': i+1,
            'sum_price': 0
        }
        result_list.append(result)

    if fixed_price_sum_list:
        for fixed_price_sum in fixed_price_sum_list:
            week = fixed_price_sum.get('week')
            result_list[week-1] = fixed_price_sum

    return result_list

