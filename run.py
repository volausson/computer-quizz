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
    Function defines start of game
    """


print('Hi, welcome to my Computer Quizz!\n')

question = input('Are you ready to play (yes or no): \n').lower()
answer = input('Are you ready to play? yes or no:\n')
user_name = input()
SCORE = 0
TOT_Q = 5


if answer.lower() == 'yes':
    answer = input('Please enter your name: ')
    print('Welcome', user_name, ',please choose level 1, 2 or 3:')
else:
    print("Ok, maybe next time.")
