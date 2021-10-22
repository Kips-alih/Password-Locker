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
