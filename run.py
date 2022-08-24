"""
Questions for Quizz
"""
import random

questions = [

    {
        'question': 'What does programming mean',
        "options": [
          'a) To give instructions to a computer',
          'b) Play difficult games on the computer',
          'c) To build computers',
        ],
        'correct_answer': 'a'
    },
    {
        'question': 'In computing there are 8 bits to a byte, but what'
        'are 4 bits called?',
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

random.sample(questions, 5)


def start_quizz():
    """
    Function defines the start of quizz
    """
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Hello, welcome to my Computer Quizz!\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    ask = True
    while ask:
        question = input('Are you ready to play (yes or no):\n').lower().strip()
        if question == 'yes':
            enter_quizz()
        if question == '':
            print('You need to type either yes or no to play!\n')
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
    player_name = input('Please enter your name (otherwise I will just call you player):\n').lower().strip()
    if player_name == '':
        player_name = 'player'
    print(f'Hi, {player_name}, here comes your first question...')
    play_quizz()


def play_quizz():
    """
    The Quizz begins.
    """
    tot_q = 5
    score = 0

    for question in questions:
        print(question['question'])
        question_options = question['options']
        for option in question_options:
            print(option)
        player_choice = get_option_input()
        if player_choice == question['correct_answer']:
            score += 1
            print('Well done, you got it right!')
        else:
            print('Wrong answer\n')
    end_game()


def get_option_input():

    player_input = input('\nEnter either a/b/c:\n').lower()
    if player_input == "" or player_input not in ["a", "b", "c"]:
        print('That was not the right answer\nPlease try again.')
        return get_option_input()
    return player_input


def end_game():
    """
    This ends the game and provides user a thank you and some information
    """
    print("Thank you for playing my first python quiz game\n")
    print('You scored', {score}, 'out of 5')
    mark = (score/tot_q) * 100

    print('Mark:', {mark}, + '%')
    print('Game Over')


start_quizz()
