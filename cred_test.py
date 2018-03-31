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

    


if __name__ == '__main__':
    unittest.main()
