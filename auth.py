import random
import validation
import database
from getpass import getpass


# register
# - first name, last name, password, email
# - generate user account

# login
# - account-number and password

# bank operations

# initializing the system

# database = {
#     2644894503: ['Saheed', 'Ibrahim', 'saolabram@gmail.com', 'taajirun', 5000]
# }
# first_name + ',' + last_name + ',' + email + ',' + password + ',' + str(0)

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
            # password = input("What is your password? \n")
            password = getpass('What is your password \n')
            user = database.authenticated_user(account_number_from_user, password)
            if user:
                f = open('data/user_record/' + str(account_number_from_user) + '.txt', 'r')
                user_details = f.readline()
                bank_operation(user_details)

            # for accountNUmber, userDetails in database.items():
            #     if accountNUmber == int(account_number_from_user):
            #         if userDetails[3] == password:
            #             is_login_successful = True
            #             bank_operation(userDetails)
        else:
            print('Account number invalid: check that you have up to 10 digits and only integer')
            init()
        print("Invalid account or password")


def register():
    print("***** Register *****")
    email = input("What is your email? \n")
    is_valid_email_address = validation.email_address_validation(email)
    if is_valid_email_address:
        first_name = input("What is your first name? \n")
    else:
        print("Invalid email address")
        register()
    is_first_name_valid = validation.first_name_validation(first_name)
    if is_first_name_valid:
        last_name = input("What is your last name? \n")
    else:
        print("Invalid first name")
        register()
    is_last_name_valid = validation.last_name_validation(last_name)
    if is_last_name_valid:
        password = input("Create a password for yourself \n")
    else:
        print("one or more of the data above is invalid")
        register()
    is_password_valid = validation.password_validation(password)
    if is_password_valid:
        try:
            account_number = generate_account_number()
        except ValueError:
            print("Account generation failed due to internet connection")
    else:
        print('Password invalid')
    # user_prepared_details = first_name + ',' + last_name + ',' + email + ',' + password + ',' + str(0)
    is_user_created = database.create(account_number, first_name, last_name, email, password, 0)
    # database[account_number] = [first_name, last_name, email, password, 0]
    if is_user_created:
        print("Your account has been created")
        print("== ==== ==== ==== ===")
        print("Your account number is: %d" % account_number)
        print("Make sure you keep it save")
        print("== ==== ==== ==== ===")
        login()
    else:
        print('unable to create an account')
        register()

    # login()


def bank_operation(user_details):
    # print("Welcome %s %s" % (user[0], user[1]))
    selected_option = int(input("What would you like to do? (1) deposit (2)withdrawal (3) Logout (4) exit \n"))
    if selected_option == 1:
        deposit_operation(user_details)
        print("Do you want to perform another transaction?")
        another_transaction = int(input("(1) Yes (2) No \n"))
        if another_transaction == 1:
            bank_operation(user_details)
        elif another_transaction == 2:
            exit()
        else:
            print("You inputted an invalid option")
    elif selected_option == 2:
        withdrawal_operation(user_details)
        print("Do you want to perform another transaction?")
        another_transaction = int(input("(1) Yes (2) No \n"))
        if another_transaction == 1:
            bank_operation()
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
        bank_operation()


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


def logout():
    login()


def generate_account_number():
    return random.randrange(1111111111, 9999999999)


# ACTUAL BANKING SYSTEM ###
# print(generateAccountNumber())
init()
