from credential import Credential

#Creating a contact
def create_credential(accountName,username,password):
    '''
    Function to create a new contact
    '''
    new_credential = Credential(accountName,username,password)
    return new_credential


def save_credential(credential):
    """
    function to save contacts
    """ 
    credential.save_credential()
#Delete contact
def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()

#Finding contact
def find_credential(accountName):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Credential.find_by_accountName(accountName)

#Check if contact exists
def check_existing_credentials(accountName):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return Credential.credential_exist(accountName)

#Displaying all contacts
def display_credential():
    '''
    Function that returns all the saved contacts
    '''
    return Credential.display_credential()

# #Copying email
# def copying_email():
#   '''
#   Function that copies email to the clipboard
#   '''
#   return Contact.copy_email()


#main function
def main():
    print("Hello Welcome to your password locker. What is your name?")

    user_name = input()


    print(f"Hello {user_name}. what would you like to do?")

    print('\n')


    while True:
            print("Use these short codes : cc - create a new credential, dc - display credentials,del - delete credential fc -find a credential, ex -exit the credential list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Credential")
                    print("-"*10)

                    print ("Account Name ....")
                    accountName = input()

                    print("Username ...")
                    username = input()

                    print("Password ...")
                    password=input()

                    # print("Email address ...")
                    # e_address = input()
                    save_credential(create_credential(accountName,username,password))                    
                    print ('\n')
                    print(f"New Credential name:{accountName}, username:{username}")
                    print ('\n')

            elif short_code == 'dc':

                    if display_credential():
                            print("Here is a list of all your contacts")
                            print('\n')

                            for credential in display_credential():
                                    print(f"{credential.accountName} {credential.username} .....{credential.password}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any contacts saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the accountName you want to search for")

                    search_accountName = input()
                    if check_existing_credentials(search_accountName):
                            search_credential = find_credential(search_credential)
                            print(f"{search_credential.accountName} {search_credential.Username}")
                            print('-' * 20)

                            print(f"Accountname.......{search_credential.accountName}")
                            print(f"Username.......{search_credential.username}")
                    else:
                            print("That credential does not exist")

            elif short_code == "del":


                print("Enter account name of the Credentials you want to delete")

                search_accountName = input()
                if find_credential(search_accountName):
                        search_credential = find_credential(search_accountName)
                        print("_"*40)
                        search_credential.delete_credential()
                        print('\n')
                        print(f"Your stored credentials for : {search_credential.accountName} successfully deleted!!!")
                        print('\n')
                else:
                        print("The Credential you want to delete does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()
