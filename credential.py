class Credential:
    """
    Class that generates new instances of credentials.
    """

    credential_list = [] # Empty credential list

    def __init__(self,accountName,username,password):

      # docstring removed for simplicity

        self.accountName = accountName
        self.username = username
        self.password = password

    #save_credential method that is called on a credential object and appends it to our credential-list list.
    def save_credential(self):

      '''
        save_credential method saves credential objects into credential_list
      '''

      Credential.credential_list.append(self)


    #the code to make the delete credential test pass.
    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credential.credential_list.remove(self)

    #code that makes the find user by accoutName pass       
    @classmethod
    def find_by_accountName(cls,accountName):
        '''
        Method that takes in a accountName and returns a credential that matches that accountName.

        Args:
            accountName: accountName to search for
        Returns :
            Credential that matches the accountName.
        '''

        for credential in cls.credential_list:
            if credential.accountName == accountName:
                return credential

    #code that makes the find if a credential object actually exists pass       
    @classmethod
    def credential_exist(cls,accountName):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            accountName: accountName to search for
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.accountName == accountName:
                return True

        return False

    #Code to make the display_credential test case pass.
    @classmethod
    def display_credential(cls):
        '''
        method that returns the credential list
        '''
        return cls.credential_list
