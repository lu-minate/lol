# this turned out quite good
# i used few new things that i learned from the python course
# i wouldn't say i did it all by myself
# but the 1st code i wrote was fairly close to the final product
# good job, proud of you

import random

options = {
    'r': 'Rock',
    'p': 'Paper',
    's': 'Scissor'
}


def play():
    user = input("pick one\n'r' for Rock\n'p' for Paper\n's' for Scissors\n> ")
    computer = random.choice(['r', 'p', 's'])
    print(f' You chose {options[user] } :: Computer chose {options[computer]}')

    if user == computer:
        return "It's a tie!"
    elif is_win(user, computer):
        return "You win!"

    return "You lose!"


def is_win(player1, player2):
    # return true if player wins
    if (player1 == 'r' and player2 == 's') or (player1 == 'p' and player2 == 'r') or (player1 == 's' and player2 == 'p'):
        return True


print(play())
