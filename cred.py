import pyperclip

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
