def account_number_validation(account_number):
    # check if account number is not empty
    # if account number is 10digits
    # if the account number is an integer

    if account_number:
        if len(str(account_number)) == 10:
            try:
                int(account_number)
                return True
            except ValueError:
                print("Invalid account number")
                return False
            except TypeError:
                print("Invalid account type")
                return False
        else:
            print("Account number cannot be less or more than 10 digits")
    else:
        print("Account number is a required field")
        return False

def validation_registration_input(input):
    # check if it's a list
    # check each item in the list and be sure they are the correct data types