import pyperclip
import random


class Cred:
    """Class that generates new instance of user credentials"""

    cred_list = []

    def __init__(self, accountName, email, username, password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            accountName: User's account name
            email: User's email
            username: User's username.
            password: User's password.
         '''
        self.accountName = accountName
        self.email = email
        self.username = username
        self.password = password

    def save_cred(self):
        '''
        save_cred method saves cred objects into cred_list
        '''
        Cred.cred_list.append(self)

    def delete_cred(self):
        '''
        delete_cred method deletes a saved account from the cred_list
        '''
        Cred.cred_list.remove(self)


    @classmethod
    def cred_exists(cls,accountName):
        '''
        Method that checks if a user's credentials exist in the cred list.
        Args:
        accountName: account name to search if the credentials exist.
        Returns :
        Boolean: True or false depending if the user's credentials exist.
        '''

        for cred in cls.cred_list:
            if cred.accountName == accountName:
                return True

        return False

    @classmethod
    def find_by_accountName(cls,accountName):
        '''
        Method that takes in an account name and returns the credentials that match that account name.

        Args:
            accountName: Account name to search for
        Returns :
            Full credentials that matches the accountName.
        '''

        for cred in cls.cred_list:
            if cred.accountName == accountName:
                return cred

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the cred list
        '''
        return cls.cred_list


    @classmethod
    def gen_password(cls,username):
        '''
        method that generates a random password based on the username
        '''
        for cred in cls.cred_list:
            letters = cred.username[1:3]
            num1 = random.randint(0,9)
            num2 = random.randint(9,16)
            gen_pass = "!"+ "num1" + "letters" + "num2"
            return gen_pass
