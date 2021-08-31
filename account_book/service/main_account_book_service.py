import account_book.dao.main_account_book_dao as main_account_book_dao


def get_main_list():
    return main_account_book_dao.get_main_list()

def get_category_sum(param):
    return main_account_book_dao.get_category_sum(param)

def get_category_seq_sum(param):
    return main_account_book_dao.get_category_seq_sum(param)

