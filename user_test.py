import unittest # Importing the unittest module
from user import User # Importing the user class
import pyperclip

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Sami-mai","@samI!maI62") # create contact object


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Sami-mai")
        self.assertEqual(self.new_user.password,"@samI!maI62")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the user.
        '''
        self.new_user.save_user()
        test_user = User("S-Mai","!Smai@72",)
        test_user.save_user()

        user_exists = User.user_exist("S-Mai")
        self.assertTrue(user_exists)


if __name__ == '__main__':
    unittest.main()
