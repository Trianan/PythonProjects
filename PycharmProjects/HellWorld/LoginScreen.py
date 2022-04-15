

logon = input("Log onto employee network? (y/n): ").lower()
if logon == 'y':
    log = True
else:
    log = False
    
tries = 0
members_list = ['Sara', 'Jon', 'Sam']
passwords = ['butterflies123','dudebruh420','dandruff']
user_name = ''
fullname = ''
role = ''
wage = ''

while log is True:

    print('WELCOME TO CORP.NET!')
    print(members_list)
    print(passwords)

    user_name = input('Name?: ').capitalize()

    if user_name in members_list:
        password = input('Password?: ')
        tries += 1
        if password in passwords:

            if user_name == 'Sara' and password == 'butterflies123':
                fullname = 'Sara Andrea Hubert'
                role = 'Cashier'
                wage = '$18.25'
            elif user_name == 'Jon' and password == 'dudebruh420':
                fullname = 'Jon Fredrick Anthony II'
                role = 'Night-shift meat clerk'
                wage = '$14.75'
            elif user_name == 'Sam' and password == 'dandruff':
                fullname = 'Samuel J. Willinkson'
                role = 'Cart guy'
                wage = '$14.34'
            elif user_name == 'Herb' and password == 'bird':
                fullname = 'Herbert Jimothy Dean'
                role = 'Pasta clerk'
                wage = '$14.00'

            else:
                print(f"Sorry {new_username}, your account is still being created!")
            profile = f'''
                                    Welcome {user_name}!

                                Employee name: {fullname}
                                Role: {role}
                                Wage: {wage}/hr.
                                    '''
            print(profile)

            diff_account = input("Log into a different account? (y/n): ").lower()
            if diff_account == 'n':
                log = False
            elif diff_account == 'y':
                log = True
            else:
                print('?')
        else:
             print('Incorrect password!')
             if tries == 3:
                 print('Too many attempts. You are locked out.')
                 log = False

    elif user_name not in members_list:
        while True:
            new_user = input('Name not in system. Add new user? (y/n): ').lower()
            if new_user == 'y':
                new_username = input('Enter new username: ')
                members_list.append(new_username)
                new_password = input('Enter new password: ')
                passwords.append(new_password)
                print('Returning to login...')
                break
            elif new_user == 'n':
                log = False
                break
            else:
                print('What?')

print('Logging off...')

