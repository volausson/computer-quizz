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


def start_game():
    """
    Function defines start of game
    """


print('Hello, welcome to my Computer Quizz!\n')

question = input('Are you ready to play (yes or no): \n')
choice = input()
score = 0
total_question = 5


if question.lower() == 'yes':
    question_str = input('Please enter your name: \n')
    choice = input(f'Welcome,{question_str}! \n')
    choice_str = input('Please choose level 1, 2 or 3 to play.\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'You chose level {choice_str}, good luck with your game!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

else:
    print('~~~~~~~~~~~~~~~~~~~~~~')
    print('Okey, maybe next time.')
    print('~~~~~~~~~~~~~~~~~~~~~~')
