from cred import Cred

def create_cred(accountName, email, username, password):
    '''
    Function to create new credentials
    '''
    new_cred = User(accountName, email, username, password)
    return new_cred

def save_new_cred(new_cred):
    '''
    Function to save credentials
    '''
    new_cred.save_cred()

def del_cred(cred):
    '''
    Function to delete credentials
    '''
    cred.delete_cred()

def check_existing_cred(accountName):
    '''
    Function that check if credentials exist with that accountName and return a Boolean
    '''
    return Cred.cred_exists(accountName)

def find_cred(accountName):
    '''
    Function that finds a user's credentials by accountName and returns the credentials
    '''
    return Cred.find_by_accountName(accountName)

def gen_password(username):
    '''
    Function that generates a random password using the given username
    '''
    return Cred.gen_password(username)

def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Cred.display_accounts()


def main():

    while True:
        print("Please use the following short codes:")
        print("""
        add - Add & save existing accounts, gen - Generate password for new account,
        disp - display accounts, del - Delete account, lo - Log out
        """)

        short_code = input().lower()

        if short_code == 'add':
            print ('\n')
            print("Add new account")
            print("-"*10)

            print("Account Name.....")
            accountName = input()

            print("Email Address.....")
            email = input()

            print("Username.....")
            username = input()

            print("Password.....")
            password = input()

            save_new_cred(Cred(accountName, email, username, password))
            print('\n')
            print(f"Your {accountName} account has successfully been added!")
            print ('\n')

        elif short_code == 'gen':
            print ('\n')
            print("A random password will be created for this account")
            print("-"*30)

            print("Account Name.....")
            accountName = input()

            print("Email Address.....")
            email = input()

            print("Username.....")
            username = input()

            password = gen_password(username)
            print(f"Your password is {password}")
            save_new_cred(Cred(accountName, email, username, password))
            print('\n')
            print(f"Your {accountName} account has successfully been added!")
            print ('\n')

        elif short_code == 'disp':
            if display_accounts():
                print ('\n')
                print("Here is a list of all your accounts")
                print('\n')

                for cred in display_accounts():
                    print(f"{cred.accountName}, {cred.email}, {cred.username}, {cred.password}")
                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')

        elif short_code == 'del':
            print ('\n')
            print("What is the name of the account you want to delete?...")
            accountName = input()
            if find_cred(accountName):
                del_cred(Cred((accountName, email, username, password)))
                print('\n')
                print(f"Your {accountName} account has successfully been deleted!")
                print ('\n')

        elif short_code == 'lo':
            print ('\n')
            print("Sorry to see you go... Come back soon!")
            print ('\n')
            break

        else:
            print ('\n')
            print("I really didn't get that. Please use the short codes")
            print ('\n')

if __name__ == '__main__':
    main()
