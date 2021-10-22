import unittest # Importing the unittest module
from credential import Credential # Importing the credential class

class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    
    '''

# Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Facebook","Muriuki","0712345678") # create credential object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.accountName,"Facebook")
        self.assertEqual(self.new_credential.username,"Muriuki")
        self.assertEqual(self.new_credential.password,"0712345678")

    #tearDown method that does clean up after each test case has run.
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.credential_list = []

    #Test case for saving our credentials
    def test_save_credential(self):

        '''
        test_save_credential test case to test if the credential object is saved into
        the credential list
        '''
        self.new_credential.save_credential() # saving the new credential
        self.assertEqual(len(Credential.credential_list),1)

    #test case test_save_multiple_credential to test if we can save multiple credentials in our credential list.
    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credential to check if we can save multiple credential
            objects to our credential_list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","username","0712345678") # new credential
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

    #A test case for the feature to delete contacts
    def test_delete_credential(self):
            '''
            test_delete_contact to test if we can remove a credential from our credential list
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","username","0712345678") # new credential
            test_credential.save_credential()

            self.new_credential.delete_credential()# Deleting a credential object
            self.assertEqual(len(Credential.credential_list),1)

     #Test case to find credential by accountName
    def test_find_credential_by_accountName(self):
        '''
        test to check if we can find a credential by accoutName and display information
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","username","0712345678") # new contact
        test_credential.save_credential()

        found_credential = Credential.find_by_accountName("Test")

        self.assertEqual(found_credential.username,test_credential.username)

    #Test case to check if the credential object actually exists
    def test_credential_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the credential.
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","username","0712345678") # new credential
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Test")

        self.assertTrue(credential_exists)

    #Test case that test to check if we receive the list of the saved credentials
    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credential.display_credential(),Credential.credential_list)








if __name__ == '__main__':
    unittest.main()