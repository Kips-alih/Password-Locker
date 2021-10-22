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
