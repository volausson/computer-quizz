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

questions : [
    {
        'question': 'What is programming?'
        'options': [
            " a) It's a robot"
            " b) solving problems using a computer"
        ],
        'answer': 'b'
    },

    {
        'question': 'What does the abbreviation IT stand for?'
        'options' [
           "a) Indoor technology"
           "b) Information technology"
        ],
        'answer': 'b'
    },

    {
        'question': 'In computing there are 8 bits to a byte, but what'
        'are 4 bits called?'
        'options' [
           "a) A nibble"
           "b) A nipple"
        ],
        'answer': 'a'
    }
]


def start_game():
    """
    Function defines the start of start of the game.
    """


print('Hello, welcome to my Computer Quizz!\n')

question = input('Are you ready to play (yes or no): \n')
choice = input()
OPTIONS = input()
TOTAL_QUESTIONS = 5
SCORE = 0

if question.lower() == 'yes':
    question_str = input('Please enter your name: \n')
    choice = input(f'Welcome,{question_str}! \n')
    choice_str = input('Please choose level 1 to play.\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'You chose level {choice_str}, good luck with your game!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    question = input('1. What is programming?\n')
    options = input("Is it 'a' a robot,\n"
                    "or is it 'b', solving problems using a computer?\n")

    if options.lower() == 'b':
        SCORE += 1
        print('well done, you got it right!')
    else:
        print('That was not the right answer, sorry.')

    question = input('2. How many bits are there in a byte??\n')

    if question.lower() == '8':
        SCORE += 1
        print('well done, you got it right!')
    else:
        print('That was not the right answer, sorry.')

    question = input('3. What is the name given to a network designed to\n'
                     'allow communication within an organization??\n')

    if question.lower() == 'intranet':
        SCORE += 1
        print('well done, you got it right!')
    else:
        print('That was not the right answer, sorry.')

    question = input('4. What does the abbreviation IT stand for?\n')
    OPTIONS = "a) Indoor technology"
    "b) Information technology"
    if options.lower() == 'b':
        SCORE += 1
        print('well done, you got it right!')
    else:
        print('That was not the right answer, sorry.')

        question = input('5. In computing there are 8 bits to a byte,\n'
                         'what are 4 bits called??\n')

    if question.lower() == 'a nibble':
        SCORE += 1
        print('well done, you got it right!')
    else:
        print('That was not the right answer, sorry.')


else:
    print('~~~~~~~~~~~~~~~~~~~~~~')
    print('Okey, maybe next time.')
    print('~~~~~~~~~~~~~~~~~~~~~~')
