# imports
import datetime

# dataBases
user_db = {
    'levi': {'Password': '123', 'Job': 'Maneger'},
    'adao': {'Password': '0000', 'Job': 'Sallesman'},
    'max': {'Password': '123', 'Job': 'God'}
}  # userDatabase
inventory_db = {
    'Papper': '50 Box',
    'Magazine': '187 Un',

}  # InventoryDatabase
# Global variables
login = False
date = datetime.datetime.today().strftime('%x')
user = 'Defalt'
page_index = 'Defalt'


# Program Head
def headimg():
    # banner
    print(' _      ________      ____     _______ _______ ______ __   __')
    print('| |    |  ____\ \    / /\ \   / / ____|__   __|  ____|  \/  |')
    print('| |    | |__   \ \  / /  \ \_/ / (___    | |  | |__  | \  / |')
    print('| |    |  __|   \ \/ /    \   / \___ \   | |  |  __| | |\/| |')
    print('| |____| |____   \  /      | |  ____) |  | |  | |____| |  | |')
    print('|______|______|   \/       |_| |_____/   |_|  |______|_|  |_|')
    print('                                                  ')
    print(f'=================== {page_index} =======================', date)


# start system
def startsys():
    if not login:
        global page_index
        page_index = 'Login Page'
        headimg()
        print('Type "Exit" if you want Quite')
        fun_login()


# login
def check_login(name,password):
    return True if name in user_db and password == user_db.get(name).get('Password') else False
def fun_login():
    # variables
    global user_db
    global login
    global user
    global page_index
    chances = 4
    page_index = 'Login Page'
    # Login Function
    while (not login) and chances > 0:
        # input user name
        user = input('User Name: ').lower()
        # verified if not empty spce or 'exit'
        while not user:
            print('Type something!')
            user = input('User Name: ').lower()
        if user == 'exit':
            print('Have a nice day! ')
            exit()
        # input password
        password = input('Password: ').lower()
        # verified if not empty spce or 'exit'
        while not password:
            print('Type something!')
            password = input('Password: ').lower()
        if password == 'exit':
            print('Have a nice day! ')
            exit()
        # verified  if have that user and password
        if check_login(user,password):
            login = True
            print(f'Welcome {user}!')
            user_menu()

        else: print('Invalid Username or Password')
        # chances for login
        chances -= 1
    # if exceeded the chances
    if chances == 0:
        print('You have exceeded the number of attempts ')
        startsys()


# User Menu
def user_menu():
    # variables
    global login
    global page_index
    page_index = 'User Page'
    # if login is true
    if login:
        # set Options
        headimg()
        print('Select Options: ', '1 - Acess  Inventory', '2 - User control', '3 - Logout',  sep='\n')
        anwser = input(' :')
        if anwser == '1':
            inventory()
        elif anwser == '2':
            user_control()
        elif anwser == '3':
            login = False
            print('Have a nice day! ')
            startsys()
        else:
            print('Type just one of options!')
            user_menu()


# Inventory Page
def inventory():
    # variables
    global login
    global page_index
    page_index = 'Inventory page'
    # if login is true
    if login:
        headimg()
        # loop for show inventory list
        for i in inventory_db.keys():
            print(i, inventory_db.get(i), sep=' ........... ')
        # option to input
        print('0 - Back', '1 - Quite', sep=' | ')
        anwser = input(':')
        if anwser == '0':  # Back option
            user_menu()
        elif anwser == '1':  # quite account
            login = False
            startsys()
        else:
            print('Type just one of options!')  # other anwsers
            inventory()


# User list Page
def user_control():
    # variable
    global login
    global page_index
    page_index = 'User control page'
    # Function to verified login
    if login:
        headimg()
        # loop for show user list
        for i in user_db.keys():
            print(i, user_db.get(i).get('Job'), sep=' ..................... ')
        print('  ')
        # options
        print('2 - For Edit Profile', '3 - For Register a new User', '4 - For Delete a user', sep=' | ')
        print('0 - Back', '1 - Quite', sep=' | ')
        anwser = input(':')
        if anwser == '0':  # Back
            user_menu()
        elif anwser == '1':  # Logout
            login = False
            startsys()
        elif anwser == '2':  # Edit Profile
            changeprofile()
        elif anwser == '3': #Register User
            registeruser()
        elif anwser == '4':  # Delete user
            deluser()
        else:  # other optons
            print('Type just one of options!')
            user_control()


# Register User page
def registeruser():
    # variables
    global login
    global page_index
    page_index = 'Register a new User'
    headimg()
    index = 0
    # if login is true
    if login:
        print('Type 0 to exit')
        # loop for input new user
        while index < 1:
            reg_user = input('Type Username: ').lower()  # input user
            if not reg_user:  # if empty
                print('Type Something!')
            elif reg_user == '0':  # if seclt exit
                user_menu()
            elif reg_user == user:
                print('You Can Not Register Your self dude :/')
            else:
                index += 1
            continue
        while index < 2:
            reg_password = input('Type Password: ')  # input password
            if not reg_password:  # if empty
                print('Type Something!')
            elif reg_password == 'exit':  # if seclt exit
                user_menu()
            else:
                index += 1
            continue
        while index < 3:
            reg_job = input('Type Job: ')  # input a job
            if not reg_job:  # if empty
                print('Type Something!')
            elif reg_job == '0':  # if seclt exit
                user_menu()
            else:
                index += 1
            continue

        user_db.update({reg_user: {'Password': reg_password, 'Job': reg_job}})
        print('User Registered!')
        # Close
        print('0 - Back', '1 - Quite')
        anwser = input(':')
        if anwser == '0':
            user_menu()
        elif anwser == '1':
            login = False
            startsys()
        else:
            print('Type just one of options!')


# delet user page
def deluser():
    # variables
    global login
    global page_index
    page_index = 'Delete user'
    headimg()
    # options
    print('User List: ', '                      0 - Back', '1 - Quite', sep='   |   ')
    index = 0
    if login:
        for i in user_db:  # loop to show user list
            print(i, user_db.get(i).get('Job'), sep=' .................. ')
        anwser = input('Type the name you want to delete: ')

        if anwser == '0':  # back otion
            user_menu()
        elif anwser == '1':  # exit option
            login = False
            startsys()
        elif anwser not in user_db:  # if the user typer for delete don't exist
            print("User don't finded")
            deluser()
        elif anwser == user:
            print('you can not delete your self sir!')
            deluser()
        elif anwser:  # if exist delete de current user
            user_db.pop(anwser)
            print('User Deleted')
            deluser()
        else:
            print('Type just one of options!')  # other options


# edit user profile page
def changeprofile():
    # variables
    global user
    global login
    global page_index
    page_index = 'Edit Profile'
    password = user_db.get(user).get('Password')
    job = user_db.get(user).get('Job')
    headimg()

    ##options
    print('Select the number of the information to change : ', 'or 0 - Back', sep='  |  ')
    print(f'1 - Name: {user}', f'2 - Password: {password}', f'3 - Job: {job}', sep='\n')
    anwser = input(':')
    # anwser
    if anwser == '1':  # Change name of user
        new_user = input('Type your new user name: ')
        user_db[new_user] = user_db[user]  # copy the select dicionary
        user_db.pop(user)  # delet the old
        user = new_user  # reatribute the new user for user
        print(f'your new name now is {new_user}')
        changeprofile()
    elif anwser == '2':  # change password
        new_password = input('Type your new Password: ')
        user_db.get(user)['Password'] = new_password
        print('Password changed! ')
        changeprofile()
    elif anwser == '3':  # change Job
        new_Job = input('Type your Job: ')
        user_db.get(user)['Job'] = new_Job
        print('Job Changed! ')
        changeprofile()
    elif anwser == '0':
        user_menu()
    else:
        print('Type just the Options!! ')
        changeprofile()


startsys()
