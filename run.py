
questions = [
    {
        "question": "What is programming?",
        "options": [
            " a) It's a robot"
            " b) solving problems using a computer"
        ],
        'answer': 'b'
    },

    {
        "question": "How many bits are there in a byte?",
        "options": [
            " a) 4"
            " b) 16"
            " c) 8"
        ],
        'answer': 'c'

    },

    {
        'question': 'What does the abbreviation IT stand for?',
        'options': [
           "a) Indoor technology"
           "b) Information technology"
           "c) Invasive technologi"
        ],
        'answer': 'b'
    },

    {
        'question': 'In computing there are 8 bits to a byte, but what'
        'are 4 bits called?',
        'options': [
           "a) A nibble"
           "b) A nipple"
           "c) A nizzle"
        ],
        'answer': 'a'
    },

    {
        'question': "What is the name given to a network designed to\n"
                    "allow communication within an organization?",
        'options': [
             'a) Internet'
             'b) Intranet'
             'c) Ethernet'
        ],
        'answer': 'a'

    }
]


def start_quizz():
    """
    Function defines the start of quizz
    """


    print('Hello, welcome to my Computer Quizz!\n')
    ask = True
    while ask:
        question = input('Are you ready to play (yes or no):').lower().strip()
        if question == 'yes':
            print('ok')
            enter_quizz()
        if question =='':
            print('Hey, you need to type either yes or no to play!')
        if question == 'no':
             print('~~~~~~~~~~~~~~~~~~~~~~')
             print('Okey, maybe next time.')
             print('~~~~~~~~~~~~~~~~~~~~~~')
             ask = False
             exit()





def enter_quizz():
    """
    Function to engage user and give responsive feedback.
    """


choice = input()
options = input()
TOTAL_QUESTIONS = 5
SCORE = 0

if question.lower() == 'yes':
    question_str = input('Please enter your name: \n')
    choice = input(f'Welcome,{question_str}! \n')
    choice_str = input('Please choose level 1 to play.\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'You chose level {choice_str}, good luck with your game!')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    question = input('4. What does the abbreviation IT stand for?\n')
    OPTIONS = "a) Indoor technology"
    "b) Information technology"
    if options.lower() == 'b':
        SCORE += 1
        print('well done, you got it right!')
    else:
        print('That was not the right answer, sorry.')


else:
   