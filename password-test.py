import unittest
from password import password

class TestPassword(unittest.TestCase):
    '''
    Test class that defines test cases for the password class behaviours.
    '''
    unittest.TestCase

def tearDown(self):
      password.account = []  

def setUp(self):
       '''
        Set up method to run before each test cases.
        '''
self.new_password = password("facebook", "@123babi")
    
def test_init_(self):
       '''
        test_init test case to test if the object is initialized properly
         '''

self.assertEqual(self.new_password.accountname,"Facebook")
self.assertEqual(self.new_password.password,"@123babi")

def test_save_password(self):
    		'''
		Test to check if the new password info is saved into the account
		'''
self.new_password.save_password()
self.assertEqual(len(password.account),1)

def test_display_password(self):
        '''
        a test to check the display accounts function
        '''
        self.assertEqual(Password.display_password(),
                         Password.user_password)

def test_save_password(self):
    '''
		Test to check if the new user info is saved into the user list
		'''
    self.new_password.save_password()
    testpassword= Password( "Facebook" "phi@12")
    testpassword.save_password()
    self.assertEqual(len(password.account),2)

def test_delete_password(self):
    '''
		Test to delete the new password info is saved into the user list
		'''
    self.new_password.delete_password()
    testpassword= Password( "Faceook" "phi@12")
    testpassword.delete_password()
    self.assertEqual(len(password.account),2)

def test_find_by_accountname(self):
        '''
		Test to find y username to return correct user
		'''
self.new_password.save_password()
testpassword= password()( "Facebook" "phi@12")
testpassword.save_password()
password_exists = Password.find_by_accountname("Facebook")
self.assertEqual(password_exists,Facebook)


if __name__ == '__main__':
    unittest.main()