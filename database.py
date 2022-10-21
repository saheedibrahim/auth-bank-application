import os
import validation

# create record
# read record
# update record 
# delete record
# CRUD

# find user
user_data_path = 'data/user_record/'


def create(account_number, first_name, last_name, email, password, balance):
    # print('create a new user record')
    # create a file
    user_data = first_name + ',' + last_name + ',' + email + ',' + password + ',' + str(balance)
    if does_account_number_exist(account_number):
        return False
    if does_email_exist(email):
        print('User already exist')
        return False

    try:
        with open(user_data_path + str(account_number) + ".txt", "x") as f:
            f.write(str(user_data))
            return True
    except FileExistsError:
        does_file_contain_data = read(user_data_path + str(account_number) + '.txt')
        if not does_file_contain_data:
            delete(account_number)
        return False

    # return completion_state
    # the name of the file would be account_number.txt
    # add the user detail to the file
    # return true


def read(user_account_number):
    is_valid_account_number = validation.account_number_validation(user_account_number)
    try:
        if is_valid_account_number:
            f = open(user_data_path + str(user_account_number) + '.txt', 'r')
        else:
            f = open(user_data_path + user_account_number, 'r')
    except FileNotFoundError:
        return 'User not found'
    except TypeError:
        print('Invalid account number format')
    else:
        return f.readline()
    # find user with account number
    # fetch the content of the file


def update(user_account_number):
    print('delete user record')
    f = open(user_data_path + str(user_account_number) + '.txt', 'r')
    previous_data = str.split(f.readline(), ',')
    previous_amount = previous_data[4]
    print(previous_amount)

    # validation
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true


def delete(user_account_number):
    is_delete_successful = False
    if os.path.exists(user_data_path + str(user_account_number) + '.txt'):
        try:
            os.remove(user_data_path + str(user_account_number) + '.txt')
            is_delete_successful = True
        except FileNotFoundError:
            print('User not found')
        finally:
            return is_delete_successful
    # find user with account number
    # delete the user record (file)
    # return true


def does_email_exist(email):
    all_users = os.listdir(user_data_path)
    for user in all_users:
        user_list = str.split(read(user), ',')
        if email in user_list:
            return True
    return False
    # find user record in the data folder


def does_account_number_exist(account_number):
    all_users = os.listdir(user_data_path)
    for user in all_users:
        if user == str(account_number) + '.txt':
            return True
    return False


def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):
        user = str.split(read(account_number), ',')
        if password == user[3]:
            return True
    return False
# create(2644894503, ['Saheed', 'Ibrahim', 'saolabram@gmail.com', 'taajirun', 5000])
# delete(8490141367)
# does_email_exist(3188683442, 'saolabram@gmai.com')
# print(does_email_exist('ksmsj@fgt.mki'))
# print(read(4203963765))

# print(read(8490141367))
# print(read(3188683442))
update(5473602799)