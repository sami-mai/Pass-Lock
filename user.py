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

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists in the user list.
        Args:
        username: username to search if the user exists
        Returns :
        Boolean: True or false depending if the user exists
        '''

        for user in cls.user_list:
            if user.username == username:
                return True

        return False
