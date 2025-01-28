# coding: utf-8
#Hello Dave, I hope you like my program!!!!
# hw1pr3.py
#I worked alone

import random          # imports the library named random

def rps():
    """ this plays a game of rock-paper-scissors
        (or a variant of that game)
        arguments: no arguments    (prompted text doesn't count as an argument)
        results: no results        (printing doesn't count as a result)
    """
    user = input("Choose your weapon (rock, paper, or scissors) (LOWERCASE ONLY) (ALSO IF USER TIES WITH ME I WIN!): ")
    comp = random.choice(['rock','paper','scissors'])
    print()

    print('The user (you)   chose', user)
    print('The computer (I) chose', user)
    print()

    if user == 'rock':
        print('Ha! We really tied--I WIN!')
    elif user =='paper':
        print('Wow it seems like no matter what you choose I win!')
    elif user == 'scissors':
        print('Sorry you lose again! (:  )')
    else:
        print ('HAHAHAH, I win again, we both chose', user, "!")

    print("Better luck next time...")
