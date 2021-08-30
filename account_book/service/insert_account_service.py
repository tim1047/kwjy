import account_book.dao.insert_account_dao as insert_account_dao


def get_division_list():
    return insert_account_dao.get_division_list()

def get_member_list():
    return insert_account_dao.get_member_list()

def get_payment_list(param):
    return insert_account_dao.get_payment_list(param)

def get_category_list_by_division_id(param):
    return insert_account_dao.get_category_list_by_division_id(param)

def get_category_seq_list(param):
    return insert_account_dao.get_category_seq_list(param)

def insert_account(param):
    insert_account_dao.insert_account(param)

def update_account(param):
    insert_account_dao.update_account(param)
    
def delete_account(param):
    insert_account_dao.delete_account(param)


