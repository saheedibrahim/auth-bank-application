def withdrawal_operation(get_balance):
    print("Withdrawal")
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdraw amount from current balance
    # display current balance

    previous_balance = int(get_previous_balance(get_balance))
    get_amount_to_deposit = int(input("Insert the amount to deposit \n"))
    if previous_balance > get_amount_to_deposit:
        balance = previous_balance - get_amount_to_deposit
        print(balance)
        return balance
    else:
        print("invalid amount inputted")


def deposit_operation(get_balance):
    print("Deposits operation")
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance

    previous_balance = get_previous_balance(get_balance)
    get_amount_to_deposit = int(input("Insert the amount to deposit \n"))
    current_balance = int(previous_balance) + get_amount_to_deposit

    print(current_balance)
    # amount_new = get_current_balance(current_balance)
    return current_balance


def get_current_balance(balance):
    get_deposit_operation = deposit_operation(balance)


def get_previous_balance(user_details):
    # if database.does_account_number_exist(user_details):
    user = str.split(user_details, ',')
    return user[4]
    # else:
    #     return user_details
    # if balance == user[4]:

    # user_details_raw = database.read(int(account_number_v))

    # return user
    # user_details[4] = balance

