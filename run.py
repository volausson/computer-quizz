"""
Questions for Quizz
"""

questions = [

    {
        'question': 'What does programming mean?',
        "options": [
          'a) To give instructions to a computer',
          'b) Play difficult games on the computer',
          'c) To build computers',
        ],
        'correct_answer': 'a'
    },
    {
        'question': 'In computing there are 8 bits to a byte, but what are 4 bits called?',
        'options': [
           "a) A nibble",
           "b) A nipple",
           "c) A nizzle"
        ],
        'correct_answer': 'a'
    },
    {
        'question': 'What is an algorithm?',
        'options': [
             'a) A robot',
             'b) A series of instructions',
             'c) A mathematical problem'
        ],
        'correct_answer': 'b'
    },
    {
        'question': 'What sort of animal is Tux, the official mascot of the Linux operating system?',

        'options': [
            'a) A fox',
            'b) A penguin',
            'c) A parrot'
        ],
        'correct_answer': 'b'
    },
    {
        'question': "What was the name of the world's first programmer?",
        'options': [
            'a) Adam Lovelace',
            'b) Ana Lovelace',
            'c) Ada Lovelace'
        ],
        'correct_answer': 'c'
    },
]


def start_quizz():
    """
    Function defines beginning of quizz and wishes Player
    welcome.
    """
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Hello, welcome to my Computer Quizz!\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    ask = True
    while ask:
        question = input('Are you ready to play?\nPlease enter y for yes or n for no:\n').lower().strip()
        if question == 'y':
            enter_quizz()
        if question == '':
            print('You need to type y for yes to play, or n for no to exit game!\n')
        if question == 'n':
            print('~~~~~~~~~~~~~~~~~~~~~~')
            print('Okey, maybe next time.')
            print('~~~~~~~~~~~~~~~~~~~~~~')
            ask = False
            exit()


def enter_quizz():
    """
    Function to engage user in quizz and give responsive feedback.
    """
    player_name = input('Please enter your name, otherwise I will just call you Player:\n').lower().strip()
    if player_name == '':
        player_name = 'Player'
    print(f'Hi, {player_name}, here comes your first question...')
    print('-----------------------------------------------------')
    play_quizz()


def play_quizz():
    """
    Function defines start of quizz.
    """
    score = 0

    for question in questions:
        print(question['question'])
        question_options = question['options']
        for option in question_options:
            print(option)
        player_choice = get_option_input()
        if player_choice == question['correct_answer']:
            score += 1
            print('----------------------------')
            print('Well done, you got it right!\nScore:', score)
            print('----------------------------')
            print('')

        else:
            score -= 1
            print('-------------------------------------')
            print('Sorry, wrong answer. You lost 1 point\nScore:', score)
            print('-------------------------------------')
            print('')

    end_game(score)


def get_option_input():

    """
    Function to define players input for options of answers.
    """
    player_input = input('\nEnter either a/b/c:\n').lower()
    if player_input == "" or player_input not in ["a", "b", "c"]:
        print('Incorrect input')
        return get_option_input()
    return player_input


def end_game(score):
    """
    This function ends the game, thank's Player for playing and informs
    of final score.
    """

    print('Thank you for playing, I hope you enjoyed the quizz.\n')
    print('You scored', score, 'out of 5\n      Well done!!!')
    print('')
    print(' ----- GAME OVER -----')
    print('')
    print('')


start_quizz()
