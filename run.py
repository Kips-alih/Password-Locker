#!/usr/bin/env python3.8
from credential import Credential
from user import User
import random
import string


def create_new_user(username,password):
    """
    function that creates a user using a password and username
    """
    new_user = User(username,password) 
    return new_user


def save_user(user):
    """
    function that saves a new user
    """
    user.save_user()


def create_credential(accountName,username,password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(accountName,username,password)
    return new_credential


def save_credential(credential):
    """
    function to save credential
    """ 
    credential.save_credential()



def del_credential(credential):
    '''
    Function to delete a credential
    '''
    credential.delete_credential()



def find_credential(accountName):
    '''
    Function that finds a credential by accountname and returns the credential
    '''
    return Credential.find_by_accountName(accountName)



def check_existing_credentials(accountName):
    '''
    Function that check if a credential exists with that accountname and return a Boolean
    '''
    return Credential.credential_exist(accountName)


def display_credential():
    '''
    Function that returns all the saved credentials
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
    print("Hello Welcome to your password locker!Proceed to create your account")
    print("\n")
    
    print("Create account")
    print('-' * 50)
    print("Username")
    created_username = input()
    print("password")
    created_password = input()
    
    save_user(create_new_user(created_username,created_password))
    print("-"*20)
    print(f"Hello {created_username}, Account created succesfully! Your password is: {created_password}")
    print("\n")
    print("Proceed to login")
    print("username")
    entered_username=input()
    print("Your password")
    entered_password=input()
    while entered_password!=created_password or entered_username!=created_username:

        print("Invalid username or password")
        print("Username")
        entered_username=input()
        print("Password")
        entered_password=input()
    else :
      print(f"Welcome :{entered_username} to your account")
      print("\n")

    # user_name = input()


    # print(f"Hello {user_name}. what would you like to do?")

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

                    while True:
  
                      print("Use the following shortcodes : cp-create password or gp-to get a system generated password")
                      password_type = input().lower()
                      if password_type == 'cp':
                          password = input("Create your password\n")
                          break
                      elif password_type== "gp":
                          print('hello, Welcome to Password generator!')
                          length = int(input('\nEnter the length of password: '))
                          all = string.ascii_letters + string.digits 
                          password = "".join(random.sample(all,length))
                          print(f"Your generated password is : {password}")
                          break


                      
                      else:
                          print("Invalid shortcode please try again")
                    
                   
                    save_credential(create_credential(accountName,username,password))                    
                    print ('\n')
                    print(f"New Credential Account name:{accountName}, Username:{username},Password: {password}")
                    print ('\n')

            elif short_code == 'dc':

                    if display_credential():
                            print("Here is a list of all your credentials")
                            print('\n')

                            for credential in display_credential():
                                    print("Accountname: "+ str(credential.accountName) + "  Username: "+str(credential.username)+ "  password: " +str(credential.password))

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the accountName you want to search for")

                    search_accountName = input()
                    if check_existing_credentials(search_accountName):
                            search_credential = find_credential(search_credential)
                            print(f"{search_credential.accountName} {search_credential.Username}")

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
                        print(f"Your credentials for : {search_credential.accountName} successfully deleted!!!")
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
