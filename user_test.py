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


if __name__ == '__main__':
    unittest.main()
