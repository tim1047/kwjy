import asyncio
import datetime
from datetime import timedelta

from dateutil import relativedelta
from django.db import transaction

import account_book.dao.main_account_book_dao as main_account_book_dao
import account_book.service.asset_service as asset_service


def get_main_list(param):
    return main_account_book_dao.get_main_list(param)


def get_category_sum(param):
    category_sum_list = main_account_book_dao.get_category_sum(param)
    category_sum_dict = {}
    total_sum_price = 0

    for category_sum in category_sum_list:
        category_id = category_sum.get("category_id", "")

        if category_id:
            total_sum_price += category_sum.get("sum_price", 0)

            if category_id not in category_sum_dict:
                category_sum_dict[category_id] = {
                    "category_id": category_id,
                    "category_nm": category_sum.get("category_nm", ""),
                    "division_id": category_sum.get("division_id", ""),
                    "sum_price": category_sum.get("sum_price", 0),
                    "data": [
                        {
                            "category_seq": category_sum.get("category_seq", ""),
                            "category_seq_nm": category_sum.get("category_seq_nm", ""),
                            "sum_price": category_sum.get("sum_price", 0),
                        }
                    ],
                }
            else:
                category_sum_dict[category_id]["sum_price"] += category_sum.get("sum_price", 0)
                category_sum_dict[category_id]["data"].append(
                    {
                        "category_seq": category_sum.get("category_seq", ""),
                        "category_seq_nm": category_sum.get("category_seq_nm", ""),
                        "sum_price": category_sum.get("sum_price", 0),
                    }
                )
            category_sum_dict[category_id]["total_sum_price"] = total_sum_price
    return list(category_sum_dict.values())


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
        'invest_rate': str(invest_rate) + '%',
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
                'account_dt': item.get('account_dt'),
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
        val = str(strt_year) + ('0' + str(strt_month) if strt_month < 10 else str(strt_month))
        account_dt_mpng[val] = i
        result_list[0].append(val[0:4] + '년 ' + val[4:6] + '월')

        if strt_month == 12:
            strt_year += 1
            strt_month = 0
        strt_month += 1

    expense_sum_daily_info = {}
    for expense_sum_daily in expense_sum_daily_list:
        day = int(expense_sum_daily.get('account_dd'))

        if expense_sum_daily_info.get(day, None) is None:
            expense_sum_daily_info[day] = []
            for i in range(0, diff):
                expense_sum_daily_info[day].append(0)
        expense_sum_daily_info[day][account_dt_mpng[expense_sum_daily.get('account_yyyymm')]] = expense_sum_daily.get(
            'sum_price'
        )

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
        temp.append(str(i) + '일')
        temp.extend(result_info_list)
        result_list.append(temp)
    return result_list


def get_my_asset_list(param):
    result_info = {'data': {}}
    proc_dt = param.get('strt_dt')
    tot_sum_price, tot_net_worth_sum_price, tot_cashable_sum_price = 0, 0, 0
    usd_krw_rate = asset_service.get_usd_krw_rate(proc_dt)
    param['usd_krw_rate'] = usd_krw_rate
    jpy_krw_rate = asset_service.get_jpy_krw_rate(proc_dt)
    param['jpy_krw_rate'] = jpy_krw_rate

    my_asset_list = []
    if param.get('type', 'delayed') == 'delayed':
        my_asset_list = get_delayed_my_asset_list(param)
    else:
        my_asset_list = get_realtime_my_asset_list_async(param)

    my_asset_group_info = {}

    for my_asset in my_asset_list:
        sum_price = my_asset['sum_price']

        if my_asset.get('asset_id') == '6':
            tot_net_worth_sum_price -= sum_price
        else:
            tot_sum_price += sum_price
            tot_net_worth_sum_price += sum_price

        if my_asset.get("cashable_yn", "Y") == "Y":
            tot_cashable_sum_price += sum_price

        asset_id = my_asset.get('asset_id')
        if result_info.get('data').get(asset_id, None) is None:
            result_info['data'][asset_id] = {'asset_nm': my_asset.get('asset_nm'), 'asset_tot_sum_price': 0, 'data': []}

        result_info['data'][asset_id]['asset_tot_sum_price'] += sum_price

        my_asset_group_id = my_asset.get('my_asset_group_id', '')
        if my_asset_group_id == '0':
            result_info['data'][asset_id]['data'].append(my_asset)
        else:
            if my_asset_group_info.get(my_asset_group_id, None) is None:
                my_asset_group_info[my_asset_group_id] = {
                    'my_asset_group_id': my_asset_group_id,
                    'my_asset_group_nm': my_asset.get('my_asset_group_nm', ''),
                    'my_asset_nm': my_asset.get('my_asset_nm', ''),
                    'asset_id': asset_id,
                    'asset_nm': my_asset.get('asset_nm', ''),
                    'sum_price': 0,
                    'qty': my_asset['qty'],
                    'data': [],
                }
            my_asset_group_info[my_asset_group_id]['sum_price'] += sum_price
            my_asset_group_info[my_asset_group_id]['data'].append(my_asset)

    for _, value in my_asset_group_info.items():
        asset_id = value.get('asset_id')
        result_info['data'][asset_id]['data'].append(value)

    result_info['tot_sum_price'] = tot_sum_price
    result_info['tot_net_worth_sum_price'] = tot_net_worth_sum_price
    result_info['tot_cashable_sum_price'] = tot_cashable_sum_price
    result_info['usd_krw_rate'] = usd_krw_rate
    result_info['jpy_krw_rate'] = jpy_krw_rate
    result_info['my_asset_accum_dts'] = my_asset_list[0]['my_asset_accum_dts'].strftime("%Y-%m-%d %H:%M:%S")

    for _, val in result_info.get('data').items():
        ordered_list = sorted(val.get('data'), key=lambda d: d['sum_price'], reverse=True)
        val['data'] = ordered_list

    return result_info


@transaction.atomic()
def get_realtime_my_asset_list_async(param):
    proc_dt = param.get('strt_dt')
    param['my_asset_id'] = None

    my_asset_list = main_account_book_dao.get_my_asset_list(param)

    async def main(my_asset_list):
        tasks = [asyncio.create_task(get_price_async(my_asset, proc_dt)) for my_asset in my_asset_list]
        my_asset_list = await asyncio.gather(*tasks)

    asyncio.run(main(my_asset_list))

    param['procDt'] = proc_dt
    main_account_book_dao.delete_my_asset_accum(param)

    for my_asset in my_asset_list:
        my_asset['accum_dt'] = proc_dt[0:6]
        if my_asset.get('exchange_rate_yn', 'N') == 'Y':
            if my_asset.get('asset_id') == '7':
                my_asset['sum_price'] *= param['jpy_krw_rate']
                my_asset['price'] *= param['jpy_krw_rate']
            else:
                my_asset['sum_price'] *= param['usd_krw_rate']
                my_asset['price'] *= param['usd_krw_rate']
        my_asset['sum_price'] = int(my_asset['sum_price'])
        my_asset['price'] = int(my_asset['price'])

        main_account_book_dao.insert_my_asset_accum(my_asset)

    return my_asset_list


def get_delayed_my_asset_list(param):
    param['proc_dt'] = param.get('strt_dt')[0:6]
    return main_account_book_dao.get_delayed_my_asset_list(param)


def get_asset_list():
    return main_account_book_dao.get_asset_list()


def insert_my_asset(param):
    return main_account_book_dao.insert_my_asset(param)


def update_my_asset(param):
    main_account_book_dao.update_my_asset(param)

    proc_dt = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    my_asset_list = main_account_book_dao.get_my_asset_list(param)

    async def main(my_asset_list):
        tasks = [asyncio.create_task(get_price_async(my_asset, proc_dt)) for my_asset in my_asset_list]
        my_asset_list = await asyncio.gather(*tasks)

    asyncio.run(main(my_asset_list))

    param['procDt'] = proc_dt

    for my_asset in my_asset_list:
        my_asset['accum_dt'] = proc_dt[0:6]
        main_account_book_dao.insert_my_asset_accum(my_asset)


def delete_my_asset(param):
    return main_account_book_dao.delete_my_asset(param)


def get_division_sum_by_division_id(param):
    proc_dt = param.get('proc_dt', '')
    division_id = param.get('division_id', '')

    year = datetime.datetime.strptime(proc_dt, '%Y%m').year
    month = datetime.datetime.strptime(proc_dt, '%Y%m').month

    result_list = []
    result = {}
    avg_total_sum_price = 0
    total_month = 6

    month = month + 1
    for i in range(0, total_month):
        if month == 1:
            month = 12
            year = year - 1
        else:
            month = month - 1

        first_day = datetime.datetime(year=year, month=month, day=1).date()
        last_day = first_day + relativedelta.relativedelta(months=1) - timedelta(days=1)

        param = {
            'strt_dt': datetime.datetime.strftime(first_day, '%Y%m%d'),
            'end_dt': datetime.datetime.strftime(last_day, '%Y%m%d'),
        }
        division_sum_list = main_account_book_dao.get_division_sum(param)
        for division_sum in division_sum_list:
            if division_sum.get('division_id', '') == division_id:
                avg_total_sum_price = avg_total_sum_price + division_sum['total_sum_price']

                division_sum['month'] = month
                result_list.append(division_sum)

    result['avg_total_sum_price'] = int(avg_total_sum_price / total_month)
    result['data'] = list(reversed(result_list))
    return result


def get_my_asset_accum(param):
    result_list = []

    strt_dt = param.get('strt_dt', '')
    end_dt = param.get('end_dt', '')

    strt_year = datetime.datetime.strptime(strt_dt, '%Y%m%d').year
    strt_month = datetime.datetime.strptime(strt_dt, '%Y%m%d').month
    end_year = datetime.datetime.strptime(end_dt, '%Y%m%d').year
    end_month = datetime.datetime.strptime(end_dt, '%Y%m%d').month

    diff_month = (end_year - strt_year) * 12 + (end_month - strt_month)
    for i in range(0, diff_month + 1):
        proc_dt = str(strt_year) + str(strt_month).rjust(2, '0')

        strt_month += 1
        if strt_month > 12:
            strt_month = 1
            strt_year += 1

        param['proc_dt'] = proc_dt
        my_asset_accum_list = main_account_book_dao.get_my_asset_accum_list(param)

        total_sum_price = 0
        for my_asset_accum in my_asset_accum_list:
            sum_price = my_asset_accum.get('total_sum_price', 0)
            if my_asset_accum.get('asset_id', '') == '6':
                sum_price *= -1
            total_sum_price += sum_price
            if not my_asset_accum.get('accum_dt', ''):
                my_asset_accum['accum_dt'] = proc_dt

        my_asset_accum_list.insert(
            0, {'accum_dt': proc_dt, 'asset_id': '0', 'asset_nm': '총 자산', 'total_sum_price': int(total_sum_price)}
        )

        my_asset_accum_info = {}
        my_asset_accum_info['data'] = my_asset_accum_list
        my_asset_accum_info['total_sum_price'] = int(total_sum_price)
        my_asset_accum_info['accum_dt'] = proc_dt

        result_list.append(my_asset_accum_info)
    return result_list


@transaction.atomic()
def insert_my_asset_accum(param):
    proc_dt = param.get('procDt', '')
    param['my_asset_id'] = None

    main_account_book_dao.delete_my_asset_accum(param)

    usd_krw_rate = asset_service.get_usd_krw_rate(proc_dt)
    jpy_krw_rate = asset_service.get_jpy_krw_rate(proc_dt)

    my_asset_list = main_account_book_dao.get_my_asset_list(param)
    for my_asset in my_asset_list:
        price = float(my_asset.get('price', 0))
        if my_asset['price_div_cd'] == 'AUTO':
            if my_asset.get('asset_id') == '1' or my_asset.get('asset_id') == '8':
                price = asset_service.get_stock_price(my_asset.get('ticker'), proc_dt)
            elif my_asset.get('asset_id') == '2':
                # price = asset_service.get_pdr_stock_price(my_asset.get('ticker'), proc_dt, datasource='yahoo')
                price = asset_service.get_stock_price(my_asset.get('ticker'), proc_dt)
            elif my_asset.get('asset_id') == '3':
                price = asset_service.get_crypto_price(my_asset.get('coin_id'), None)
            elif my_asset.get('asset_id') == '7':
                price = asset_service.get_japan_stock_price(my_asset.get('ticker'))

        if my_asset['exchange_rate_yn'] == 'Y':
            if my_asset.get('asset_id') == '7':
                price *= jpy_krw_rate
            else:
                price *= usd_krw_rate

        my_asset['accum_dt'] = proc_dt[0:6]
        my_asset['price'] = price
        main_account_book_dao.insert_my_asset_accum(my_asset)


async def get_price_async(my_asset, proc_dt):
    price_div_cd = my_asset.get('price_div_cd')
    price = float(my_asset.get('price', 0))
    qty = float(my_asset.get('qty', 0))

    if price_div_cd == 'AUTO':
        # 가격조회
        loop = asyncio.get_running_loop()
        if my_asset.get('asset_id') == '1' or my_asset.get('asset_id') == '8':
            price = await loop.run_in_executor(
                None, lambda: asset_service.get_stock_price(my_asset.get('ticker'), proc_dt)
            )
        elif my_asset.get('asset_id') == '2':
            # price = await loop.run_in_executor(None, lambda: asset_service.get_pdr_stock_price(my_asset.get('ticker'), proc_dt, datasource='yahoo'))
            price = await loop.run_in_executor(
                None, lambda: asset_service.get_stock_price(my_asset.get('ticker'), proc_dt)
            )
        elif my_asset.get('asset_id') == '3':
            price = await loop.run_in_executor(
                None, lambda: asset_service.get_crypto_price(my_asset.get('coin_id'), None)
            )
            # price = asset_service.get_crypto_price(my_asset.get('coin_id'), None)
        elif my_asset.get('asset_id') == '7':
            price = await loop.run_in_executor(
                None, lambda: asset_service.get_japan_stock_price(my_asset.get('ticker'))
            )

    sum_price = int(price * qty)
    my_asset['sum_price'] = sum_price
    my_asset['price'] = price
    return my_asset
