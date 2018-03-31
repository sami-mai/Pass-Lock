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

    


if __name__ == '__main__':
    unittest.main()
