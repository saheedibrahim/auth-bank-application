import random
import validation

# register
# - first name, last name, password, email
# - generate user account

# login
# - account-number and password

# bank operations

# initializing the system

database = {
    2644894503: ['Saheed', 'Ibrahim', 'saolabram@gmail.com', 'taajirun', 5000]
}


def init():
    is_valid_option_selected = False
    print("Welcome to bankPHP")
    while not is_valid_option_selected:
        have_account = int(input("Do you have an account with us: 1 (yes) 2 (no): "))
        if have_account == 1:
            is_valid_option_selected = True
            login()
        elif have_account == 2:
            is_valid_option_selected = True
            register()
        else:
            print("You have selected invalid option")


def login():
    print("***** Login *****")
    is_login_successful = False
    while not is_login_successful:
        account_number_from_user = input("What is your account number? \n")
        is_valid_account_number = validation.account_number_validation(account_number_from_user)
        if is_valid_account_number:
            password = input("What is your password? \n")
            for accountNUmber, userDetails in database.items():
                if accountNUmber == int(account_number_from_user):
                    if userDetails[3] == password:
                        is_login_successful = True
                        bank_operation(userDetails)
        else:
            init()
        print("Invalid account or password")


def register():
    print("***** Register *****")
    email = input("What is your email? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    try:
        account_number = generate_account_number()
    except ValueError:
        print("Account generation failed due to internet connection")
    database[account_number] = [first_name, last_name, email, password, 0]
    print("Your account has been created")
    print("== ==== ==== ==== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it save")
    print("== ==== ==== ==== ===")

    login()

def bank_operation(user):
    print("Welcome %s %s" % (user[0], user[1]))
    selected_option = int(input("What would you like to do? (1) deposit (2)withdrawal (3) Logout (4) exit \n"))
    if selected_option == 1:
        deposit_operation(user)
        print("Do you want to perform another transaction?")
        another_transaction = int(input("(1) Yes (2) No \n"))
        if another_transaction == 1:
            bank_operation(user)
        elif another_transaction == 2:
            exit()
        else:
            print("You inputted an invalid option")
    elif selected_option == 2:
        withdrawal_operation(user)
        print("Do you want to perform another transaction?")
        another_transaction = int(input("(1) Yes (2) No \n"))
        if another_transaction == 1:
            bank_operation(user)
        elif another_transaction == 2:
            exit()
        else:
            print("You inputted an invalid option")
    elif selected_option == 3:
        logout()
    elif selected_option == 4:
        exit()
    else:
        print("Invalid option selected")
        bank_operation(user)


def withdrawal_operation(get_balance):
    print("Withdrawal")
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdraw amount from current balance
    # display current balance

    previous_balance = get_current_balance(get_balance)
    get_amount_to_deposit = int(input("Insert the amount to deposit \n"))
    if previous_balance > get_amount_to_deposit:
        balance = previous_balance - get_amount_to_deposit
        print(balance)
    else:
        print("invalid amount inputted")


def deposit_operation(get_balance):
    print("Deposits operation")
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance

    previous_balance = get_current_balance(get_balance)
    get_amount_to_deposit = int(input("Insert the amount to deposit \n"))
    current_balance = previous_balance + get_amount_to_deposit
    print(current_balance)


def get_current_balance(user_details):
    return user_details[4]


def set_current_balance(user_details, balance):
    user_details[4] = balance


def logout():
    login()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


# ACTUAL BANKING SYSTEM ###
# print(generateAccountNumber())
init()
