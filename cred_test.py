import unittest
from cred import Cred
import pyperclip

class TestCred(unittest.TestCase):

    '''
    Test class that defines test cases for the Cred class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_cred = Cred("Facebook","sami.mai@gmail.com","Sami-maifb","@samI!maI4fb")


    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''

        Cred.cred_list = []

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_cred.accountName,"Facebook")
        self.assertEqual(self.new_cred.email,"sami.mai@gmail.com")
        self.assertEqual(self.new_cred.username,"Sami-maifb")
        self.assertEqual(self.new_cred.password,"@samI!maI4fb")

    def test_save_cred(self):
        '''
        test_save_cred test case to test if the cred object is saved into
         the cred list
        '''
        self.new_cred.save_cred()
        self.assertEqual(len(Cred.cred_list),1)

    def test_cred_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the user's credentials.
        '''
        self.new_cred.save_cred()
        test_cred = Cred("facebook","steph.bart@gmail.com","Bart-Menz","!Bmenz@fb")
        test_cred.save_cred()

        cred_exists = Cred.cred_exists("facebook")
        self.assertTrue(cred_exists)

    def test_find_cred_by_accountName(self):
        '''
        test to check if we can find a user's credentials by accountName and display information
        '''
        self.new_cred.save_cred()
        test_cred = Cred("facebook","steph.bart@gmail.com","Bart-Menz","!Bmenz@fb")
        test_cred.save_cred()

        found_cred = Cred.find_by_accountName("facebook")

        self.assertEqual(found_cred.accountName,test_cred.accountName)

    def test_display_all_credentials(self):
        '''
        test to check if we can display all the accounts a user has
        '''
        self.assertEqual(Cred.display_accounts(),Cred.cred_list)

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove an account from our cred list
            '''
            self.new_cred.save_cred()
            test_cred = Cred("facebook","steph.bart@gmail.com","Bart-Menz","!Bmenz@fb")
            test_cred.save_cred()

            self.new_cred.delete_cred()
            self.assertEqual(len(Cred.cred_list),1)    


if __name__ == '__main__':
    unittest.main()
