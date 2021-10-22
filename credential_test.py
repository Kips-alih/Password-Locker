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







if __name__ == '__main__':
    unittest.main()