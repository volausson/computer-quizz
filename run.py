import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('computer_quizz')


def welcome():
    """
    Function defines start of game and gives choise of wich
    level to play
    """


print('Hi, welcome to my Computer Quizz!\n')


answer = input('Are you ready to play? yes or no:\n')
name = input()


if answer.lower() == 'yes':
    answer = input('Please enter your name: ')
    print('Welcome', name, ',please choose level 1, 2 or 3:')
else:
    print("Ok, mayby next time.")
