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

def get_expense_sum_daily(param):
    result_list = [['일자']]

    expense_sum_daily_list = main_account_book_dao.get_expense_sum_daily(param)

    strt_dt = param.get('strt_dt')
    end_dt = param.get('end_dt')

    strt_year = int(strt_dt[0:4])
    strt_month = int(strt_dt[4:6])
    end_year = int(end_dt[0:4])
    end_month = int(end_dt[4:6])

    year_diff = end_year - strt_year
    month_diff = end_month - strt_month
    diff = year_diff * 12 + month_diff + 1

    account_dt_mpng = {}
    for i in range(0, diff):
        val = str(strt_year) + '0' + str(strt_month) if strt_month < 10 else str(strt_month) 
        account_dt_mpng[val] = i
        result_list[0].append(val)
        
        if strt_month == 12:
            strt_year += 1
            strt_month = 1
        strt_month += 1

    expense_sum_daily_info = {}
    for expense_sum_daily in expense_sum_daily_list:    
        day = int(expense_sum_daily.get('account_dd'))

        if expense_sum_daily_info.get(day, None) is None:
            expense_sum_daily_info[day] = []
            for i in range(0, diff):
                expense_sum_daily_info[day].append(0)
        expense_sum_daily_info[day][account_dt_mpng[expense_sum_daily.get('account_yyyymm')]] = (expense_sum_daily.get('sum_price'))

    for i in range(1, 32):
        if expense_sum_daily_info.get(i, None) is None:
            expense_sum_daily_info[i] = []
            for ii in range(0, diff):
                expense_sum_daily_info[i].append(0)

        cur_expense_sum_list = expense_sum_daily_info.get(i)
        prev_expense_sum_list = expense_sum_daily_info.get(i - 1, [])

        if prev_expense_sum_list:
            for j in range(0, len(prev_expense_sum_list)):
                cur_expense_sum_list[j] += prev_expense_sum_list[j]            
    
    for i in range(1, 32):
        result_info_list = expense_sum_daily_info.get(i)
        temp = list()
        temp.append(str(i))
        temp.extend(result_info_list)
        result_list.append(temp)
    return result_list
