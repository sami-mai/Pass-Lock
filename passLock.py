import pyperclip

class User:
    """Class that generates new instance of users"""

    user_list = []
    def __init__(self, username, password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            username: New user's username.
            password: New user's password.
         '''
        self.username = username
        self.password = password
