import os
# create record
# read record
# update record 
#deete record
# CRUD

# find user
user_data_path = 'data/user_record/'

def create(account_number, user_details):
    # print('create a new user record')
    # create a file

    try:
        with open(user_data_path + str(account_number) + ".txt", "x") as f:
            f.write(str(user_details))
            return  True
    except FileExistsError:
        print('User already exist')
        return False

    # return completion_state
    # the name of the file would be account_number.txt
    # add the user detail to the file
    # return true

def read(user_account_number):
    try:
        with open('data/user_record/' + str(user_account_number) + '.txt', 'r') as f:
            return f.readline()
    except FileNotFoundError:
        return 'User not found'
    # find user with account number
    # fetch the content of the file

def update(user_account_number):
    print('delete user record')
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
    # delete the user reord (file)
    # return true

def find(user_account_number):
    print('find user')
    # find user record in the data folder

# create(2644894503, ['Saheed', 'Ibrahim', 'saolabram@gmail.com', 'taajirun', 5000])
# delete(8490141367)
print(read(4203963765))
print(read(8490141367))
print(read(3188683442))