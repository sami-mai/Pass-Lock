#!/usr/bin/env python3.6
from user import User

def create_user(fullname, email, username, password):
    '''
    Function to create a new user
    '''
    new_user = User(fullname, email, username, password)
    return new_user

def save_new_user(new_user):
    '''
    Function to save user
    '''
    new_user.save_user()

def check_existing_user(username):
    '''
    Function that check if a user exists/is logged in with that username and return a Boolean
    '''
    return User.user_exists(username)

def main():
    print("Welcome to PassLocker")
    print("-"*10)

    while True:
        print("Please use the following short codes:")
        print('\n')
        print ("su - Sign-up, li - Login", "ex - Exit")

        short_code = input().lower()

        if short_code == 'su':
            print("Sign up to create a PassLocker account")
            print("-"*10)

            print("Fullname.....")
            fullname = input()

            print("Email Address.....")
            email = input()

            print("Username.....")
            username = input()

            print("Password.....")
            password = input()

            save_new_user(User(fullname, email, username, password))
            print('\n')
            print(f"Welcome {username}, your account has sucessfully been created")
            print ('\n')

        elif short_code == 'li':
            print("Login to your PassLocker account")
            print("-"*10)

            i=0
            while i<3:
                i=i+1
                print("Username.....")
                username = input()
                if username == check_existing_user(username):

                    while i<3:
                        i=i+1
                        print("Password.....")
                        password = input()
                        if password == user.password:
                            print(f"Welcome {username}, you are logged in!")
                            break
                            break
                        else:
                            print("Incorrect password")

                else:
                    print(f"{username} does not exist, please sign up.")
        elif short_code == 'ex':
            print("Bye .......")
            break
        else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()
