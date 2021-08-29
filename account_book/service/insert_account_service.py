import account_book.dao.insert_account_dao as insert_account_dao


def get_division_list():
    return insert_account_dao.get_division_list()


def get_category_list_by_division_id(param):
    return insert_account_dao.get_category_list_by_division_id(param)

