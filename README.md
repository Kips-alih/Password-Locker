# The Password-Locker

## By [Alphonce Kipngeno](https://github.com/Kips-alih) ,October 2021

## Description

Application that will help us manage our passwords and even generate new passwords for us.

## Setup/Installation Instructions

### To get the project into your local machine

* Open your terminal
* Create a folder and navigate to the folder you created.
* Run `git clone https://github.com/Kips-alih/Password-Locker.git`
* Run `cd Password-Locker` command to confirm it was successfully cloned.

### To run this application

* Open the cloned project in your editor e.g `code .` to open in visual studio code editor.
* On the terminal run these commands:
`chmod +x run.py`
`./run.py`

## User Stories

As a user, i want to :

* Create a password locker account with my details, a login username and password.
* Store my already existing account credentials in the application.
* Create new account credentials in the application and the application generates a password for me.
* Have the option of putting in a password that I want to use for the new credential account.
* View my various account credentials and their passwords in the application.
* Delete a credentials account that I no longer need in the application.

## Behavior Driven Development

|               Behaviour              | Input                            | Output                                               |
|:------------------------------------:|----------------------------------|------------------------------------------------------|
| Open the application on the terminal | Run the command **./run.py** | Hello Welcome to your password locker!Proceed to create your account |
| Create a username and password        | Enter a username of your choice and password     | Hello **username**,Account created succesfully! Your password is:**password**|
| Proceed to login |   Enter your **username** and **password** | Welcome: **username** to your account |
| Create new credential | Enter **cc** | Enter account name and username then enter **cp** to create your own password or **gp** to get a system generated password where you'll have to specify length of the password you need | New Credential **Account name**, **Username**,**Password** |
| Display stored credentials       |           Enter ***dc***         | A list of all credentials that has been stored or You don't have any credentials saved yet|
| Delete an existing credential that you no longer need| Enter **del** |Enter the account name of the Credential you want to delete and returns true if the it has been deleted and false if it doesn't exist|
|  Exit the application                |              Enter **ex**       | Exits the application |

## Technologies used

* Python3.8

## Support and contact details

Reach out to me through the following email addresses:

* alphonce.kipngeno@student.moringaschool.com.
* alphoncekipngeno@gmail.com.

### License

* LICENSED UNDER  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE).
