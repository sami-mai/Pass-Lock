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
        self.new_user = User("Samirah Maison","sami.mai@gmail.com","Sami-mai","@samI!maI62") # create contact object


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        User.user_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.fullname,"Samirah Maison")
        self.assertEqual(self.new_user.email,"sami.mai@gmail.com")
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
        test_user = User("Stephanie Bart","steph.bart@gmail.com","Bart-Menz","!Bmenz@72")
        test_user.save_user()

        user_exists = User.user_exists("Bart-Menz")
        self.assertTrue(user_exists)

    def test_find_user_by_username(self):
        '''
        test to check if we can find a user by user and display information
        '''

        self.new_user.save_user()
        test_user = User("Stephanie Bart","steph.bart@gmail.com","Bart-Menz","!Bmenz@72")
        test_user.save_user()

        found_user = User.find_by_username("Bart-Menz")

        self.assertEqual(found_user.password,test_user.password)


if __name__ == '__main__':
    unittest.main()
