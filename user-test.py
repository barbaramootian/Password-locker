import unittest
from user import user

class TestUser (unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    unittest.TestCase

def tearDown(self):
  user().user_list =[]  

def setUp(self):
       '''
        Set up method to run before each test cases.
        '''
self.new_user = user("Barbra", "Reson"  "babi" "@123babi")
    
def test_init_(self):
       '''
        test_init test case to test if the object is initialized properly
         '''

self.assertEqual(self.new_user.firstname,"Barbra")
self.assertEqual(self.new_user.lastname,"Reson")
self.assertEqual(self.new_user.username,"babi")
self.assertEqual(self.new_user.password,"@123babi")

def test_save_user(self):
    		'''
		Test to check if the new user info is saved into the user list
		'''
self.new_user.save_user()
self.assertEqual(len(User.users_list),1)

def test_display_user(self):
        '''
        a test to check the display accounts function
        '''
        self.assertEqual(User.display_user(),
                         User.user)

def test_save_user(self):
    '''
		Test to check if the new user info is saved into the user list
		'''
    self.new_user.save_user()
    testuser= User("Fiona", "Wanjiku", "phi" "phi@12")
    testuser.save_user()
    self.assertEqual(len(User.users_list),2)

def test_delete_user(self):
    '''
		Test to delete the new user info is saved into the user list
		'''
    self.new_user.delete_user()
    testuser= User("Fiona", "Wanjiku", "phi" "phi@12")
    testuser.delete_user()
    self.assertEqual(len(User.users_list),2)

def test_find_by_username(self):
        '''
		Test to find y username to return correct user
		'''
self.new_user.save_user()
testuser= user("Fiona", "Wanjiku", "phi" "phi@12")
testuser.save_user()
user_exists = User.find_by_username("phi")
self.assertEqual(user_exists,phi)


if __name__ == '__main__':
    unittest.main()