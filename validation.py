import re


def account_number_validation(account_number):
    # check if account number is not empty
    # if account number is 10digits
    # if the account number is an integer

    if account_number:
        try:
            int(account_number)
            if len(str(account_number)) == 10:
                return True
            # else:
            #     print("Account number cannot be less or more than 10 digits")
        except ValueError:
            # print("Invalid account number")
            return False
        except TypeError:
            # print("Invalid account type")
            return False
    else:
        print("Account number is a required field")
        return False


# def validation_registration_input(input):
# check if it's a list
# check each item in the list and be sure they are the correct data types

def email_address_validation(email):
    pat = "^[A-Za-z0-9-_]+@[A-Za-z0-9]+\.[a-z]{1,3}$"
    if re.match(pat, email):
        return True
    else:
        return False


def first_name_validation(first_name):
    if first_name.isalpha():
        return True
    else:
        return False


def last_name_validation(last_name):
    if last_name.isalpha():
        return True
    else:
        return False


def password_validation(password):
    special_char = ['$', '@', '#', '%']
    val = False
    if len(password) < 8:
        val = False
    elif len(password) > 20:
        val = False
    elif not any(char.isdigit() for char in password):
        val = False
    elif not any(char.isupper() for char in password):
        val = False
    elif not any(char.islower() for char in password):
        val = False
    elif not any(char in special_char for char in password):
        val = False
    else:
        return True

    # is_last_name_valid = validation.last_name_validation(last_name)
    # if is_last_name_valid:
    #     password = input("Create a password: Password should contain a digit, uppercase, lowercase, special character, more than 8 character and less than 20\n")
