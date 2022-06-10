"""
Questions for Quizz
"""

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
        'question': 'What does programming mean',
        "options": [
          'a) To give instructions to a computer'
          'b) Play difficult games on the computer'
          'c) To build computers'
        ],
        'answer': 'a'
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

    },
    {
        'question': 'What is an algorithm?',
        'options': [
             'a) A robot'
             'b) A series of instructions'
             'c) A mathematical problem'
        ],
        'answer': 'b'
    },
    {
        'question': 'What sort of animal is Tux, the official mascot of the Linux operating system?',

        'options': [
            'a) A fox'
            'b) A penguin'
            'c) A parrot'
        ],
        'answer': 'b'
    },
    {
        'question': "What was the name of the world's first programmer?",
        'options': [
            'a) Adam Lovelace'
            'b) Ana Lovelace'
            'c) Ada Lovelace'
        ],
        'answer': 'c'
    },
    {
      'question': 'Who is considered the father of computers?',

      'options': [
        'a) Charles Gabbage'
        'b) Charles Cabbage'
        'c) Charles Babbage'
      ],
      'answer': 'c'
    },
    {
      'question': 'Who is considered to be The Father of Artificial Intelligence?',
      'options': [
               'a) John McCarthy'
               'b) John McArthur'
               'c) James McCarthy'
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
        if question == '':
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


TOTAL_QUESTIONS = 5
SCORE = 0

player_name = input('Please enter your name \n')
('Otherwise I will just call you player): ').lower().strip()
if player_name == '':
    print(f'Hi, {player_name}, here comes your first question...')
